def visitProgram(self, ast, o):
    scope = Scope(o, [])

    # First look: check redeclarations of global variables/functions
    scope.global_env = functools.reduce(lambda a, b: a + [b.accept(self, a)], ast.decl, scope.global_env)

    # Second look: check other errors
    [x.accept(self, scope) for x in ast.decl]


def visitVarDecl(self, ast, o):
    if not isinstance(o, Scope):
        if self.checkRedeclared(ast.variable.name, o, Variable()):
            return Symbol(ast.variable.name, ast.varInit.accept(self, o) if ast.varInit is not None else Unknown())


def visitFuncDecl(self, ast, o):
    if not isinstance(o, Scope):
        return self.visitFuncDeclFirstCheck(ast, o)
    else:
        return self.visitFuncDeclSecondCheck(ast, o)


def visitFuncDeclFirstCheck(self, ast, o):
    if self.checkRedeclared(ast.name.name, o, Function()):
        return Symbol(ast.name.name, MType([], Unknown()))


def visitFuncDeclSecondCheck(self, ast, o):
    # check redeclared parameter
    paramLst = functools.reduce(
        lambda a, b: a + [Symbol(b.variable.name, b.varInit.accept(self, o) if b.varInit is not None else Unknown())]
        if self.checkRedeclared(b.variable.name, a, Parameter()) else a, ast.param, [])

    # check redeclared variable in function
    varLst = functools.reduce(
        lambda a, b: a + [Symbol(b.variable.name, b.varInit.accept(self, o) if b.varInit is not None else Unknown())]
        if self.checkRedeclared(b.variable.name, a, Variable()) else a, ast.body[0], paramLst)

    o.local_env = varLst
    # create scope for function and iterate through all stmts
    [x.accept(self, o) for x in ast.body[1]]


def visitAssign(self, ast, o):
    print(o.local_env)
    # get type
    leftSymbol = ast.lhs.accept(self, o)
    leftType = leftSymbol.mtype if isinstance(leftSymbol, Symbol) else leftSymbol
    rightSymbol = ast.rhs.accept(self, o)
    rightType = rightSymbol.mtype if isinstance(rightSymbol, Symbol) else rightSymbol

    if isinstance(leftType, VoidType):
        raise TypeMismatchInStatement(ast)
    if not isinstance(leftType, type(rightType)) and not isinstance(leftType, Unknown):
        raise TypeMismatchInStatement(ast)
    if isinstance(leftType, Unknown):
        if isinstance(rightType, Unknown):
            raise TypeCannotBeInferred(ast)
        else:
            obj = self.inferType(leftSymbol, o, rightType)
            return obj


def inferType(self, inferObj, o, typ):
    for i in range(len(o.local_env)):
        if inferObj == o.local_env[i]:
            o.local_env[i].mtype = typ
            return o
    for i in range(len(o.global_env)):
        if inferObj == o.global_env[i]:
            o.global_env[i].mtype = typ
            return o