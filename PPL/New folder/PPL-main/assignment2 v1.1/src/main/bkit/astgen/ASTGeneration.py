from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):

    # program : vardecls? funcdecls EOF ;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        if ctx.vardecls():
            return Program(ctx.vardecls().accept(self) + ctx.funcdecls().accept(self))
        else:
            return Program(ctx.funcdecls().accept(self))

    # vardecls: vardecl+ ;
    def visitVardecls(self, ctx: BKITParser.VardeclsContext):
        return reduce(lambda x, y: x + y.accept(self), ctx.vardecl(), [])

    # vardecl: VAR COLON varlist SEMI;
    def visitVardecl(self, ctx: BKITParser.VardeclContext):
        return ctx.varlist().accept(self)

    # varlist: var (COMMA var)* ;
    def visitVarlist(self, ctx: BKITParser.VarlistContext):
        return list(map(lambda x: x.accept(self), ctx.var()))

    # var: var_array | var_scalar ;
    def visitVar(self, ctx: BKITParser.VarContext):
        if ctx.var_array():
            return ctx.var_array().accept(self)
        else:
            return ctx.var_scalar().accept(self)

    # var_array: ID index_op+ (ASSIGN literal)?;
    def visitVar_array(self, ctx: BKITParser.Var_arrayContext):
        if ctx.literal():
            return VarDecl(Id(ctx.ID().getText()), [x.accept(self) for x in ctx.index_op()], ctx.literal().accept(self))
        else:
            return VarDecl(Id(ctx.ID().getText()), [x.accept(self) for x in ctx.index_op()], None)

    # var_scalar: ID (ASSIGN literal)?;
    def visitVar_scalar(self, ctx: BKITParser.Var_scalarContext):
        if ctx.literal():
            return VarDecl(Id(ctx.ID().getText()), [], ctx.literal().accept(self))
        else:
            return VarDecl(Id(ctx.ID().getText()), [], None)

    # index_op: (LS expression RS) ;
    def visitIndex_op(self, ctx: BKITParser.Index_opContext):
        return ctx.expression().accept(self)

    # arraylit : LC litlist RC ;
    def visitArraylit(self, ctx: BKITParser.ArraylitContext):
        return ArrayLiteral(ctx.litlist().accept(self))

    # litlist : literal (COMMA literal)* ;
    def visitLitlist(self, ctx: BKITParser.LitlistContext):
        return list(map(lambda x: x.accept(self), ctx.literal()))

    # literal : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit ;
    def visitLiteral(self,ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                return IntLiteral(int(ctx.INTLIT().getText(), 16))
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                return IntLiteral(int(ctx.INTLIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral('True' == ctx.BOOLLIT().getText())
        elif ctx.arraylit():
            return ctx.arraylit().accept(self)
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))

    # funcdecls: funcdecl* ;
    def visitFuncdecls(self, ctx: BKITParser.FuncdeclsContext):
        if ctx.funcdecl():
            return [x.accept(self) for x in ctx.funcdecl()]
        else:
            return []

    # funcdecl: FUNCTION COLON ID (PARAMETER COLON paralist)? body ;
    def visitFuncdecl(self, ctx: BKITParser.FuncdeclContext):
        if ctx.paralist():
            return FuncDecl(Id(ctx.ID().getText()), ctx.paralist().accept(self), ctx.body().accept(self))
        else:
            return FuncDecl(Id(ctx.ID().getText()), [], ctx.body().accept(self))

    # paralist: var (COMMA var)* ;
    def visitParalist(self, ctx: BKITParser.ParalistContext):
        return list(map(lambda x: x.accept(self), ctx.var()))

    # body: BODY COLON nullstmt ENDBODY DOT ;
    def visitBody(self, ctx: BKITParser.BodyContext):
        return ctx.nullstmt().accept(self)

    # nullstmt: vardeclstmt* otherstmt* ;
    def visitNullstmt(self, ctx: BKITParser.NullstmtContext):
        if ctx.vardeclstmt() and ctx.otherstmt():
            lst = reduce(lambda x, y: x + y, [x.accept(self) for x in ctx.vardeclstmt()])
            return (lst, [y.accept(self) for y in ctx.otherstmt()])
        elif ctx.vardeclstmt():
            lst = reduce(lambda x, y: x + y, [x.accept(self) for x in ctx.vardeclstmt()])
            return (lst, [])
        elif ctx.otherstmt():
            return ([], [x.accept(self) for x in ctx.otherstmt()])
        else:
            return ([],[])

    # stmtlst: vardeclstmt+ otherstmt* | vardeclstmt* otherstmt+ ;
    def visitStmtlst(self, ctx: BKITParser.StmtlstContext):
        if ctx.vardeclstmt() and ctx.otherstmt():
            return [reduce(lambda x, y: x + y, [x.accept(self) for x in ctx.vardeclstmt()]), list(map(lambda x: x.accept(self), ctx.otherstmt()))]
        elif ctx.vardeclstmt():
            return [reduce(lambda x, y: x + y, [x.accept(self) for x in ctx.vardeclstmt()]), []]
        elif ctx.otherstmt():
            return [[], list(map(lambda x: x.accept(self), ctx.otherstmt()))]

    # vardeclstmt: vardecl;
    def visitVardeclstmt(self, ctx: BKITParser.VardeclstmtContext):
        return ctx.vardecl().accept(self)

    # otherstmt: assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | callstmt | returnstmt;
    def visitOtherstmt(self, ctx: BKITParser.OtherstmtContext):
        return self.visitChildren(ctx)

    # assignstmt: assignvar ASSIGN expression SEMI ;
    def visitAssignstmt(self, ctx: BKITParser.AssignstmtContext):
        return Assign(ctx.assignvar().accept(self), ctx.expression().accept(self))

    # assignvar: ID index_op* ;
    def visitAssignvar(self, ctx: BKITParser.AssignvarContext):
        if ctx.index_op():
            return ArrayCell(Id(ctx.ID().getText()), [x.accept(self) for x in ctx.index_op()])
        else:
            return Id(ctx.ID().getText())

    # ifstmt: ifthenstmt elsestmt ENDIF DOT ;
    def visitIfstmt(self, ctx: BKITParser.IfstmtContext):
        return If(ctx.ifthenStmt().accept(self), ctx.elseStmt().accept(self))

    # ifthenstmt: IF expression THEN stmtlst (ELSEIF expression THEN stmtlst)* ;
    def visitIfthenStmt(self, ctx: BKITParser.IfthenStmtContext):
        return list(map(lambda x, y: (x.accept(self), y.accept(self)[0], y.accept(self)[1]), ctx.expression(), ctx.stmtlst()))

    # elsestmt: (ELSE stmtlst)? ENDIF DOT ;
    def visitElseStmt(self, ctx: BKITParser.ElseStmtContext):
        if ctx.ELSE():
            return (ctx.stmtlst().accept(self)[0],ctx.stmtlst().accept(self)[1])
        else:
            return ([],[])

    # forstmt: FOR LR ID ASSIGN expression COMMA expression COMMA expression RR DO stmtlst ENDFOR DOT ;;
    def visitForstmt(self, ctx: BKITParser.ForstmtContext):
        return For(Id(ctx.ID().getText()), ctx.expression(0).accept(self), ctx.expression(1).accept(self), ctx.expression(2).accept(self), (ctx.stmtlst().accept(self)[0],ctx.stmtlst().accept(self)[1]))

    # whilestmt: WHILE expression DO stmtlst ENDWHILE DOT;
    def visitWhilestmt(self, ctx: BKITParser.WhilestmtContext):
        return While(ctx.expression().accept(self), (ctx.stmtlst().accept(self)[0],ctx.stmtlst().accept(self)[1]))

    # dowhilestmt: DO stmt WHILE expression ENDDO DOT ;
    def visitDowhilestmt(self, ctx: BKITParser.DowhilestmtContext):
        return Dowhile((ctx.stmtlst().accept(self)[0],ctx.stmtlst().accept(self)[1]), ctx.expression().accept(self))

    # breakstmt: BREAK SEMI ;
    def visitBreakstmt(self, ctx: BKITParser.BreakstmtContext):
        return Break()

    # continuestmt: CONTINUE SEMI ;
    def visitContinuestmt(self, ctx: BKITParser.ContinuestmtContext):
        return Continue()

    # returnstmt: RETURN expression? SEMI ;
    def visitReturnstmt(self, ctx: BKITParser.ReturnstmtContext):
        if ctx.expression():
            return Return(ctx.expression().accept(self))
        else:
            return Return(None)

    # callstmt: ID LR exprlist RR SEMI ;
    def visitCallstmt(self, ctx: BKITParser.CallstmtContext):
        return CallStmt(Id(ctx.ID().getText()), ctx.exprlist().accept(self))

    # exprlist: expression (COMMA expression)* ;
    def visitExprlist(self, ctx: BKITParser.ExprlistContext):
        return list(map(lambda x: x.accept(self), ctx.expression()))

    # expression: expr1 (EQUAL|NOT_EQUAL|FLOAT_NOT_EQUAL|LESS|LESS_EQUAL|GREATER|GREATER_EQUAL|FLOAT_LESS|FLOAT_LESS_EQUAL|FLOAT_GREATER|FLOAT_GREATER_EQUAL) expr1 | expr1;
    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return ctx.expr1(0).accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))

    # expr1: expr1 (AND|OR) expr1 | expr2;
    def visitExpr1(self, ctx: BKITParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return ctx.expr2().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))

    # expr2: expr2 (ADD|FLOAT_ADD|SUB|FLOAT_SUB) expr3 | expr3 ;
    def visitExpr2(self, ctx: BKITParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(), ctx.expr2().accept(self), ctx.expr3().accept(self))

    # expr3: expr3 (MULTIPLY|FLOAT_MULTIPLY|DIVIDE|FLOAT_DIVIDE|REMAINDER|FLOAT_REMAINDER) expr4 | expr4 ;
    def visitExpr3(self, ctx: BKITParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(), ctx.expr3().accept(self), ctx.expr4().accept(self))

    # expr4: NOT expr4 | expr5;
    def visitExpr4(self, ctx: BKITParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        elif ctx.getChild(0) == ctx.NOT():
            op = ctx.NOT().getText()
        return UnaryOp(op, ctx.expr4().accept(self))

    # expr5: (SUB|FLOAT_SUB) expr5 | expr6;
    def visitExpr5(self, ctx: BKITParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return UnaryOp(ctx.getChild(0).getText(), ctx.expr5().accept(self))

    # expr6: funccall | literal | LR expression RR | assignvar;
    def visitExpr6(self, ctx: BKITParser.Expr6Context):
        if ctx.funccall():
            return ctx.funccall().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.expression():
            return ctx.expression().accept(self)
        elif ctx.assignvar():
            return ctx.assignvar().accept(self)

    # element_expr: (ID|funccall) index_op+ ;
    def visitElement_expr(self, ctx: BKITParser.Element_exprContext):
        if ctx.ID():
            return Id(ctx.ID().getText()) + [x.accept(self) for x in ctx.index_op()]
        elif ctx.funccall():
            return ctx.funccall().accept(self) + [x.accept(self) for x in ctx.index_op()]

    # funccall: ID LR exprlist? RR ;
    def visitFunccall(self, ctx: BKITParser.FunccallContext):
        if ctx.exprlist():
            return CallExpr(Id(ctx.ID().getText()), ctx.exprlist().accept(self))
        else:
            return CallExpr(Id(ctx.ID().getText()), [])
