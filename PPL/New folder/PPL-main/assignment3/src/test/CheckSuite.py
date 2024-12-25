import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_only_vardecl(self):
        input = Program([VarDecl(Id("alo"),[],None)])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_func_with_no_main(self):
        input = Program([FuncDecl(Id("foo"),[],([],[]))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare_func_main(self):
        input = Program(
        [FuncDecl(Id("main"),[],([],[])),FuncDecl(Id("main"),[],([],[]))])
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclare_func_not_main(self):
        input = Program(
        [FuncDecl(Id("foo"),[],([],[])),FuncDecl(Id("foo"),[],([],[])),FuncDecl(Id("main"),[],([],[]))])
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_func_not_main_again(self):
        input = Program(
        [FuncDecl(Id("foo"),[],([],[])),FuncDecl(Id("main"),[],([],[])),FuncDecl(Id("foo"),[],([],[]))])
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_vardecl_outside_main(self):
        input = Program(
        [VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_vardecl_outside_main_with_init(self):
        input = Program(
        [VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],BooleanLiteral(True)),
         VarDecl(Id("x"),[],FloatLiteral(15.2)),FuncDecl(Id("main"),[],([],[]))])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl_inside_main(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None)],[]))])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl_inside_main_with_init(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],BooleanLiteral(True)),
     VarDecl(Id("x"),[],FloatLiteral(15.2))],[]))])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_vardecl_funcdecl_same_name(self):
        input = Program(
        [VarDecl(Id("foo"),[],None),FuncDecl(Id("main"),[],([],[])),FuncDecl(Id("foo"),[],([],[]))])
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_vardecl_name_main(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("main"),[],None),FuncDecl(Id("main"),[],([],[]))])
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_paradecl_in_func(self):
        input = Program(
        [FuncDecl(Id("main"),[VarDecl(Id("p"),[],None),VarDecl(Id("p"),[],None)],([],[]))])
        expect = str(Redeclared(Parameter(),"p"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_paradecl_in_func_with_init(self):
        input = Program([FuncDecl(Id("main"),
                                                                         [VarDecl(Id("p"),[],IntLiteral(20)),
                                                                          VarDecl(Id("p"),[],FloatLiteral(2.2))],
                                                                         ([],[]))])
        expect = str(Redeclared(Parameter(),"p"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_paradecl_vardecl(self):
        input = Program(
        [FuncDecl(Id("main"),[VarDecl(Id("p"),[],None)],([VarDecl(Id("p"),[],None)],[]))])
        expect = str(Redeclared(Variable(),"p"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_vardecl_main_only(self):
        input = Program([VarDecl(Id("main"),[],None)])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_assign_undecl_with(self):
        input = Program(
        [FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(2))]))])
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_assign_undecl_with_vardeclared(self):
        input = Program(
        [VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[Assign(Id("x"),Id("y"))]))])
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_assign_undecl_with_vardeclared_in_func(self):
        input = Program(
        [FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),Id("y"))]))])
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_assign_undecl_with_paradecl(self):
        input = Program(
        [FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),Id("y"))]))])
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_expr_undecl(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],(
    [],[Assign(Id("x"),BinaryOp("+",IntLiteral(2),Id("abc")))]))])
        expect = str(Undeclared(Identifier(),"abc"))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_assign_literal_diff_type(self):
        input = Program(
        [FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(22.11))],[Assign(Id("x"),IntLiteral(2))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_assign_var_diff_type(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],FloatLiteral(22.11)),VarDecl(Id("y"),[],BooleanLiteral(True))],
    [Assign(Id("x"),Id("y"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_assign_var_diff_type_local_global(self):
        input = Program([VarDecl(Id("x"),[],FloatLiteral(22.11)),
                                                                       FuncDecl(Id("main"),[],(
                                                                       [VarDecl(Id("y"),[],BooleanLiteral(True))],
                                                                       [Assign(Id("x"),Id("y"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_assign_both_side_none(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),Id("y"))]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_infer_by_assign(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],BooleanLiteral(False))],[Assign(Id("x"),FloatLiteral(2.345)),Assign(Id("x"),Id("y"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_infer_by_binaryop(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[
        Assign(Id("x"),Id("y")),Assign(Id("y"),BooleanLiteral(False))]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_assign_two_diff_type(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],(
    [],[Assign(Id("x"),BinaryOp("+",IntLiteral(3),BooleanLiteral(True)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(3),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_infer_then_binop(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],IntLiteral(2)),
                                                                            VarDecl(Id("y"),[],None)],([],[
        Assign(Id("x"),BinaryOp("+.",Id("y"),FloatLiteral(2.5)))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BinaryOp("+.",Id("y"),FloatLiteral(2.5)))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_mismatch_in_more_complex_expr_2(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp(">",BinaryOp("%",Id("x"),Id("y")),BinaryOp("+",Id("z"),IntLiteral(3)))),Assign(Id("z"),Id("x"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("z"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_mismatch_expression_simple_literal(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",FloatLiteral(2.5),IntLiteral(2)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("+",FloatLiteral(2.5),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_mismatch_in_more_complex_expr(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],
    [Assign(Id("x"),BinaryOp(">",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("+",Id("z"),IntLiteral(3))))]))])
        expect = str(TypeMismatchInExpression(
        BinaryOp(">",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("+",Id("z"),IntLiteral(3)))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_mismatch_expr_unary(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],FloatLiteral(10.5))],[Assign(Id("x"),UnaryOp("-.",IntLiteral(5)))]))])
        expect = str(TypeMismatchInExpression(UnaryOp("-.",IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_mismatch_stmt_unary(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(3))],
    [Assign(Id("x"),UnaryOp("-.",FloatLiteral(0.5))),
     Assign(Id("y"),BinaryOp("*.",Id("x"),FloatLiteral(22.11)))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("y"),BinaryOp("*.",Id("x"),FloatLiteral(22.11)))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_in_complex_expr(self):
        input = Program([FuncDecl(Id("main"),[],(
    [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],
    [Assign(Id("x"),BinaryOp("||",BooleanLiteral(True),BinaryOp(">",Id("t"),Id("z"))))]))])
        expect = str(Undeclared(Identifier(),"t"))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_undeclared_function_use_ast(self):
        input = Program(
        [FuncDecl(Id("main"),[],([],[CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_diff_length_para(self):
        input = Program([FuncDecl(Id("flag"),[VarDecl(Id("x"),[],None)],([],[])),
                                                      FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[])))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_diff_length_para_2(self):
        input = Program([FuncDecl(Id("flag"),[VarDecl(Id("x"),[],None)],([],[])),FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)])))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_callstmt_2_corresponding_para_unknown(self):
        input = Program(
        [FuncDecl(Id("flag"),[VarDecl(Id("x"),[],None)],([],[])),
         FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[VarDecl(Id("x"),[],None)])]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id("flag"),[VarDecl(Id("x"),[],None)])))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_callstmt_2_corresponding_para_infer(self):
        input = Program(
        [FuncDecl(Id("flag"),[VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],IntLiteral(3))],([],[])),
         FuncDecl(Id("main"),[],([VarDecl(Id("abc"),[],None),VarDecl(Id("xyz"),[],FloatLiteral(3.5))],
                                   [CallStmt(Id("flag"),[Id("abc"),Id("xyz")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[Id("abc"),Id("xyz")])))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_callstmt_2_corresponding_para_infer_literal(self):
        input = Program(
        [FuncDecl(Id("flag"),[VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],IntLiteral(3))],([],[])),
         FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[IntLiteral(2),StringLiteral("True")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[IntLiteral(2),StringLiteral("True")])))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_callsmt_undeclared_argument(self):
        input = Program(
        [FuncDecl(Id("flag"),[VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],IntLiteral(3))],([],[])),
         FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[Id("abc"),IntLiteral(3)])]))])
        expect = str(Undeclared(Identifier(),"abc"))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_callsmt_expr_argument(self):
        input = Program([FuncDecl(Id("flag"),[VarDecl(Id("x"),[],FloatLiteral(3.5)),VarDecl(Id("y"),[],IntLiteral(3))],([],[])),FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[BinaryOp("+",IntLiteral(15),IntLiteral(10)),IntLiteral(13)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[BinaryOp("+",IntLiteral(15),IntLiteral(10)),IntLiteral(13)])))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_infer_in_callstmt_then_assign(self):
        input = Program([FuncDecl(Id("flag"),[VarDecl(Id("x"),[],IntLiteral(10))],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[CallStmt(Id("flag"),[Id("x")]),Assign(Id("x"),BooleanLiteral(True))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_infer_in_complex_callstmt_then_assign(self):
        input = Program([FuncDecl(Id("flag"),[VarDecl(Id("x"),[],IntLiteral(10))],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[CallStmt(Id("flag"),[Id("y")]),Assign(Id("x"),BinaryOp("*.",Id("x"),UnaryOp("-",Id("y"))))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("*.",Id("x"),UnaryOp("-",Id("y")))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_many_stmt_dowhile(self):
        input = Program([FuncDecl(Id("alo"),[],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("alo"),[],IntLiteral(0))],[Assign(Id("alo"),BinaryOp("+",Id("alo"),CallStmt(Id("alo"),[])))]))])
        expect = str(Undeclared(Function(),"alo"))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_shadow_in_callstmt(self):
        input = Program([FuncDecl(Id("alo"),[],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("alo"),[],IntLiteral(0))],[CallStmt(Id("alo"),[])]))])
        expect = str(Undeclared(Function(),"alo"))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_undeclared_in_while(self):
        input = Program([FuncDecl(Id("main"),[],([],[While(BooleanLiteral(True),([],[Assign(Id("i"),IntLiteral(2))]))]))])
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_not_bool_in_while_cond(self):
        input = Program([FuncDecl(Id("main"),[],([],[While(StringLiteral("alo"),([VarDecl(Id("i"),[],None)],[Assign(Id("i"),IntLiteral(2))]))]))])
        expect = str(TypeMismatchInStatement(While(StringLiteral("alo"),([VarDecl(Id("i"),[],None)],[Assign(Id("i"),IntLiteral(2))]))))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_diff_infer_in_while(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],FloatLiteral(10.5))],[While(BooleanLiteral(True),([],[Assign(Id("i"),IntLiteral(2))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("i"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_wrong_expr_with_var_in_while(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(1))],[While(BinaryOp("-",Id("x"),Id("y")),([],[Assign(Id("i"),IntLiteral(2))]))]))])
        expect = str(TypeMismatchInStatement(While(BinaryOp("-",Id("x"),Id("y")),([],[Assign(Id("i"),IntLiteral(2))]))))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_infer_by_while_condition(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[While(BinaryOp("<",Id("x"),Id("y")),([],[Assign(Id("x"),FloatLiteral(2.5))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_infer_by_while_condition_2(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[While(UnaryOp("!",Id("x")),([],[Assign(Id("x"),FloatLiteral(2.5))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_infer_by_while_condition_3(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(2))],[While(UnaryOp("!",Id("x")),([],[Assign(Id("x"),BooleanLiteral(True)),Assign(Id("x"),Id("y"))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_error_while_in_while(self):
        input = Program([FuncDecl(Id("main"),[],([],[While(BooleanLiteral(True),([],[While(BooleanLiteral(True),([],[Assign(Id("i"),IntLiteral(2))]))]))]))])
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_infer_in_callexpr_stmt(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(FloatLiteral(2.5))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(3))],[Assign(Id("x"),CallExpr(Id("alo"),[]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_infer_in_callexpr_expr(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(FloatLiteral(2.5))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(3))],[Assign(Id("x"),BinaryOp("+",IntLiteral(2),CallExpr(Id("alo"),[])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(2),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_infer_in_callexpr_add(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(IntLiteral(2))])),FuncDecl(Id("foo"),[],([],[Return(FloatLiteral(2.5))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("alo"),[])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_return_func_int_func(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(IntLiteral(2))])),FuncDecl(Id("foo"),[],([],[Return(CallExpr(Id("alo"),[]))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],BooleanLiteral(True))],[Assign(Id("x"),CallExpr(Id("alo"),[]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_return_voidtype(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(None)])),FuncDecl(Id("foo"),[],([],[Return(CallExpr(Id("alo"),[]))])),FuncDecl(Id("main"),[],([],[]))])
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_while_cond_with_callexpr(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([],[While(CallExpr(Id("alo"),[]),([],[Assign(Id("i"),IntLiteral(2))]))]))])
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_callexpr_dowhile(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(IntLiteral(10))])),FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(3))],[Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),CallExpr(Id("alo"),[]))]))])
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_not_bool_in_dowhile_cond(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(3))],[Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),BinaryOp("*.",FloatLiteral(22.11),FloatLiteral(11.22)))]))])
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),BinaryOp("*.",FloatLiteral(22.11),FloatLiteral(11.22)))))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_undeclared_in_dowhile(self):
        input = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),BooleanLiteral(True))]))])
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_infer_by_dowhile_expr(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),UnaryOp("!",Id("i")))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("i"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_dowhile_in_dowhile(self):
        input = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[Dowhile(([],[Assign(Id("i"),IntLiteral(2))]),BooleanLiteral(True))]),BooleanLiteral(True))]))])
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_self_infer_dowhile(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[Dowhile(([],[Assign(Id("i"),BooleanLiteral(True)),Assign(Id("i"),StringLiteral("True"))]),Id("i"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("i"),StringLiteral("True"))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_self_infer_while(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[While(Id("i"),([],[Assign(Id("i"),BooleanLiteral(True)),Assign(Id("i"),StringLiteral("True"))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("i"),StringLiteral("True"))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_invoke_callstmt_after_main(self):
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("flag"),[])])),FuncDecl(Id("flag"),[VarDecl(Id("i"),[],None)],([],[]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("flag"),[])))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_invoke_callexpr_after_main(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("flag"),[]))])),FuncDecl(Id("flag"),[VarDecl(Id("i"),[],None)],([],[]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("flag"),[])))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_cannot_infer_callexpr(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("flag"),[Id("x")]))])),FuncDecl(Id("flag"),[VarDecl(Id("i"),[],None)],([],[]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("flag"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_wrong_inittype_for(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[For(Id("x"),FloatLiteral(1.2),BinaryOp(">",Id("x"),Id("y")),IntLiteral(5),([],[Assign(Id("x"),FloatLiteral(3.5))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("x"),FloatLiteral(1.2),BinaryOp(">",Id("x"),Id("y")),IntLiteral(5),([],[Assign(Id("x"),FloatLiteral(3.5))]))))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_undeclared_init_for(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("y"),[],None)],([],[For(Id("x"),FloatLiteral(1.2),BinaryOp(">",Id("x"),Id("y")),IntLiteral(5),([],[]))]))])
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_wrong_idxtype_for(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],StringLiteral("hello")),VarDecl(Id("y"),[],None)],([],[For(Id("x"),IntLiteral(1),BinaryOp(">",Id("x"),Id("y")),IntLiteral(5),([],[]))]))])
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp(">",Id("x"),Id("y")),IntLiteral(5),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_wrong_expr2type_for(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("z"),[],None)],[Assign(Id("z"),UnaryOp("-.",FloatLiteral(2.2))),For(Id("x"),IntLiteral(1),Id("z"),IntLiteral(5),([],[]))]))])
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),Id("z"),IntLiteral(5),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_arrayliteral_for(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("y"),[],None)],[For(Id("y"),ArrayCell(Id("x"),[IntLiteral(2)]),BooleanLiteral(True),ArrayCell(Id("x"),[IntLiteral(3)]),([],[Assign(Id("x"),BooleanLiteral(False))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_arrayliteral_while(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[While(BinaryOp("<",ArrayCell(Id("x"),[IntLiteral(1)]),ArrayCell(Id("x"),[IntLiteral(2)])),([],[Assign(Id("x"),BooleanLiteral(False))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_arrayliteral_dowhile(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Dowhile(([],[Assign(Id("x"),BooleanLiteral(False))]),BinaryOp("<",ArrayCell(Id("x"),[IntLiteral(1)]),ArrayCell(Id("x"),[IntLiteral(2)])))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_infer_by_expr_for(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[For(Id("z"),Id("x"),Id("y"),IntLiteral(3),([],[Assign(Id("y"),BooleanLiteral(False)),Assign(Id("z"),IntLiteral(2)),Assign(Id("x"),BooleanLiteral(False))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_infer_func_by_for(self):
        input = Program([FuncDecl(Id("alo"),[],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[For(Id("y"),CallExpr(Id("alo"),[]),BooleanLiteral(True),IntLiteral(5),([],[Assign(Id("x"),CallExpr(Id("alo"),[]))])),Assign(Id("x"),FloatLiteral(2.3))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(2.3))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_wrong_condtype_if(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[If([[BinaryOp("+",Id("x"),Id("y")),[],[Assign(Id("x"),IntLiteral(10))]],[BinaryOp("!=",Id("x"),Id("y")),[],[]]],([],[]))]))])
        expect = str(TypeMismatchInStatement(If([(BinaryOp("+",Id("x"),Id("y")),[],[Assign(Id("x"),IntLiteral(10))]),(BinaryOp("!=",Id("x"),Id("y")),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_undeclared_inside_if(self):
        input = Program([FuncDecl(Id("main"),[],([],[If([[BinaryOp("+",Id("x"),IntLiteral(2)),[],[]]],([],[]))]))])
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_undeclared_func_inside_if(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[If([[BinaryOp("<",Id("x"),IntLiteral(2)),[],[CallStmt(Id("alo"),[])]]],([],[]))]))])
        expect = str(Undeclared(Function(),"alo"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_infer_func_inside_if(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(2))],[If([[CallExpr(Id("alo"),[]),[],[Assign(Id("x"),CallExpr(Id("alo"),[]))]]],([],[]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_cannot_infer_inside_if(self):
        input = Program([FuncDecl(Id("alo"),[],([],[Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[If([[CallExpr(Id("alo"),[]),[VarDecl(Id("y"),[],None)],[Assign(Id("x"),Id("y"))]]],([],[]))]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_another_infer_in_if(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[If([[BinaryOp(">",BinaryOp("*",Id("x"),Id("y")),Id("z")),[],[Assign(Id("x"),BinaryOp("-",Id("y"),Id("z")))]]],([],[Assign(Id("x"),BooleanLiteral(True))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_redeclared_builtin_func(self):
        input = Program([FuncDecl(Id("main"),[],([],[])),FuncDecl(Id("float_to_int"),[],([],[]))])
        expect = str(Redeclared(Function(),"float_to_int"))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_assign_wrong_type_builtin_callstmt(self):
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("bool_of_string"),[BooleanLiteral(2)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("bool_of_string"),[BooleanLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_assign_wrong_type_builtin_callexpr(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("string_of_int"),[BooleanLiteral(2)]))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("string_of_int"),[BooleanLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_wrong_parameter_callstmt_builtin(self):
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("read"),[BooleanLiteral(2)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("read"),[BooleanLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_infer_by_builtin_func(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallStmt(Id("string_of_int"),[IntLiteral(2)])),Assign(Id("x"),IntLiteral(2))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_infer_voidtype_func_in_expr(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("printLn"),[]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("printLn"),[]))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_infer_arraycell(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Return(ArrayCell(Id("arr"),[]))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id("arr"),[])))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_return_str_arraycell(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[Assign(Id("x"),CallExpr(Id("alo"),[])),Assign(Id("y"),CallExpr(Id("f2"),[])),Assign(Id("x"),Id("y"))])),FuncDecl(Id("alo"),[],([],[Return(ArrayLiteral([IntLiteral(1)]))])),FuncDecl(Id("f2"),[],([],[Return(StringLiteral(""))]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("alo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_recur_param(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("y"),[],FloatLiteral(7.0))],[Assign(Id("x"),IntLiteral(5)),CallStmt(Id("main"),[Id("y")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_some_testcase(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])])])),Return(None)]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_funccall_expr(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),BinaryOp("<=.",CallExpr(Id("main"),[Id("x")]),CallExpr(Id("main"),[IntLiteral(5)])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("<=.",CallExpr(Id("main"),[Id("x")]),CallExpr(Id("main"),[IntLiteral(5)]))))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_arraycel_idx(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(1),IntLiteral(3),IntLiteral(2)]))],[Return(ArrayCell(Id("arr"),[CallExpr(Id("main"),[])]))])),FuncDecl(Id("test"),[],([],[CallStmt(Id("main"),[])]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id("arr"),[CallExpr(Id("main"),[])])))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_unknown_arraycell(self):
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[2,3],None)],[Assign(Id("x"),Id("y"))]))])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_composite_func_param(self):
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[2],None)],([],[Assign(Id("x"),ArrayLiteral([IntLiteral(5),IntLiteral(6)])),Return(CallExpr(Id("main"),[Id("x")]))]))])
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_final(self):
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("So Tired :(((,thanks teacher,i have already done my best"),[])]))])
        expect = str(Undeclared(Function(),"So Tired :(((,thanks teacher,i have already done my best"))
        self.assertTrue(TestChecker.test(input,expect,500))
