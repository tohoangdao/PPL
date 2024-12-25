from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *
from functools import reduce

class ASTGeneration(CSlangVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_dec()])


    # Visit a parse tree produced by CSlangParser#class_dec.
    def visitClass_dec(self, ctx:CSlangParser.Class_decContext):
        if ctx.super_part():
            return ClassDecl(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.member()], self.visit(ctx.super_part())) 
        
        return ClassDecl(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.member()])

    # Visit a parse tree produced by CSlangParser#super_part.
    def visitSuper_part(self, ctx:CSlangParser.Super_partContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        if ctx.attribute():
            return self.visit(ctx.attribute())
        
        return self.visit(ctx.method())


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
        if ctx.var_dec():
            return AttributeDecl(self.visit(ctx.var_dec())) 
        
        return AttributeDecl(self.visit(ctx.const_dec()))

    def visitConst_dec(self, ctx:CSlangParser.Const_decContext):
        idd = self.visit(ctx.id_list())
        typee = self.visit(ctx.at_type())
        expr = self.visit(ctx.expressions_list()) 
        return map(lambda x,y:ConstDecl(x,typee,y),idd,expr)
    

    # Visit a parse tree produced by CSlangParser#var_dec.
    def visitVar_dec(self, ctx:CSlangParser.Var_decContext):
        idd = self.visit(ctx.id_list())
        typee = self.visit(ctx.at_type())
        expr = self.visit(ctx.expressions_list()) if ctx.expressions_list() else [] 
        #return list(map(lambda x,y:VarDecl(x,typee,y),idd,expr))
        return VarDecl(idd, typee, expr) 

    # Visit a parse tree produced by CSlangParser#id_list.
    def visitId_list(self, ctx:CSlangParser.Id_listContext):
        return [self.visit(x) for x in ctx.iden()]

    # Visit a parse tree produced by CSlangParser#expressions_list.
    def visitExpressions_list(self, ctx:CSlangParser.Expressions_listContext):
        return [self.visit(expressions) for expressions in ctx.expressions()]


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        if ctx.method_dec():
            return self.visit(ctx.method_dec())
        
        return self.visit(ctx.method_con())


    # Visit a parse tree produced by CSlangParser#method_dec.
    def visitMethod_dec(self, ctx:CSlangParser.Method_decContext):
        name = self.visit(ctx.iden())
        params = self.visit(ctx.parameter_list()) if ctx.parameter_list() else [] 
        returnType = self.visit(ctx.func_type())
        body= self.visit(ctx.block_statement())
        return MethodDecl(name,params,returnType,body)
        
    # Visit a parse tree produced by CSlangParser#parameter_list.
    def visitParameter_list(self, ctx:CSlangParser.Parameter_listContext):
        return list(map(lambda x: x.accept(self), ctx.parameter()))

    # Visit a parse tree produced by CSlangParser#parameter.
    def visitParameter(self, ctx:CSlangParser.ParameterContext):
        list_var = []
        varType = self.visit(ctx.at_type())
        ids = self.visit(ctx.id_list())
        for i in ids:
            list_var = list_var + [VarDecl(i,varType)]
        return list_var


    # Visit a parse tree produced by CSlangParser#method_con.
    def visitMethod_con(self, ctx:CSlangParser.Method_conContext):
        name = Id(str(ctx.CONSTRUCTOR().getText()))
        params = self.visit(ctx.parameter_list()) if ctx.parameter_list() else [] 
        returnType = VoidType()
        body= self.visit(ctx.block_statement())
        return MethodDecl(name,params,returnType,body)


    # Visit a parse tree produced by CSlangParser#at_type.
    def visitAt_type(self, ctx:CSlangParser.At_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOL():
            return BoolType()
        if ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            pass

    # Visit a parse tree produced by CSlangParser#func_type.
    def visitFunc_type(self, ctx:CSlangParser.Func_typeContext):
        if ctx.at_type():
            return self.visit(ctx.at_type())
        if ctx.VOID():
            return VoidType()
        else:
            pass

    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        size = int(ctx.INTLIT().getText())
        if ctx.INT():
            arrayType = IntType()
        if ctx.FLOAT():
            arrayType = FloatType()
        if ctx.STRING():
            arrayType = StringType()
        if ctx.BOOL():
            arrayType = BoolType()
        return ArrayType(size,arrayType)


    # Visit a parse tree produced by CSlangParser#expressions.
    def visitExpressions(self, ctx:CSlangParser.ExpressionsContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))



    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        if ctx.getChildCount()==4:
            return ArrayCell(self.visit(ctx.expr7()),self.visit(ctx.expressions()))
        
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.expr7()),Id(ctx.ID().getText()))
        
        else:
            param=self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return CallExpr(self.visit(ctx.expr7()),Id(ctx.ID().getText()),param)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        if ctx.expr9():
            return self.visit(ctx.expr9())
        
        else:
            obj=self.visit(ctx.expr9()) if ctx.DOT() else None
            method=Id(ctx.At().getText())
            if ctx.OPENCC():
                param=self.visit(ctx.expr_list()) if ctx.expr_list() else []
                return CallExpr(obj,method,param)
            else:
                return FieldAccess(obj,method)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        if ctx.NEW():
            param=self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return NewExpr(Id(ctx.ID().getText()),param)
        else:
            return self.visit(ctx.expr10())


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        if ctx.OPENCC():
            return self.visit(ctx.expressions())
        else:
            if ctx.INTLIT():
                return IntLiteral(int(ctx.INTLIT().getText()))
            if ctx.FLOATLIT():
                return FloatLiteral(float(ctx.FLOATLIT().getText()))
            if ctx.STRINGLIT():
                return StringLiteral(str(ctx.STRLIT().getText()))
            if ctx.boollit():
                return self.visit(ctx.boollit())
            if ctx.SELF():
                return SelfLiteral()
            if ctx.iden():
                return self.visit(ctx.iden())
            if ctx.arraylit():
                return self.visit(ctx.arraylit())


    # Visit a parse tree produced by CSlangParser#expr_list.
    def visitExpr_list(self, ctx:CSlangParser.Expr_listContext):
        return [self.visit(expressions) for expressions in ctx.expressions()]


    # Visit a parse tree produced by CSlangParser#statement.
    def visitStatement(self, ctx:CSlangParser.StatementContext):
        if ctx.vardec_statement():
            return self.visit(ctx.vardec_statement())
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
        if ctx.method_statement():
            return self.visit(ctx.method_statement())
        if ctx.return_statemen():
            return self.visit(ctx.return_statemen())
        if ctx.block_statemen():
            return self.visit(ctx.block_statemen())


    # Visit a parse tree produced by CSlangParser#vardec_statement.
    def visitVardec_statement(self, ctx:CSlangParser.Vardec_statementContext):
        return self.visit(ctx.attribute)


    # Visit a parse tree produced by CSlangParser#assign_statement.
    def visitAssign_statement(self, ctx:CSlangParser.Assign_statementContext):
        return Assign(self.visit(ctx.expressions(0)),self.visit(ctx.expressions(1)))


    # Visit a parse tree produced by CSlangParser#if_statement.
    def visitIf_statement(self, ctx:CSlangParser.If_statementContext):
        expr = self.visit(ctx.expressions())
        thenStmt = self.visit(ctx.block_statement(0))
        preStmt = self.visit(ctx.pre_statement()) if ctx.pre_statement() else None # None if there is no pre-statement
        elseStmt = self.visit(ctx.block_statement(1)) if ctx.ELSE() else None
        return If(expr,thenStmt,preStmt,elseStmt)


    def visitPre_statement(self, ctx:CSlangParser.Pre_statementContext):
        return self.visit(ctx.block_statement())
    # Visit a parse tree produced by CSlangParser#for_statement.
    def visitFor_statement(self, ctx:CSlangParser.For_statementContext):
        return For(self.visit(ctx.for_condition(0)), self.visit(ctx.expressions()), self.visit(ctx.for_condition(1)), self.visit(ctx.block_statement()))


    # Visit a parse tree produced by CSlangParser#for_condition.
    def visitFor_condition(self, ctx:CSlangParser.For_conditionContext):
        return Assign(self.visit(ctx.expressions(0)),self.visit(ctx.expressions(1)))


    # Visit a parse tree produced by CSlangParser#break_statement.
    def visitBreak_statement(self, ctx:CSlangParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by CSlangParser#continue_statement.
    def visitContinue_statement(self, ctx:CSlangParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by CSlangParser#method_statement.
    def visitMethod_statement(self, ctx:CSlangParser.Method_statementContext):
        return self.visit(ctx.expr8())


    # Visit a parse tree produced by CSlangParser#return_statement.
    def visitReturn_statement(self, ctx:CSlangParser.Return_statementContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)


    # Visit a parse tree produced by CSlangParser#block_statement.
    def visitBlock_statement(self, ctx:CSlangParser.Block_statementContext):
        return [Block(self.visit(x) for x in ctx.statement())]


    # Visit a parse tree produced by CSlangParser#arraylit.
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.litlist()))


    # Visit a parse tree produced by CSlangParser#litlist.
    def visitLitlist(self, ctx:CSlangParser.LitlistContext):
        return [self.visit(x) for x in ctx.literal()]


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        if ctx.boollit():
            return self.visit(ctx.boollit())

    # Visit a parse tree produced by CSlangParser#iden.
    def visitIden(self, ctx:CSlangParser.IdenContext):
        if ctx.ID():           
            return Id(ctx.ID().getText())
        return Id(f'{ctx.At().getText()}')


    # Visit a parse tree produced by CSlangParser#boollit.
    def visitBoollit(self, ctx:CSlangParser.BoollitContext):
        if ctx.getText() == "true":
            return BooleanLiteral(True)
        return BooleanLiteral(False)

