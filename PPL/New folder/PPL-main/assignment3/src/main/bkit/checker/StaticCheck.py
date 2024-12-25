"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *
from functools import reduce


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_to_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]

    def lookup(self, name, lst):
        for x in lst:
            for y in x:
                if name == y.name:
                    return y
        return None

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def main_exist(self, ast):
        main_defined = False
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) and decl.name.name == 'main':
                main_defined = True
                break
        return main_defined

    def infer_type(self, obj, env, typ):
        for i in env[0] + env[1]:
            if obj == i:
                if isinstance(i.mtype, MType):
                    i.mtype.restype = typ
                else:
                    i.mtype = typ
        return env

    def infer_mtype(self, obj, env, typ):
        for i in range(len(env[1])):
            if isinstance(env[1][i], Symbol):
                for j in range(len(env[1][i].mtype.intype)):
                    if obj == env[1][i].mtype.intype[j]:
                        env[1][i].mtype.intype[j] = typ
        return env

    def visitProgram(self, ast, env):
        decl_list = [env, []]
        if not self.main_exist(ast):
            raise NoEntryPoint()

        for i in ast.decl:
            if isinstance(i, VarDecl):
                decl_list[0].append(i.accept(self, decl_list))
            elif isinstance(i, FuncDecl):
                returnType = Unknown()
                # for stmt in i.body[1]:
                #     if isinstance(stmt, Return):
                #         returnType = stmt.expr.accept(self, decl_list)
                func = Symbol(i.name.name, MType([(x.varInit.accept(self, decl_list) if x.varInit is not None else Unknown()) for x in i.param], returnType))

                for y in decl_list[0]:
                    if i.name.name == y.name:
                        raise Redeclared(Function(), i.name.name)
                decl_list[0].append(func)

        for i in ast.decl:
            if isinstance(i, FuncDecl):
                i.accept(self, decl_list)

    def visitVarDecl(self, ast, env):
        for i in env[0]:
            if ast.variable.name == i.name:
                raise Redeclared(Variable(), ast.variable.name)
        return Symbol(ast.variable.name, ast.varInit.accept(self, env) if ast.varInit is not None else Unknown())

    def visitFuncDecl(self, ast, env):
        local_env = []
        para_list = []
        is_declared = self.lookup(ast.name.name, [env[0],env[1]])

        for param in ast.param:
            if param.variable.name in (para_list[i].name for i in range(len(para_list))):
                raise Redeclared(Parameter(), param.variable.name)
            else:
                para_list.append(Symbol(param.variable.name,param.varInit.accept(self, env) if param.varInit is not None else Unknown()))

        local_env.append(para_list)
        for decl in ast.body[0]:
            local_env.append(decl.accept(self, local_env))

        returnType = Unknown()
        # for stmt in ast.body[1]:
        #     if isinstance(stmt, Return) and stmt.expr is None:
        #         returnType = VoidType()
        #     elif isinstance(stmt, Return) and stmt.expr is not None:
        #         returnType = stmt.expr.accept(self, env)

        para_lst = reduce(lambda x, y: [[y.accept(self, x)] + x[0], env[0] + [Symbol(ast.name.name, MType([(i.varInit.accept(self, env) if i.varInit is not None else Unknown()) for i in ast.param], returnType))] + env[1]], ast.param,
                          [[], env[0] + [Symbol(ast.name.name, MType([(i.varInit.accept(self, env) if i.varInit is not None else Unknown()) for i in ast.param], returnType))] + env[1]])

        var_lst = reduce(lambda x, y: [[y.accept(self, x)] + x[0], para_lst[1]], ast.body[0], para_lst)

        for stmt in ast.body[1]:
            if isinstance(stmt, Return):
                self.infer_type(is_declared, env, stmt.accept(self, var_lst))
            stmt.accept(self, var_lst)

    def visitId(self, ast, env):
        is_declared = self.lookup(ast.name, [env[0], env[1]])
        if is_declared is None:
            raise Undeclared(Identifier(), ast.name)
        return is_declared

    def visitBinaryOp(self, ast, env):
        leftSymbol = ast.left.accept(self, env)
        leftType = leftSymbol.mtype if isinstance(leftSymbol, Symbol) else leftSymbol
        leftFuncType = leftType.restype if isinstance(leftType, MType) else leftType
        rightSymbol = ast.right.accept(self, env)
        rightType = rightSymbol.mtype if isinstance(rightSymbol, Symbol) else rightSymbol
        rightFuncType = rightType.restype if isinstance(rightType, MType) else rightType
        if ast.op in ['+', '-', '*', '\\', '%']:
            # type check
            if not isinstance(leftFuncType, (IntType, Unknown)) or not isinstance(rightFuncType, (IntType, Unknown)):
                raise TypeMismatchInExpression(ast)
            # type infer
            if isinstance(leftFuncType, Unknown):
                self.infer_type(leftSymbol, env, IntType())
            if isinstance(rightFuncType, Unknown):
                self.infer_type(rightSymbol, env, IntType())
            return IntType()
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            # type check
            if not isinstance(leftFuncType, (FloatType, Unknown)) or not isinstance(rightFuncType, (FloatType, Unknown)):
                raise TypeMismatchInExpression(ast)
            # type infer
            if isinstance(leftFuncType, Unknown):
                self.infer_type(leftSymbol, env, FloatType())
            if isinstance(rightFuncType, Unknown):
                self.infer_type(rightSymbol, env, FloatType())
            return FloatType()
        elif ast.op in ['>', '>=', '<', '<=', '==', '!=']:
            # type check
            if not isinstance(leftFuncType, (IntType, Unknown)) or not isinstance(rightFuncType, (IntType, Unknown)):
                raise TypeMismatchInExpression(ast)
            # type infer
            if isinstance(leftFuncType, Unknown):
                self.infer_type(leftSymbol, env, IntType())
            if isinstance(rightFuncType, Unknown):
                self.infer_type(rightSymbol, env, IntType())
            return BoolType()
        elif ast.op in ['>.', '>=.', '<.', '<=.', '=/=']:
            # type check
            if not isinstance(leftFuncType, (FloatType, Unknown)) or not isinstance(rightFuncType, (FloatType, Unknown)):
                raise TypeMismatchInExpression(ast)
            # type infer
            if isinstance(leftFuncType, Unknown):
                self.infer_type(leftSymbol, env, FloatType())
            if isinstance(rightFuncType, Unknown):
                self.infer_type(rightSymbol, env, FloatType())
            return BoolType()
        elif ast.op in ['&&', '||']:
            # type check
            if not isinstance(leftFuncType, (BoolType, Unknown)) or not isinstance(rightFuncType, (BoolType, Unknown)):
                raise TypeMismatchInExpression(ast)
            # type infer
            if isinstance(leftFuncType, Unknown):
                self.infer_type(leftSymbol, env, BoolType())
            if isinstance(rightFuncType, Unknown):
                self.infer_type(rightSymbol, env, BoolType())
            return BoolType()

    def visitUnaryOp(self, ast, env):
        operandSymbol = ast.body.accept(self, env)
        operandType = operandSymbol.mtype if isinstance(operandSymbol, Symbol) else operandSymbol
        operandFuncType = operandType.restype if isinstance(operandType, MType) else operandType
        if ast.op == '-':
            if not isinstance(operandFuncType, (IntType, Unknown)):
                raise TypeMismatchInExpression(ast)
            if isinstance(operandType, Unknown):
                self.infer_type(operandSymbol, env, IntType())
            return IntType()
        elif ast.op == '-.':
            if not isinstance(operandFuncType, (FloatType, Unknown)):
                raise TypeMismatchInExpression(ast)
            if isinstance(operandType, Unknown):
                self.infer_type(operandSymbol, env, FloatType())
            return FloatType()
        elif ast.op == '!':
            if not isinstance(operandFuncType, (BoolType, Unknown)):
                raise TypeMismatchInExpression(ast)
            if isinstance(operandType, Unknown):
                self.infer_type(operandSymbol, env, BoolType())
            return BoolType()

    def visitCallExpr(self, ast, env):
        args_lst = [x.accept(self, env) for x in ast.param]
        is_declared = self.lookup(ast.method.name, [env[0], env[1]])

        if is_declared is None or not isinstance(is_declared.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        # check same number of parameter
        elif len(is_declared.mtype.intype) != len(args_lst) or not isinstance(is_declared.mtype.intype, list):
            raise TypeMismatchInExpression(ast)

        # check same type of each corresponding parameter
        else:
            for i in range(len(args_lst)):
                if isinstance(args_lst[i], Symbol):
                    if isinstance(is_declared.mtype.intype[i], Unknown):
                        if isinstance(args_lst[i].mtype, Unknown):
                            return "cannot infer"
                        else:
                            self.infer_mtype(is_declared.mtype.intype[i], env, args_lst[i].mtype)
                    else:
                        if isinstance(args_lst[i].mtype, Unknown):
                            args_lst[i].mtype = is_declared.mtype.intype[i]
                    if isinstance(is_declared.mtype.intype[i], type(args_lst[i].mtype)):
                        continue
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    if isinstance(is_declared.mtype.intype[i], Unknown):
                        if isinstance(args_lst[i], Unknown):
                            return "cannot infer"
                        else:
                            self.infer_mtype(is_declared.mtype.intype[i], env, args_lst[i])
                    else:
                        if isinstance(args_lst[i], Unknown):
                            args_lst[i] = is_declared.mtype.intype[i]
                    if isinstance(is_declared.mtype.intype[i], type(args_lst[i])):
                        continue
                    else:
                        raise TypeMismatchInExpression(ast)
            return is_declared

    def visitArrayCell(self, ast, env):
        arrSymbol = ast.arr.accept(self, env)
        is_declared = self.lookup(arrSymbol.name, [env[0], env[1]])
        # print()
        if is_declared is None:
            raise Undeclared(Identifier(), arrSymbol.name)

        for idx in ast.idx:
            idxSymbol = idx.accept(self,env)
            idxType = idxSymbol.mtype if isinstance(idxSymbol, Symbol) else idxSymbol
            idxFuncType = idxType.restype if isinstance(idxType, MType) else idxType
            if isinstance(idxFuncType, Unknown):
                idx_declared = self.lookup(idxSymbol.name, [env[0], env[1]])
                self.infer_type(idx_declared.name, env, IntType())
            if not isinstance(idxFuncType, IntType):
                raise TypeMismatchInExpression(ast)
        if isinstance(is_declared.mtype, MType):
            if isinstance(is_declared.mtype.restype, Unknown):
                return "cannot infer"
        if isinstance(is_declared.mtype, Unknown):
            raise TypeMismatchInExpression(ast)

        lst = is_declared.mtype.dimen if isinstance(is_declared.mtype, ArrayType) else is_declared.mtype.restype.dimen
        typ = is_declared.mtype if isinstance(is_declared.mtype, ArrayType) else is_declared.mtype.restype
        if len(lst) != len(ast.idx) or not isinstance(typ, ArrayType):
            raise TypeMismatchInExpression(ast)
        return typ.eletype

    def visitAssign(self, ast, env):
        leftSymbol = ast.lhs.accept(self, env)
        leftType = leftSymbol.mtype if isinstance(leftSymbol, Symbol) else leftSymbol
        rightSymbol = ast.rhs.accept(self, env)
        rightType = rightSymbol.mtype if isinstance(rightSymbol, Symbol) else rightSymbol
        rightFuncType = rightType.restype if isinstance(rightType,MType) else rightType
        if rightSymbol == "cannot infer" or leftSymbol == "cannot infer":
            raise TypeCannotBeInferred(ast)
        if isinstance(leftType, VoidType) or isinstance(rightFuncType, VoidType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(leftType, type(rightFuncType)) and not isinstance(leftType, Unknown) and not isinstance(rightFuncType, Unknown):
            raise TypeMismatchInStatement(ast)
        if isinstance(leftType, Unknown) and isinstance(rightFuncType, Unknown):
            raise TypeCannotBeInferred(ast)
        elif isinstance(leftType, Unknown) and not isinstance(rightFuncType, Unknown):
            self.infer_type(leftSymbol, env, rightFuncType)
        elif isinstance(rightFuncType, Unknown) and not isinstance(leftType, Unknown):
            self.infer_type(rightSymbol, env, leftType)

    def visitIf(self, ast, env):
        local_env = [[]]
        for if_list in ast.ifthenStmt:
            expSymbol = if_list[0].accept(self,env)
            expType = expSymbol.mtype if isinstance(expSymbol, Symbol) else expSymbol
            expFuncType = expType.restype if isinstance(expType, MType) else expType
            if isinstance(expFuncType, (Unknown, BoolType)):
                self.infer_type(expSymbol, env, BoolType())
            else:
                raise TypeMismatchInStatement(ast)
            for decl in if_list[1]:
                local_env.append(decl.accept(self, local_env))
            for stmt in if_list[2]:
                stmt.accept(self, [env[0] + local_env[1:]] + [env[1]])

        for decl in ast.elseStmt[0]:
            local_env.append(decl.accept(self, local_env))

        for stmt in ast.elseStmt[1]:
            stmt.accept(self, [env[0] + local_env[1:]] + [env[1]])

    def visitFor(self, ast, env):
        idx1Symbol = ast.idx1.accept(self, env)
        if isinstance(idx1Symbol.mtype, (Unknown, IntType)):
            self.infer_type(idx1Symbol, env, IntType())
        else:
            raise TypeMismatchInStatement(ast)

        expr1Symbol = ast.expr1.accept(self, env)
        expr1Type = expr1Symbol.mtype if isinstance(expr1Symbol, Symbol) else expr1Symbol
        expr1FuncType = expr1Type.restype if isinstance(expr1Type, MType) else expr1Type
        if isinstance(expr1FuncType, (Unknown, IntType)):
            self.infer_type(expr1Symbol, env, IntType())
        else:
            raise TypeMismatchInStatement(ast)

        expr2Symbol = ast.expr2.accept(self, env)
        expr2Type = expr2Symbol.mtype if isinstance(expr2Symbol, Symbol) else expr2Symbol
        expr2FuncType = expr2Type.restype if isinstance(expr2Type, MType) else expr2Type
        if isinstance(expr2FuncType, (Unknown, BoolType)):
            self.infer_type(expr2Symbol, env, BoolType())
        else:
            raise TypeMismatchInStatement(ast)

        expr3Symbol = ast.expr3.accept(self, env)
        expr3Type = expr3Symbol.mtype if isinstance(expr3Symbol, Symbol) else expr3Symbol
        expr3FuncType = expr3Type.restype if isinstance(expr3Type, MType) else expr3Type
        if isinstance(expr3FuncType, (Unknown, IntType)):
            self.infer_type(expr3Symbol, env, IntType())
        else:
            raise TypeMismatchInStatement(ast)

        local_env = [[]]
        for decl in ast.loop[0]:
            local_env.append(decl.accept(self, local_env))

        for stmt in ast.loop[1]:
            stmt.accept(self, [env[0] + local_env[1:]] + [env[1]])

    def visitReturn(self, ast, env):
        returnSymbol = ast.expr.accept(self, env) if ast.expr is not None else VoidType()
        returnType = returnSymbol.mtype if isinstance(returnSymbol,Symbol) else returnSymbol
        returnFuncType = returnType.restype if isinstance(returnType, MType) else returnType

        if not ast.expr:
            if not isinstance(returnFuncType, VoidType):
                raise TypeMismatchInStatement(ast)
        elif isinstance(returnFuncType, VoidType):
            raise TypeMismatchInStatement(ast)
        elif isinstance(returnFuncType, Unknown):
            raise TypeCannotBeInferred(ast)
        return returnFuncType

    def visitDowhile(self, ast, env):
        expSymbol = ast.exp.accept(self, env)
        expType = expSymbol.mtype if isinstance(expSymbol, Symbol) else expSymbol
        expFuncType = expType.restype if isinstance(expType, MType) else expType
        # print(ast)
        # is_return = False
        local_env = [[]]
        for decl in ast.sl[0]:
            local_env.append(decl.accept(self, local_env))

        for stmt in ast.sl[1]:
            stmt.accept(self, [env[0] + local_env[1:]] + [env[1]])

        if isinstance(expFuncType, (Unknown, BoolType)):
            self.infer_type(expSymbol, env, BoolType())
        else:
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, env):
        expSymbol = ast.exp.accept(self, env)
        expType = expSymbol.mtype if isinstance(expSymbol, Symbol) else expSymbol
        expFuncType = expType.restype if isinstance(expType, MType) else expType
        if isinstance(expFuncType, (Unknown, BoolType)):
            self.infer_type(expSymbol, env, BoolType())
        else:
            raise TypeMismatchInStatement(ast)

        # is_return = False
        local_env = [[]]
        for decl in ast.sl[0]:
            local_env.append(decl.accept(self, local_env))
        # var_lst = reduce(lambda a, b: a + [Symbol(b.variable.name, b.varInit.accept(self, env) if b.varInit is not None else Unknown())],ast.sl[0])

        for stmt in ast.sl[1]:
            stmt.accept(self, [env[0] + local_env[1:]]+[env[1]])

    def visitContinue(self, ast, env):
        pass

    def visitBreak(self, ast, env):
        pass

    def visitCallStmt(self, ast, env):
        para_list = [x.accept(self, env) for x in ast.param]
        # check undeclared
        is_declared = self.lookup(ast.method.name, [env[0],env[1]])
        if is_declared is None or not isinstance(is_declared.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        # check same number of parameter
        elif len(is_declared.mtype.intype) != len(para_list) or not isinstance(is_declared.mtype.intype, list):
            raise TypeMismatchInStatement(ast)

        # check same type of each corresponding parameter
        else:
            for i in range(len(para_list)):
                if isinstance(para_list[i], Symbol):
                    if isinstance(para_list[i].mtype, Unknown):
                        if isinstance(is_declared.mtype.intype[i], Unknown):
                            raise TypeCannotBeInferred(ast)
                        else:
                            # self.infer_mtype(para_list[i], env, is_declared.mtype.intype[i])
                            para_list[i].mtype = is_declared.mtype.intype[i]
                    if isinstance(is_declared.mtype.intype[i], type(para_list[i].mtype)):
                        continue
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    if isinstance(para_list[i], Unknown):
                        if isinstance(is_declared.mtype.intype[i], Unknown):
                            raise TypeCannotBeInferred(ast)
                        else:
                            # self.infer_mtype(para_list[i], env, is_declared.mtype.intype[i])
                            para_list[i] = is_declared.mtype.intype[i]
                    if isinstance(is_declared.mtype.intype[i], type(para_list[i])):
                        continue
                    else:
                        raise TypeMismatchInStatement(ast)

        # return is_declared.mtype.restype if isinstance(is_declared.mtype, MType) else is_declared.mtype

    def visitIntLiteral(self, ast, env):
        return IntType()

    def visitFloatLiteral(self, ast, env):
        return FloatType()

    def visitBooleanLiteral(self, ast, env):
        return BoolType()

    def visitStringLiteral(self, ast, env):
        return StringType()

    def visitArrayLiteral(self, ast, env):
        ele_typ = ast.value[0].accept(self,env)
        dim = [len(ast.value)] + (ele_typ.dimen if isinstance(ele_typ,ArrayType) else [])
        if isinstance(ele_typ,ArrayType):
            ele_typ = ele_typ.eletype
        return ArrayType(dim, ele_typ)
