from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        if ctx.decls():
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
        else:
            return self.visit(ctx.decl())
    
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardec():
            return self.visit(ctx.vardec())
        else:
            return self.visit(ctx.funcdec())

    # Visit a parse tree produced by MT22Parser#vardec.
    def visitVardec(self, ctx:MT22Parser.VardecContext):
        if ctx.var_assign():
            # [("a", 3), ("b", 2), ("c", 1), type]
            ListTuple = self.visit(ctx.var_assign())
            Type = ListTuple.pop()
            idList, expList = [], []
            for tup in ListTuple:
                idList.append(tup[0])
                expList.append(tup[1])
            ReverseExp = zip(idList, expList[::-1])
            return [VarDecl(var[0], Type, var[1]) for var in ReverseExp]
        
        else:
            return self.visit(ctx.var_declare())

    # Visit a parse tree produced by MT22Parser#var_assign.
    def visitVar_assign(self, ctx:MT22Parser.Var_assignContext):
        if ctx.var_type():
            return [(ctx.ID().getText(),self.visit(ctx.expr()) ) , self.visit(ctx.var_type())]
        return [(ctx.ID().getText(), self.visit(ctx.expr()))] + self.visit(ctx.var_assign())


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        idList = self.visit(ctx.id_list())
        varType = self.visit(ctx.var_type())
        return [VarDecl(id, varType) for id in idList]


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        if ctx.id_list():
            return [ctx.ID().getText()] + self.visit(ctx.id_list())
        return [ctx.ID().getText()]


    # Visit a parse tree produced by MT22Parser#funcdec.
    def visitFuncdec(self, ctx:MT22Parser.FuncdecContext):
        name = ctx.ID(0).getText()
        return_type = self.visit(ctx.type_list())
        params = self.visit(ctx.param_list()) if ctx.param_list() else []
        inherit = ctx.ID(1).getText() if ctx.ID(1) else None
        body = self.visit(ctx.funcbody())
        return [FuncDecl(name, return_type, params, inherit, body)]


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visit(ctx.block_statement())


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.var_type())
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        return ParamDecl(str(name), typ ,out, inherit)



    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        if ctx.param_list():
            return [self.visit(ctx.param())] + self.visit(ctx.param_list())
        return [self.visit(ctx.param())]


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        if ctx.expr_list():
            expr_list = self.visit(ctx.expr_list())
            return FuncCall(ctx.ID().getText(),expr_list)
        else:
            return FuncCall(ctx.ID().getText(),[])


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        if(ctx.getChildCount() == 1):
            return [(ctx.INTLIT().getText())]
        else:
            return [(ctx.INTLIT().getText())] + self.visit(ctx.dimension())


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.atomic():
            return self.visit(ctx.atomic())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        if ctx.AUTO():
            return AutoType()
        else:
            pass


    # Visit a parse tree produced by MT22Parser#type_list.
    def visitType_list(self, ctx:MT22Parser.Type_listContext):
        if ctx.atomic():
            return self.visit(ctx.atomic())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        if ctx.AUTO():
            return AutoType()
        if ctx.VOID():
            return VoidType()       
        else:
            pass



    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        typ = self.visit(ctx.atomic())
        dim = self.visit(ctx.dimension())
        return ArrayType(dim, typ)


    # Visit a parse tree produced by MT22Parser#boolean.
    def visitBoolean(self, ctx:MT22Parser.BooleanContext):
        if ctx.TRUE():
            return BooleanLit(True)
        return BooleanLit(False)


    # Visit a parse tree produced by MT22Parser#atomic.
    def visitAtomic(self, ctx:MT22Parser.AtomicContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BooleanType()
        else:
            pass


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        if ctx.expr_list():
            expr_list = self.visit(ctx.expr_list())
            return ArrayLit(expr_list)
        else:
            return ArrayLit([])
    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))



    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        
        return self.visit(ctx.getChild(0))



    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.indexOp():
            return self.visit(ctx.indexOp())
        
        return self.visit(ctx.getChild(0)) 


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.OPENCC():
            return self.visit(ctx.expr())
        else:
            if ctx.INTLIT():
                return IntegerLit(int(ctx.INTLIT().getText()))
            if ctx.FLOATLIT():
                if(ctx.FLOATLIT().getText().startswith('.')):
                    newfloat = '0' + ctx.FLOATLIT().getText()
                    return FloatLit(float(newfloat))
                else:
                    return FloatLit(float(ctx.FLOATLIT().getText()))
            if ctx.STRINGLIT():
                return StringLit(str(ctx.STRINGLIT().getText()))
            if ctx.boolean():
                return self.visit(ctx.boolean())
            if ctx.funccall():
                return self.visit(ctx.funccall())
            if ctx.ID():
                return Id(ctx.ID().getText())
            if ctx.arraylit():
                return self.visit(ctx.arraylit())



    # Visit a parse tree produced by MT22Parser#indexOp.
    def visitIndexOp(self, ctx:MT22Parser.IndexOpContext):
        name = ctx.ID().getText()
        cell = self.visit(ctx.expr_list())
        return ArrayCell(name, cell)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        if ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.for_statement():
            return self.visit(ctx.for_statement())
        if ctx.break_statement():
            return self.visit(ctx.break_statement())
        if ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        if ctx.while_statement():
            return self.visit(ctx.while_statement())
        if ctx.dowhile_statement():
            return self.visit(ctx.dowhile_statement())
        if ctx.return_statement():
            return self.visit(ctx.return_statement())
        if ctx.block_statement():
            return self.visit(ctx.block_statement())
        if ctx.call_statement():
            return self.visit(ctx.call_statement())
        else:
            return None

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.indexOp():
            return self.visit(ctx.indexOp())
        else:
            return Id(ctx.ID().getText())        


    # Visit a parse tree produced by MT22Parser#assign_statement.
    def visitAssign_statement(self, ctx:MT22Parser.Assign_statementContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        expr = self.visit(ctx.expr())
        tstmt = self.visit(ctx.statement(0))
        if ctx.ELSE():
            fstmt = self.visit(ctx.statement(1))
            return IfStmt(expr, tstmt, fstmt)
        else:
            return IfStmt(expr, tstmt)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr(0))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.statement())
        return ForStmt(AssignStmt(lhs, rhs), cond, upd, stmt)

    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        cond = self.visit(ctx.while_con())
        stmt = self.visit(ctx.statement())
        return WhileStmt(cond, stmt)

    # Visit a parse tree produced by MT22Parser#dowhile_statement.
    def visitDowhile_statement(self, ctx:MT22Parser.Dowhile_statementContext):
        cond = self.visit(ctx.while_con())
        stmt = self.visit(ctx.block_statement())
        return DoWhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#while_con.
    def visitWhile_con(self, ctx:MT22Parser.While_conContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        if ctx.getChildCount() > 2:
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt()


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        if ctx.expr_list():
            expr_list = self.visit(ctx.expr_list())
            return CallStmt(ctx.ID().getText(),expr_list)
        else:
            return CallStmt(ctx.ID().getText(),[])


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        body = []
        for item in range(1, ctx.getChildCount() - 1):
            temp = ctx.getChild(item)
            if type(temp) is MT22Parser.StatementContext:
                body += [self.visit(temp)]
            else:
                body += self.visit(temp)
        return BlockStmt(body)



    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return [self.visit(expressions) for expressions in ctx.expr()]