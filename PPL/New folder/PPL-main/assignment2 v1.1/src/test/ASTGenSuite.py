import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var: x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_var_decl(self):
        input = """Var: a = 5;"""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_many_var_decl(self):
        input = """Var: c, d = 6, e, f;"""
        expect = Program([VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_array_var_decl(self):
        input = """Var: m, n[10];"""
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_vardecls(self):
        input = """Var:x, y;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_vardecl2(self):
        input = """Var:x = 2, y = 5.6;"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(2)), VarDecl(Id("y"), [], FloatLiteral(5.6))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_compo_var_decl(self):
        input = """Var: b[3] = {2, 3, 4};"""
        expect = Program([VarDecl(Id("b"),[IntLiteral(3)],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    
    def test_another_intlit_var(self):
        input = """Var: abc[0o567][0xFCE]; """
        expect = Program([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    
    def test_program(self):
        input = """
        Function: main
            Body:
                x = 10;
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_var_stmt_program(self):
        input = """
        Function: main
            Body:
                Var: z = 20;
                x = 10;
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("z"),[],IntLiteral(20))],[Assign(Id("x"),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    
    def test_composite_para(self):
        input = """
            Function: main
            Body:
                x[0][0xE3] = 22;
            EndBody. """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(227)]),IntLiteral(22))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_empty_body(self):
        input = """
        Function: main
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_var_stmt(self):
        input = """
        Function: main
            Body:
                x = 1 + 2 * 3 \ 4;
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),BinaryOp("+",IntLiteral(1),BinaryOp("\\",BinaryOp("*",IntLiteral(2),IntLiteral(3)),IntLiteral(4))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_op_expr_stmt(self):
        input = """
        Function: main
            Body:
                x = (1 + 1) * (4 - 5);
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(1)),BinaryOp("-",IntLiteral(4),IntLiteral(5))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_var_op_expr_stmt(self):
        input = """
        Function: main
            Body:
                x = 2 + y;
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),BinaryOp("+",IntLiteral(2),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_float_assign(self):
        input = """
        Function: main
            Body:
                x = 1.2 + 3.4 - 1.5;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),BinaryOp("-",BinaryOp("+",FloatLiteral(1.2),FloatLiteral(3.4)),FloatLiteral(1.5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    
    def test_para(self):
        input = """
        Function: main
        Parameter: n
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    
    def test_index_para(self):
        input = """
        Function: main
            Parameter: i[2]
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("i"),[IntLiteral(2)],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_normal_for(self):
        input = """
        Function: main
            Body:
                For(i=0,i<5,2) Do x+1;
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[None,None]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test_funccall_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i < 5, 2)
                Do print(i);
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[CallStmt(Id("print"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_if_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i < 5, 2)
                Do
                    If !True
                    Then a = 1;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[If([(UnaryOp("!",BooleanLiteral(True)),[],[Assign(Id("a"),IntLiteral(1))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_break_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i<5, 2)
                Do
                    If a != 0
                    Then Break;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[If([(BinaryOp("!=",Id("a"),IntLiteral(0)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    
    def test_continue_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i < 5, 2)
                Do
                    If !0
                    Then Break;
                    Else Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[If([(UnaryOp("!",IntLiteral(0)),[],[Break()])],([],[Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    
    def test_return_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i < 5, 2)
                Do
                    If ! a
                    Then Return 0;
                    Else Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[If([(UnaryOp("!",Id("a")),[],[Return(IntLiteral(0))])],([],[Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_ifstmt(self):
        input = """
            Function: main
                Body:
                    If a > b Then h = a;
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("h"),Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    
    def test_else_ifstmt(self):
        input = """
            Function: main
                Body:
                    If a > 0
                    Then b = 0;
                    Else c = 0;
                    EndIf.
                EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp(">",Id("a"),IntLiteral(0)),[],[Assign(Id("b"),IntLiteral(0))])],([],[Assign(Id("c"),IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))
    
    def test_expr_cond_ifstmt(self):
        input = """
        Function: main
            Body:
                If a == 0
                Then b = 25 % b;
                Else c = (a + b);
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(0)),[],[Assign(Id("b"),BinaryOp("%",IntLiteral(25),Id("b")))])],([],[Assign(Id("c"),BinaryOp("+",Id("a"),Id("b")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_normal_while(self):
        input = """
            Function: main
                Body:
                    While i < 5
                    Do i = i + 1;
                    EndWhile.
                EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)), ([],[Assign(Id("i"), BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_if_while(self):
        input = """
        Function: main
            Body:
                While x < 2
                Do
                    If a > 2
                    Then a = 1;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(2)),([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Assign(Id("a"),IntLiteral(1))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    
    def test_break_while(self):
        input = """
        Function: main
            Body:
                While x < 2
                Do
                    If a > 2
                    Then Break;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(2)),([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    
    def test_continue_while(self):
        input = """
        Function: main
            Body:
                While i < 10
                Do Continue;
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(10)),([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_return_while(self):
        input = """
        Function: main
            Body:
                While i < 10
                Do
                    If i == 4
                    Then Return 3 * i;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(10)),([],[If([(BinaryOp("==",Id("i"),IntLiteral(4)),[],[Return(BinaryOp("*",IntLiteral(3),Id("i")))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_func_stmt_while(self):
        input = """
        Function: main
            Body:
                While x + 2
                Do Return print(x);
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("+",Id("x"),IntLiteral(2)),([],[Return(CallExpr(Id("print"),[Id("x")]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_normal_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    x = a + b;
                    writeln(x);
                While(a > b)
                EndDo.
            EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("a"),Id("b"))),CallStmt(Id("writeln"),[Id("x")])]),BinaryOp(">",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_func_expr_dowhile(self):
        input = """
        Function: main
            Body:
            Do print(i);
            While(a == b)
            EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[CallStmt(Id("print"),[Id("i")])]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    
    def test_if_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    If a > 2
                    Then a = 0;
                    EndIf.
                While(a == b)
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Assign(Id("a"),IntLiteral(0))])],([],[]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    
    def test_break_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    If a > 2
                    Then Break;
                    EndIf.
                While(a == b)
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Break()])],([],[]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    
    def test_continue_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    If a > 2
                    Then Break;
                    Else Continue;
                    EndIf.
                While(a == b)
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Break()])],([],[Continue()]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))
    
    def test_return_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    If a > 2
                    Then Return a;
                    Else Continue;
                    EndIf.
                While(a == b)
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Return(Id("a"))])],([],[Continue()]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_while_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    While i < 5
                    Do a[i] = b +.1.0;
                    i = i + 1;
                    EndWhile.
                While(a == b)
                EndDo
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
    
    def test_varstmt_dowhile(self):
        input = """
        Function: main
            Body:
                Do
                    Var: x = 10;
                    If a > 2
                    Then a = 0;
                    EndIf.
                While a==b
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([VarDecl(Id("x"),[],IntLiteral(10))],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Assign(Id("a"),IntLiteral(0))])],([],[]))]),BinaryOp("==",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_many_stmt_while(self):
        input = """
        Function: main
            Body:
                While (x<2) && (a==0)
                Do
                    If a > 2
                    Then Break;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(0))),([],[If([(BinaryOp(">",Id("a"),IntLiteral(2)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_boolean(self):
        input = """
        Function: main
            Body:
                a = !True;
                b = (False || True) && True;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",BooleanLiteral(True))),Assign(Id("b"),BinaryOp("&&",BinaryOp("||",BooleanLiteral(False),BooleanLiteral(True)),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))
    
    def test_index_op(self):
        input = """
        Function: main
            Body:
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    
    def test_complicated_var(self):
        input = """
        Function: main
            Body:
                Var: a[a[numb(2)][b || True]][b[b[1 + 0o567]]] = 4;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[ArrayCell(Id("a"),[CallExpr(Id("numb"),[IntLiteral(2)]),BinaryOp("||",Id("b"),BooleanLiteral(True))]),ArrayCell(Id("b"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(1),IntLiteral(375))])])],IntLiteral(4))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_vardecl_program(self):
        input = """
        Function: main
            Body:
                Var: r = 10., v;
                v = (4. \.3.) *.3.14 *.r *.r *.r;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[], None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))
    
    def test_vardecl_not_first_instmt(self):
        input = """
        Function: main
            Body:
            Var: i = 0;
                While i < 5
                Do Var: k = 10;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([VarDecl(Id("k"), [], IntLiteral(10))],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    
    def test_vardecl_first(self):
        input = """
        Function: main
            Body:
            Var: i = 0;
                While i < 5
                Do
                    Var: k = 10;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([VarDecl(Id("k"),[],IntLiteral(10))],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_array_literal(self):
        input = """
        Function: main
            Body:
                a[3] = {10, 15, 20};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(3)]),ArrayLiteral([IntLiteral(10),IntLiteral(15),IntLiteral(20)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_two_dim_array(self):
        input = """
        Function: main
            Body:
                a[2][3] = {{10, 15, 20}, {1, 2, 3}};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(10),IntLiteral(15),IntLiteral(20)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    
    def test_array_with_space(self):
        input = """
        Function: main
            Body:
                a[3] = {10, 15, 20};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(3)]),ArrayLiteral([IntLiteral(10),IntLiteral(15),IntLiteral(20)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_different_item_array(self):
        input = """
        Function: main
            Body:
                a[3] = {1, True, 3.0};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(3)]),ArrayLiteral([IntLiteral(1),BooleanLiteral(True),FloatLiteral(3.0)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    
    def test_diff_item_indim_array(self):
        input = """
        Function: main
            Body:
                a[2][2] = {{1, 3}, {"a", "b"}};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2)]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(3)]),ArrayLiteral([StringLiteral("a"),StringLiteral("b")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_exprindex_array(self):
        input = """
        Function: main
            Body:
                a[0o567+sum(a,b)] = {1, 3};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(375),CallExpr(Id("sum"),[Id("a"),Id("b")]))]),ArrayLiteral([IntLiteral(1),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    
    def test_sign_operator(self):
        input = """
        Function: main
            Body:
                a = -10;
                b = -0o567;
                c = -0xFFE;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("-",IntLiteral(10))),Assign(Id("b"),UnaryOp("-",IntLiteral(375))),Assign(Id("c"),UnaryOp("-",IntLiteral(4094)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    
    def test_funccall(self):
        input = """
        Function: main
            Body:
                print(x);
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    
    def test_funcall_semi(self):
        input = """
        Function: main
            Body:
                print(a, b, c=0);
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("a"),Id("b"),Id("c")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    
    def test_funcall_funcall(self):
        input = """
        Function: main
            Body:
                print(sum(add(22, 11)));
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("sum"),[CallExpr(Id("add"),[IntLiteral(22),IntLiteral(11)])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    
    def test_many_functions(self):
        input = """
        Var: x;
        Function: fact
        Parameter: n
            Body:
                If n == 0
                Then Return 1;
                Else Return n * fact(n - 1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[], None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[], None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    
    def test_many_vardecl(self):
        input = """
                Var: a = 10.;
                Var: b[5];
                Var: c[2][3],d = 6, e;
                """
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(10.0)),VarDecl(Id("b"),[IntLiteral(5)], None),VarDecl(Id("c"),[IntLiteral(2),IntLiteral(3)], None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_many_vardecl_in_func(self):
        input = """
            Var: a = 10.;
            Var: b[0];
            Var: c[1][2], e;
            Function: main
            Body:
                Var: a = 10.;
                Var: b[0];
                Var: c[1][2], e;
            EndBody."""
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(10.0)),VarDecl(Id("b"),[IntLiteral(0)], None),VarDecl(Id("c"),[IntLiteral(1),IntLiteral(2)], None),VarDecl(Id("e"),[], None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],FloatLiteral(10.0)),VarDecl(Id("b"),[IntLiteral(0)], None),VarDecl(Id("c"),[IntLiteral(1),IntLiteral(2)], None),VarDecl(Id("e"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_array_func(self):
        input = """
        Function: main
        Body:
            Var: i = 1 ;
            n[i+1] = 10; 
            printLn (n[i+i])
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(1))],[Assign(ArrayCell(Id("n"),[BinaryOp("+",Id("i"),IntLiteral(1))]),IntLiteral(10)),CallStmt(Id("printLn"),[ArrayCell(Id("n"),[BinaryOp("+",Id("i"),Id("i"))])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_many_if(self):
        input = """
        Function: main
        Body:
            Var: i = 1 ;
            If a > b
            Then 
                If b > c
                Then Break;
                Else a = 0;
                EndIf.
            EndIf.
            If c>d
            Then c=1+3+4+5;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(1))],[If([(BinaryOp(">",Id("a"),Id("b")),[],[If([(BinaryOp(">",Id("b"),Id("c")),[],[Break()])],([],[Assign(Id("a"),IntLiteral(0))]))])],([],[])),If([(BinaryOp(">",Id("c"),Id("d")),[],[Assign(Id("c"),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_string_var(self):
        input = """Var: a="Alo" """
        expect = Program([VarDecl(Id("a"),[],StringLiteral("Alo"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_string_multivar(self):
        input = """Var: a[1]="Alo",b, c=2 """
        expect = Program([VarDecl(Id("a"),[IntLiteral(1)],StringLiteral("Alo")),VarDecl(Id("b"),[], None),VarDecl(Id("c"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_string_assign(self):
        input = """
        Function: main
             Body:
                 a = "What are you doing";
                 b = "Bye bye";
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),StringLiteral("What are you doing")),Assign(Id("b"),StringLiteral("Bye bye"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_string_array(self):
        input = """
        Function: main
             Body:
                 a[4] = {"abc", "def", "ghi", "jkl"};
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(4)]),ArrayLiteral([StringLiteral("abc"),StringLiteral("def"),StringLiteral("ghi"),StringLiteral("jkl")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_string_in_func(self):
        input = """Var: a;
        Function: main
             Body:
                 Var: name;
                 printLn("Enter your name:");
                 read(name);
             EndBody."""
        expect = Program([VarDecl(Id("a"),[], None),FuncDecl(Id("main"),[],([VarDecl(Id("name"),[], None)],[CallStmt(Id("printLn"),[StringLiteral("Enter your name:")]),CallStmt(Id("read"),[Id("name")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_string_argument(self):
        input = """
        Function: sum
        Parameter: a,b
            Body:
                Return a + b;
            EndBody.
        Function: main
             Body:
                 sum("Hello", "World!");
             EndBody."""
        expect = Program([FuncDecl(Id("sum"),[VarDecl(Id("a"),[], None),VarDecl(Id("b"),[], None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("sum"),[StringLiteral("Hello"),StringLiteral("World!")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_string_multielement(self):
        input = """
        Function: main
             Body:
                 arr[4][2] = {{"123", "True", "22.11", "jkl"},{"123", "True", "22.11", "jkl"}};
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("arr"),[IntLiteral(4),IntLiteral(2)]),ArrayLiteral([ArrayLiteral([StringLiteral("123"),StringLiteral("True"),StringLiteral("22.11"),StringLiteral("jkl")]),ArrayLiteral([StringLiteral("123"),StringLiteral("True"),StringLiteral("22.11"),StringLiteral("jkl")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_bool_assign(self):
        input = """
        Function: main
             Body:
                 flag = True;
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("flag"),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_bool_array(self):
        input = """
        Function: main
             Body:
                 flag[3] = {True, False, False};
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("flag"),[IntLiteral(3)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(False)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_bool_var(self):
        input = """
        Function: main
             Body:
                fl = !False;
                flag[3] = {True, False, False};
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("fl"),UnaryOp("!",BooleanLiteral(False))),Assign(ArrayCell(Id("flag"),[IntLiteral(3)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(False)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_bool_function(self):
        input = """
        Function: flag
             Body:
                 Return True;
             EndBody.
        Function: main
             Body:
                 print(flag());
             EndBody."""
        expect = Program([FuncDecl(Id("flag"),[],([],[Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("flag"),[])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_expr_string_func(self):
        input = """Var: age;
        Function: main
             Body:
                 print("Enter your age:");
                 read(age);
                 If age<18
                 Then deniedaccess(False);
                 Else access(True);
                 EndIf.
             EndBody."""
        expect = Program([VarDecl(Id("age"),[], None),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("Enter your age:")]),CallStmt(Id("read"),[Id("age")]),If([(BinaryOp("<",Id("age"),IntLiteral(18)),[],[CallStmt(Id("deniedaccess"),[BooleanLiteral(False)])])],([],[CallStmt(Id("access"),[BooleanLiteral(True)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_many_elseif(self):
        input = """
        Function: main
             Parameter: n
             Body:
                 If (n == 0) Then
                        Return 0;
                 ElseIf (n == 1) Then 
                        Return 1;
                 ElseIf (n == 2) Then 
                        Return 2;
                 ElseIf (n == 3) Then 
                        Return 3;
                 Else Return 4;
                 EndIf.
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[], None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(0))]),(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Return(IntLiteral(1))]),(BinaryOp("==",Id("n"),IntLiteral(2)),[],[Return(IntLiteral(2))]),(BinaryOp("==",Id("n"),IntLiteral(3)),[],[Return(IntLiteral(3))])],([],[Return(IntLiteral(4))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_many_parentheses_function(self):
        input = """
        Function: main
             Body:
                 print((((((((a))))))));
             EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_for_break_continue(self):
        input = """
        Function: main
            Body:
                For(i=0,i<5,2) 
                Do
                    Continue;
                    Break;
                    Return 0; 
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[Continue(),Break(),Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    
    def test_while_break_continue(self):
        input = """
        Function: main
            Body:
                While i<5 
                Do
                    Continue;
                    Break;
                    Return 0; 
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Continue(),Break(),Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_normal_func_define_use(self):
        input = """
            Function: sum0frange
                Parameter: n
                Body:
                    result = 0;
                    For(i=0,i<n,i+1)
                    Do
                        result = result + i;
                    EndFor.
                    Return result;
                EndBody.
            Function: main
                Body:
                    print("Sum from 0 to 10: ");
                    print(sum0range(10));
                EndBody.
            """
        expect = Program([FuncDecl(Id("sum0frange"),[VarDecl(Id("n"),[], None)],([],[Assign(Id("result"),IntLiteral(0)),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),([],[Assign(Id("result"),BinaryOp("+",Id("result"),Id("i")))])),Return(Id("result"))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("Sum from 0 to 10: ")]),CallStmt(Id("print"),[CallExpr(Id("sum0range"),[IntLiteral(10)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_for_in_for(self):
        input = """
            Function: main
                Body:
                    Var: result = 0;
                    For(i=0,i<n,i+1)
                    Do
                        For(j=i,j<n,j+1)
                        Do
                            result = result + i;
                        EndFor.
                    EndFor.
                EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("result"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),([],[For(Id("j"),Id("i"),BinaryOp("<",Id("j"),Id("n")),BinaryOp("+",Id("j"),IntLiteral(1)),([],[Assign(Id("result"),BinaryOp("+",Id("result"),Id("i")))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_complicated_index(self):
        input = """
            Function: main
                Body:
                    a[a[numb(2)][b||True]][b[b[1+0o567]]] = a[b[2][b[12E-9]*3]] + 4;
                EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("a"),[CallExpr(Id("numb"),[IntLiteral(2)]),BinaryOp("||",Id("b"),BooleanLiteral(True))]),ArrayCell(Id("b"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(1),IntLiteral(375))])])]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),BinaryOp("*",ArrayCell(Id("b"),[FloatLiteral(1.2e-08)]),IntLiteral(3))])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_func_in_func(self):
        input = """
            Function: main
                Body:
                    print(divide(sum(add(22, 11)),sub(10,5)));
                EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("divide"),[CallExpr(Id("sum"),[CallExpr(Id("add"),[IntLiteral(22),IntLiteral(11)])]),CallExpr(Id("sub"),[IntLiteral(10),IntLiteral(5)])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_if_for_dowhile(self):
        input = """
            Function: main
                Body:
                    Do 
                        For(x=0, z == 4, z% 2)
                        Do  If (x > 3)
                            Then x-3; 
                            Else x+3;
                            EndIf.
                        EndFor.
                    While a>3
                    EndDo.
                EndBody.      
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[For(Id("x"),IntLiteral(0),BinaryOp("==",Id("z"),IntLiteral(4)),BinaryOp("%",Id("z"),IntLiteral(2)),([],[If([(BinaryOp(">",Id("x"),IntLiteral(3)),[],[None,None])],([],[None,None]))]))]),BinaryOp(">",Id("a"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_many_expr_callstmt(self):
        input = """
            Function: main
                Body:
                    print(a,b,"wat is this", True || !False, 1+1==2, ("another expression"))
                EndBody.      
            """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("a"),Id("b"),StringLiteral("wat is this"),BinaryOp("||",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))),BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)),StringLiteral("another expression")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_callstmt_dowhile(self):
        input = """
            Function: main
                Body:
                    Do 
                        print(a,b,"wat is this", True || !False, 1+1==2, ("another expression"))
                    While a>3
                    EndDo.
                EndBody.      
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[CallStmt(Id("print"),[Id("a"),Id("b"),StringLiteral("wat is this"),BinaryOp("||",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))),BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)),StringLiteral("another expression")])]),BinaryOp(">",Id("a"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_call_for_dowhile(self):
        input = """
            Function: main
                Body:
                    Do 
                        For(x=0, z == 4, z% 2)
                        Do
                            print(a,b,"wat is this", True || !False, 1+1==2, ("another expression"))
                        EndFor.
                    While a>3
                    EndDo.
                EndBody.      
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[For(Id("x"),IntLiteral(0),BinaryOp("==",Id("z"),IntLiteral(4)),BinaryOp("%",Id("z"),IntLiteral(2)),([],[CallStmt(Id("print"),[Id("a"),Id("b"),StringLiteral("wat is this"),BinaryOp("||",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))),BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)),StringLiteral("another expression")])]))]),BinaryOp(">",Id("a"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_call_for_dowhile_var(self):
        input = """
            Var: a = 2;
            Function: main
                Body:
                    Var: abc = 132;
                    Do For(x=0, z == 4, z%2)
                        Do
                            print(a,b,"wat is this", True || !False, 1+1==2, ("another expression"))
                        EndFor.
                    While a>3
                    EndDo.
                EndBody.      
            """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(2)),FuncDecl(Id("main"),[],([VarDecl(Id("abc"),[],IntLiteral(132))],[Dowhile(([],[For(Id("x"),IntLiteral(0),BinaryOp("==",Id("z"),IntLiteral(4)),BinaryOp("%",Id("z"),IntLiteral(2)),([],[CallStmt(Id("print"),[Id("a"),Id("b"),StringLiteral("wat is this"),BinaryOp("||",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))),BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)),StringLiteral("another expression")])]))]),BinaryOp(">",Id("a"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_call_dowhile(self):
        input = """
            Function: main
                Body:
                    Do a+3;
                        If a<4
                        Then a = 10;
                        Else a = foo(3, a[5], !4);
                        EndIf.
                    While (foo())
                    EndDo.
                EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[None,None,If([(BinaryOp("<",Id("a"),IntLiteral(4)),[],[Assign(Id("a"),IntLiteral(10))])],([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3),ArrayCell(Id("a"),[IntLiteral(5)]),UnaryOp("!",IntLiteral(4))]))]))]),CallExpr(Id("foo"),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_combined_program1(self):
        input = """
            Function: main
                Body:
                    Do a+3;
                        If a<4
                        Then Break;
                        Else a = foo(3, a[5], !4);
                        EndIf.
                    While (True)
                    EndDo.
                EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[None,None,If([(BinaryOp("<",Id("a"),IntLiteral(4)),[],[Break()])],([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3),ArrayCell(Id("a"),[IntLiteral(5)]),UnaryOp("!",IntLiteral(4))]))]))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_combined_program2(self):
        input = """
            Function: main
                Body:
                    Do a+3;
                        If a<4
                        Then Return a = foo(3, a[5], !4);
                        Else a[2][3] = {{10,15,20},{1,2,3}};
                        EndIf.
                    While (True)
                    EndDo.
                EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([],[None,None,If([(BinaryOp("<",Id("a"),IntLiteral(4)),[],[Return(Id("a")),CallStmt(Id("foo"),[IntLiteral(3),ArrayCell(Id("a"),[IntLiteral(5)]),UnaryOp("!",IntLiteral(4))])])],([],[Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(10),IntLiteral(15),IntLiteral(20)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_combined_program3(self):
        input = """
            Function: loop
                Body:
                Var: abc[0o567][0xFCE];
                    For(i=0, i < 5, 2)
                    Do
                        If !True
                        Then a = 1;
                        EndIf.
                    EndFor.
                EndBody.
            Function: main
            Parameter: x,y,z,a[1+111]
                Body:
                    Return loop();
                EndBody.
            """
        expect = Program([FuncDecl(Id("loop"),[],([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[If([(UnaryOp("!",BooleanLiteral(True)),[],[Assign(Id("a"),IntLiteral(1))])],([],[]))]))])),FuncDecl(Id("main"),[VarDecl(Id("x"),[], None),VarDecl(Id("y"),[], None),VarDecl(Id("z"),[], None),VarDecl(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(111))], None)],([],[Return(CallExpr(Id("loop"),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_combined_program4(self):
        input = """
            Function: loop
                Body:
                Var: abc[0o567][0xFCE];
                    For(i=0, i < 5, 2)
                    Do Break;
                    EndFor.
                EndBody.
            Function: sum
                Body:
                    Return a+b;
                EndBody.
            Function: sub
                Body:
                    Return a-b;
                EndBody.
            Function: main
            Parameter: x,y,z,a[1+111]
                Body:
                    Return loop();
                EndBody.
            """
        expect = Program([FuncDecl(Id("loop"),[],([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(2),([],[Break()]))])),FuncDecl(Id("sum"),[],([],[Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("sub"),[],([],[Return(BinaryOp("-",Id("a"),Id("b")))])),FuncDecl(Id("main"),[VarDecl(Id("x"),[], None),VarDecl(Id("y"),[], None),VarDecl(Id("z"),[], None),VarDecl(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(111))], None)],([],[Return(CallExpr(Id("loop"),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_combined_program5(self):
        input = """Var: a[6][5][4];
        Function: main 
        Parameter: a,b[2][2] 
            Body: Var: arr[3] = {1,2,3};   
                If g != null 
                Then print(g);  
                    Return;
                EndIf.  
                print("So much"); 
            EndBody."""
        expect = Program([VarDecl(Id("a"),[IntLiteral(6),IntLiteral(5),IntLiteral(4)], None),FuncDecl(Id("main"),[VarDecl(Id("a"),[], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(2)], None)],([VarDecl(Id("arr"),[IntLiteral(3)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[If([(BinaryOp("!=",Id("g"),Id("null")),[],[CallStmt(Id("print"),[Id("g")]),Return(None)])],([],[])),CallStmt(Id("print"),[StringLiteral("So much")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_combined_program6(self):
        input = """ Var: abc[0o567][0xFCE];
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: m, n[10];
            Function: main
                 Body:
                 EndBody. """
        expect = Program([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_manyvardecl_program(self):
        input = """ Var: abc[0o567][0xFCE];
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: m, n[10];
            Function: main
                 Body:
                    Var: abc[0o567][0xFCE];
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: m, n[10];
                 EndBody. """
        expect = Program([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None),FuncDecl(Id("main"),[],([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_manyvardecl_if(self):
        input = """
        Function: main
            Body:
                If (g != "null") 
                Then  Var: abc[0o567][0xFCE];
                ElseIf (a == "notnull")
                Then Var: b[2][3] = {{2,3,4},{4,5,6}};
                Else Var: m, n[10];
                EndIf. 
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp("!=",Id("g"),StringLiteral("null")),[VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None)],[]),(BinaryOp("==",Id("a"),StringLiteral("notnull")),[VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[])],([VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None)],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_manyvardecl_for(self):
        input = """
        Function: main
            Body:
                For(i=0, i<10, i+1)
                Do
                    Var: abc[0o567][0xFCE];
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: m, n[10];
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None)],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_manyvardecl_while(self):
        input = """
        Function: main
            Body:
                While (i<10)
                Do Var: abc[0o567][0xFCE];
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: m, n[10];
                    print("Hello");
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(10)),([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None)],[CallStmt(Id("print"),[StringLiteral("Hello")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_manyvardecl_dowhile(self):
        input = """
        Function: main
            Body:
                Do Var: abc[0o567][0xFCE];
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: m, n[10];
                    print("Hello");
                While (i<10)
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Dowhile(([VarDecl(Id("abc"),[IntLiteral(375),IntLiteral(4046)], None),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("m"),[], None),VarDecl(Id("n"),[IntLiteral(10)], None)],[CallStmt(Id("print"),[StringLiteral("Hello")])]),BinaryOp("<",Id("i"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_final_program(self):
        input = """
        Function: main
            Body:
                print("Hello World!")
            EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("Hello World!")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))