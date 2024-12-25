from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *
from functools import reduce

class ASTGeneration(CSlangVisitor):

    # Visit a parse tree produced by CSlangParser#program.

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_dec.
    def visitClass_dec(self, ctx:CSlangParser.Class_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#super_part.
    def visitSuper_part(self, ctx:CSlangParser.Super_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#const_dec.
    def visitConst_dec(self, ctx:CSlangParser.Const_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#var_dec.
    def visitVar_dec(self, ctx:CSlangParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_list.
    def visitId_list(self, ctx:CSlangParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expressions_list.
    def visitExpressions_list(self, ctx:CSlangParser.Expressions_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_dec.
    def visitMethod_dec(self, ctx:CSlangParser.Method_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameter_list.
    def visitParameter_list(self, ctx:CSlangParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameter.
    def visitParameter(self, ctx:CSlangParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_con.
    def visitMethod_con(self, ctx:CSlangParser.Method_conContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#at_type.
    def visitAt_type(self, ctx:CSlangParser.At_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#func_type.
    def visitFunc_type(self, ctx:CSlangParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expressions.
    def visitExpressions(self, ctx:CSlangParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_list.
    def visitExpr_list(self, ctx:CSlangParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statement.
    def visitStatement(self, ctx:CSlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#vardec_statement.
    def visitVardec_statement(self, ctx:CSlangParser.Vardec_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_statement.
    def visitAssign_statement(self, ctx:CSlangParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_statement.
    def visitIf_statement(self, ctx:CSlangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#pre_statement.
    def visitPre_statement(self, ctx:CSlangParser.Pre_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_statement.
    def visitFor_statement(self, ctx:CSlangParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_condition.
    def visitFor_condition(self, ctx:CSlangParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_statement.
    def visitBreak_statement(self, ctx:CSlangParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_statement.
    def visitContinue_statement(self, ctx:CSlangParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_statement.
    def visitMethod_statement(self, ctx:CSlangParser.Method_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_statement.
    def visitReturn_statement(self, ctx:CSlangParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_statement.
    def visitBlock_statement(self, ctx:CSlangParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraylit.
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#litlist.
    def visitLitlist(self, ctx:CSlangParser.LitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#iden.
    def visitIden(self, ctx:CSlangParser.IdenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#boollit.
    def visitBoollit(self, ctx:CSlangParser.BoollitContext):
        return self.visitChildren(ctx)