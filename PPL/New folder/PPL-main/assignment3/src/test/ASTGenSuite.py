import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        Function: main
            Body:
                x = ;
            EndBody."""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    # def test_var_stmt_program(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: z = 20;
    #             x = 10;
    #         EndBody."""
    #     expect = Program(
    #         [FuncDecl(Id("main"), [], ([VarDecl(Id("z"), [], IntLiteral(20))], [Assign(Id("x"), IntLiteral(10))]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))
