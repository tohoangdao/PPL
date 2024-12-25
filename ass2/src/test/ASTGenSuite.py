import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_full_vardecl_concate_1(self):
        input = """x: auto = a :: b;"""
        expect = """Program([
	VarDecl(x, AutoType, BinExpr(::, Id(a), Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_full_vardecl_concate_2(self):
        input = """x, y: float = a :: b, (a_sdq :: sda) :: asw; """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(::, Id(a), Id(b)))
	VarDecl(y, FloatType, BinExpr(::, BinExpr(::, Id(a_sdq), Id(sda)), Id(asw)))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_full_vardecl_concate_3(self):
        input = """x, y: array [1_02, 23] of string = (\"he slo ae\" :: true) :: (1_23.0e-10 :: a), (a_sdq :: sda) :: asw; """
        expect = """Program([
	VarDecl(x, ArrayType([102, 23], StringType), BinExpr(::, BinExpr(::, StringLit(he slo ae), BooleanLit(True)), BinExpr(::, FloatLit(1.23e-08), Id(a))))
	VarDecl(y, ArrayType([102, 23], StringType), BinExpr(::, BinExpr(::, Id(a_sdq), Id(sda)), Id(asw)))
])"""

        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_full_vardecl_compares(self):
        input = """x: boolean = ((((a == b) >= c) < d) > s) != 1_00_00;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(!=, BinExpr(>, BinExpr(<, BinExpr(>=, BinExpr(==, Id(a), Id(b)), Id(c)), Id(d)), Id(s)), IntegerLit(10000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_full_vardecl_andor(self):
        input = """x: boolean = (a && b) || c;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_full_vardecl_operator1(self):
        input = """x: integer = (1_123 + 2.10e+10) - 1_0_0_0;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_full_vardecl_operator2(self):
        input = """x: integer = ((1_123 * 2.10e+10) / 1_0_0_0) % abc;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)), Id(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_full_vardecl_negation(self):
        input = """x, y, z: integer = !ab, !(!a), !(!(!b));"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(!, Id(ab)))
	VarDecl(y, IntegerType, UnExpr(!, UnExpr(!, Id(a))))
	VarDecl(z, IntegerType, UnExpr(!, UnExpr(!, UnExpr(!, Id(b)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test_full_vardecl_index(self):
        input = """x: integer = a[1 + 2, a == b, \"hello\", !a_SADsd, 3 * 3.0];"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), StringLit(hello), UnExpr(!, Id(a_SADsd)), BinExpr(*, IntegerLit(3), FloatLit(3.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))


    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_assignstmt_program_1(self):
        input = """main: function void () {
            a = b;
            as = c + 2.0e-3;
            ass = (\"Hello\" + \"asdas\") :: 10_20.1e2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(as), BinExpr(+, Id(c), FloatLit(0.002))), AssignStmt(Id(ass), BinExpr(::, BinExpr(+, StringLit(Hello), StringLit(asdas)), FloatLit(102010.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))   


    def test_assignstmt_program_2(self):
        input = """main: function void () {
            a[1_0, 2] = b >= a;
            a[1] = arr[1];

        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(10), IntegerLit(2)]), BinExpr(>=, Id(b), Id(a))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(arr, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_ifstmt_program_1(self):
        input = """main: function void () {
           if (DSAD == b) print(2_213_1231);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(DSAD), Id(b)), CallStmt(print, IntegerLit(22131231)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316)) 
    
    def test_ifstmt_program_2(self):
        """if with blockstmt"""
        input = """main: function void(){
                    if ((x > 1) && (x <= 10)) 
                        {
                            y = 2;
                            continue;
                        }
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(x), IntegerLit(1)), BinExpr(<=, Id(x), IntegerLit(10))), BlockStmt([AssignStmt(Id(y), IntegerLit(2)), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317)) 

    def test_ifstmt_program_3(self):
        """if else with blockstmt"""
        input = """main: function void () {
           if ((DSAD == b) && (a :: b))  {
                return asdasdads();
           }
           else {
                if (a + 1 == 2) break;
           }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(DSAD), Id(b)), BinExpr(::, Id(a), Id(b))), BlockStmt([ReturnStmt(FuncCall(asdasdads, []))]), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), IntegerLit(1)), IntegerLit(2)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318)) 

    def test_forstmt_program_1(self):
        """for statement"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                printInteger();
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), CallStmt(printInteger, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319)) 
    
    def test_forstmt_program_2(self):
        """for statement wwith blockstmt"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                {
                    printInteger();
                    a: integer = 10_23; 
                    return a + 1;
                }
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ), VarDecl(a, IntegerType, IntegerLit(1023)), ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320)) 
    
    def test_forstmt_program_3(self):
        """for statement wwith blockstmt"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                {
                    if ((a && b) >= 1.21) return helloworld();
                    else break;
                    a,b: array[2] of integer;
                }
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(&&, Id(a), Id(b)), FloatLit(1.21)), ReturnStmt(FuncCall(helloworld, [])), BreakStmt()), VarDecl(a, ArrayType([2], IntegerType)), VarDecl(b, ArrayType([2], IntegerType))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321)) 

    def test_whilestmt_program_1(self):
        """while statement without blockstmt"""
        input = """ASDASD: function boolean(inherit out a: auto, out b: array [2] of string) inherit a
        {
            while( a >= b ) return a();
        }
        """
        expect = """Program([
	FuncDecl(ASDASD, BooleanType, [InheritOutParam(a, AutoType), OutParam(b, ArrayType([2], StringType))], a, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), ReturnStmt(FuncCall(a, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322)) 
    

    def test_whilestmt_program_2(self):
        """while statement without blockstmt"""
        input = """ASDASD: function boolean(inherit out a: auto, out b: array [2] of string) inherit a
        {
            while( a >= b ) 
                if (a == n) return printInteger(); 
                else break;
        }
        """
        expect = """Program([
	FuncDecl(ASDASD, BooleanType, [InheritOutParam(a, AutoType), OutParam(b, ArrayType([2], StringType))], a, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), IfStmt(BinExpr(==, Id(a), Id(n)), ReturnStmt(FuncCall(printInteger, [])), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323)) 

    def test_whilestmt_program_3(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                a,b,c: integer = 1,2,3;
                a[1] = 1.2;
                break;    
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), FloatLit(1.2)), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324)) 
    
    def test_whilestmt_program_4(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                while(a == b) {
                    break;
                }  
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325)) 
    

    def test_whilestmt_program_5(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                while(a == b) {
                    while (a <= b) 
                    {
                        {break;}
                    }
                }  
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(<=, Id(a), Id(b)), BlockStmt([BlockStmt([BreakStmt()])]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326)) 
    
    def test_dowhilestmt_program_1(self):
        input = """main: function void()
        {
           do {a = a + 1;} while(a == b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test_dowhilestmt_program_2(self):
        input = """main: function void()
        {
           do {{{a = a + 1;}}} while(a[1] == b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), Id(b)), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    
 

# -----------------------TESTCASE--------------------------------
    def testcase29(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def testcase30(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    a: integer = a[1+2, 1*5];"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(a, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def testcase31(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    d: integer = a[1+2, 1*5];
                    c: string = a(1, f("abc"));"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(d, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
	VarDecl(c, StringType, FuncCall(a, [IntegerLit(1), FuncCall(f, [StringLit(abc)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def testcase32(self):
        # test vardecl with no init of array
        input = """x: array[2,3] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def testcase33(self):
        # test basic funcdecls
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
        printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def testcase34(self):
        # test funcdecls
        input = """main: function void () {
        x: integer;
        x = (3+4)*2;
        b: array [2] of float;
        b[0] = 4.5;
        preventDefault();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(*, BinExpr(+, IntegerLit(3), IntegerLit(4)), IntegerLit(2))), VarDecl(b, ArrayType([2], FloatType)), AssignStmt(ArrayCell(b, [IntegerLit(0)]), FloatLit(4.5)), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def testcase35(self):
        # ifstmt without blockstmt and else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def testcase36(self):
        # ifstmt without blockstmt but have else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
        else a[0] = "hello world in else";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world in else)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def testcase37(self):
        # forstmt without block
        input = """
    a,b,c : array [2] of integer = {1,1}, {2,2}, {3,5-4};
    main: function void () {
        for (i=1,i<100,i+1) break;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(1)]))
	VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(2)]))
	VarDecl(c, ArrayType([2], IntegerType), ArrayLit([IntegerLit(3), BinExpr(-, IntegerLit(5), IntegerLit(4))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def testcase38(self):
        # forstmt with block
        input = """
    main: function void () {
        for (i=1,i<100,i+1) {
            if (a<1) continue;
            a: boolean = false;
        }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), ContinueStmt()), VarDecl(a, BooleanType, BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def testcase39(self):
        # whilestmt without block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) a = a + 1;
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def testcase40(self):
        # whilestmt with block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) {
            for(i = 1, i < 10, i + 1) a = a + 1;
        }
        readBoolean(a==10);
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))])), CallStmt(readBoolean, BinExpr(==, Id(a), IntegerLit(10))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def testcase41(self):
        # dowhile
        input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(c, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(c), StringLit()), BlockStmt([CallStmt(readString, StringLit(abc)), AssignStmt(Id(c), BinExpr(::, Id(c), StringLit(abc))), CallStmt(printString, Id(c))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def testcase42(self):
        input = """
    testfunc: function auto (a: boolean) {
        while (a < 10) {
            {
                a = a + 1;
            }
        }
    }
"""
        expect = """Program([
	FuncDecl(testfunc, AutoType, [Param(a, BooleanType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def testcase43(self):
        input = """
    testfunc: function string (a: boolean) {
        x: float = 1.5e-10 + x + y;
    }
"""
        expect = """Program([
	FuncDecl(testfunc, StringType, [Param(a, BooleanType)], None, BlockStmt([VarDecl(x, FloatType, BinExpr(+, BinExpr(+, FloatLit(1.5e-10), Id(x)), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def testcase44(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def testcase45(self):
        input = """
    testfunc: function void (inherit out a: array[2, 3] of boolean) inherit foo {
        if(a[a[1, 2], 2] == "true") {
            {
                {
                    a[a[a[1, 2], 3], 2] = "false";
                }
            }
        }
            
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([2, 3], BooleanType))], foo, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(2)]), StringLit(true)), BlockStmt([BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3)]), IntegerLit(2)]), StringLit(false))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_stmt1(self):
        input = """
        main : function void () {
            a = b;
            __a = ___;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(__a), Id(___))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_stmt2(self):
        input = """
        main : function void () {
            int_var = 1_2 * (.e-3 + a)/b % 2;
            bool_var = a > b&&!c;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(int_var), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(12), BinExpr(+, FloatLit(0.0), Id(a))), Id(b)), IntegerLit(2))), AssignStmt(Id(bool_var), BinExpr(>, Id(a), BinExpr(&&, Id(b), UnExpr(!, Id(c)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_stmt3(self):
        input = """
        main : function void () {
            ret = foo(1*2/(3-a));
            idx = lst[1*2+foo(a)];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(ret), FuncCall(foo, [BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(-, IntegerLit(3), Id(a)))])), AssignStmt(Id(idx), ArrayCell(lst, [BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), FuncCall(foo, [Id(a)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_stmt4(self):
        input = """
        main : function void () {
            ret = foo(1*2/(3-a));
            idx = lst[1*2+foo(a)];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(ret), FuncCall(foo, [BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(-, IntegerLit(3), Id(a)))])), AssignStmt(Id(idx), ArrayCell(lst, [BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), FuncCall(foo, [Id(a)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_stmt5(self):
        input = """
        main : function void () {
            mret = foo(1, "str", foo(3,4,5), {1,2});
            eret = foo();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(mret), FuncCall(foo, [IntegerLit(1), StringLit(str), FuncCall(foo, [IntegerLit(3), IntegerLit(4), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])), AssignStmt(Id(eret), FuncCall(foo, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test_stmt6(self):
        input = """
        main : function void () {
            midx = lst[id[1,2], id[3,4], 5];
            mmidx = lst[lv1[1,2], lv1[3, lv2[4, lv3[5]]]];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(midx), ArrayCell(lst, [ArrayCell(id, [IntegerLit(1), IntegerLit(2)]), ArrayCell(id, [IntegerLit(3), IntegerLit(4)]), IntegerLit(5)])), AssignStmt(Id(mmidx), ArrayCell(lst, [ArrayCell(lv1, [IntegerLit(1), IntegerLit(2)]), ArrayCell(lv1, [IntegerLit(3), ArrayCell(lv2, [IntegerLit(4), ArrayCell(lv3, [IntegerLit(5)])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_stmt7(self):
        input = """
        main : function void () {
            if (a) a=b;
            if (b) {a=b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), AssignStmt(Id(a), Id(b))), IfStmt(Id(b), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_stmt8(self):
        input = """
        main : function void () {
            if (a) a=b; else
            if (b) {a=b;} else {}
            if (b) {} else {}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), AssignStmt(Id(a), Id(b)), IfStmt(Id(b), BlockStmt([AssignStmt(Id(a), Id(b))]), BlockStmt([]))), IfStmt(Id(b), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_stmt9(self):
        input = r"""
        main : function void () {
            if (a*b<c&&!true%2) a=foo(arr[a]);
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, BinExpr(*, Id(a), Id(b)), BinExpr(&&, Id(c), BinExpr(%, UnExpr(!, BooleanLit(True)), IntegerLit(2)))), AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test_stmt10(self):
        input = r"""
        main : function void () {
            if (arr[0]) {
                a=foo(arr[a]);
                return a;
            }
            else continue;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(ArrayCell(arr, [IntegerLit(0)]), BlockStmt([AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])), ReturnStmt(Id(a))]), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_program22(self):
        input = """main: function void() {}
            foo: function string(n: string) {
                a = "abc" + "abc";  
                for (i = 1, i <= 100, i+1) write(testcase);
                a = {a + foo(3),-b,c[0]} + power(-a);
                if (!true && (true && !false + -abc)) return a;
                return {a,-b,b % c};
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, StringType, [Param(n, StringType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, StringLit(abc), StringLit(abc))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(write, Id(testcase))), AssignStmt(Id(a), BinExpr(+, ArrayLit([BinExpr(+, Id(a), FuncCall(foo, [IntegerLit(3)])), UnExpr(-, Id(b)), ArrayCell(c, [IntegerLit(0)])]), FuncCall(power, [UnExpr(-, Id(a))]))), IfStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), BinExpr(&&, BooleanLit(True), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, Id(abc))))), ReturnStmt(Id(a))), ReturnStmt(ArrayLit([Id(a), UnExpr(-, Id(b)), BinExpr(%, Id(b), Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test_stmt11(self):
        input = r"""
        main : function void () {
            if (arr[0]) {
                a=foo(arr[a]);
                return a;
            }
            else {
                a=b;
                b=!false;
                continue;
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(ArrayCell(arr, [IntegerLit(0)]), BlockStmt([AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])), ReturnStmt(Id(a))]), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), UnExpr(!, BooleanLit(False))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test_stmt12(self):
        input = r"""
        main : function void () {
            if (1) {
                if (2)
                    if (3)
                        if (4) {}
                        else return;
            }
            else {
                if (2)
                    if (3)
                    {
                        a=b==c;
                        continue;
                    }
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(IntegerLit(1), BlockStmt([IfStmt(IntegerLit(2), IfStmt(IntegerLit(3), IfStmt(IntegerLit(4), BlockStmt([]), ReturnStmt())))]), BlockStmt([IfStmt(IntegerLit(2), IfStmt(IntegerLit(3), BlockStmt([AssignStmt(Id(a), BinExpr(==, Id(b), Id(c))), ContinueStmt()])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_stmt12b(self):
        input = r"""
        main : function void () {
            for (a=1, 1-2, 2<=2) return;
            for (a=1, 1-2, 2<=2) {}
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(<=, IntegerLit(2), IntegerLit(2)), ReturnStmt()), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(<=, IntegerLit(2), IntegerLit(2)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test_stmt13(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
            {
                b=c;
                continue;
                return;
                return 2*2%2/2;
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), BlockStmt([AssignStmt(Id(b), Id(c)), ContinueStmt(), ReturnStmt(), ReturnStmt(BinExpr(/, BinExpr(%, BinExpr(*, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_stmt14(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_stmt15(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2))), ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test_stmt16(self):
        input = r"""
        main : function void () {
            for (a=1, a!=2, a+1*b) 
                for (b=b, b, b) 
                    for (c=c, c, c) 
                        for (d=d, d, d) continue;   
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(!=, Id(a), IntegerLit(2)), BinExpr(+, Id(a), BinExpr(*, IntegerLit(1), Id(b))), ForStmt(AssignStmt(Id(b), Id(b)), Id(b), Id(b), ForStmt(AssignStmt(Id(c), Id(c)), Id(c), Id(c), ForStmt(AssignStmt(Id(d), Id(d)), Id(d), Id(d), ContinueStmt()))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_stmt16a(self):
        input = """
        main : function void () {
            do{
            
            }
            while (a);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test_stmt17(self):
        input = """
        main : function void () {
            do{
                a=b;
                b = 1*2/3 + 2%22 <1;
                break;
            }
            while ( a==(1<-c) );
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), BinExpr(<, IntegerLit(1), UnExpr(-, Id(c)))), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), BinExpr(<, BinExpr(+, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(%, IntegerLit(2), IntegerLit(22))), IntegerLit(1))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_stmt17a(self):
        input = """
        main : function void () {
            do{
                do{
                    do{
                        return a!=!c;
                    }while (3);
                }
                while (2);
            }
            while (1);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([DoWhileStmt(IntegerLit(2), BlockStmt([DoWhileStmt(IntegerLit(3), BlockStmt([ReturnStmt(BinExpr(!=, Id(a), UnExpr(!, Id(c))))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_stmt18(self):
        input = """
        main : function void () {
            for (a=2, a==b, a+b*2%3)
                continue;
            for (a=2, a==b, a+b*2%3)
            {
                c: integer = true;
                b = (b+1)/2 || c;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), ContinueStmt()), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), BlockStmt([VarDecl(c, IntegerType, BooleanLit(True)), AssignStmt(Id(b), BinExpr(||, BinExpr(/, BinExpr(+, Id(b), IntegerLit(1)), IntegerLit(2)), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_stmt19(self):
        input = """
        main : function void () {
            for (a=2, a==b, a+b*2%3)
                continue;
            for (arr[2_2]=2E-3, arr[2], a+b*2%3)
            {
                c: integer = true;
                b = (b+1)/2 || c;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), ContinueStmt()), ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(22)]), FloatLit(0.002)), ArrayCell(arr, [IntegerLit(2)]), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), BlockStmt([VarDecl(c, IntegerType, BooleanLit(True)), AssignStmt(Id(b), BinExpr(||, BinExpr(/, BinExpr(+, Id(b), IntegerLit(1)), IntegerLit(2)), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_stmt20(self):
        input = """
        main : function void () {
            for (a=a, a||b, !a+b&&2%3)
                for (arr[0]=1_2, arr[1], !true)
                {
                    a = b;
                    for (_0id=1, ("sub"+"\\"expr\\""), a!=false)
                        return;
                }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), Id(a)), BinExpr(||, Id(a), Id(b)), BinExpr(&&, BinExpr(+, UnExpr(!, Id(a)), Id(b)), BinExpr(%, IntegerLit(2), IntegerLit(3))), ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(12)), ArrayCell(arr, [IntegerLit(1)]), UnExpr(!, BooleanLit(True)), BlockStmt([AssignStmt(Id(a), Id(b)), ForStmt(AssignStmt(Id(_0id), IntegerLit(1)), BinExpr(+, StringLit(sub), StringLit(\\"expr\\")), BinExpr(!=, Id(a), BooleanLit(False)), ReturnStmt())])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_call_stmt(self):
        input = """
        main : function void () {
            foo(a*foo("string"/(a-arr[foo()])%2), b, 2_2.E-2);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, Id(a), FuncCall(foo, [BinExpr(%, BinExpr(/, StringLit(string), BinExpr(-, Id(a), ArrayCell(arr, [FuncCall(foo, [])]))), IntegerLit(2))])), Id(b), FloatLit(0.22))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_complex_exp(self):
        input = r"""
        a:auto = -2 / !false :: b<=c || (true!=fal) % 3;
        """
        expect = r"""Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(/, UnExpr(-, IntegerLit(2)), UnExpr(!, BooleanLit(False))), BinExpr(<=, Id(b), BinExpr(||, Id(c), BinExpr(%, BinExpr(!=, BooleanLit(True), Id(fal)), IntegerLit(3))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
       
    def test_complex_exp1(self):
        input = r"""
        a:auto = -2 / (!false :: b<=-c) || (foo()+arr[a]) % -3-2;
        """
        expect = r"""Program([
	VarDecl(a, AutoType, BinExpr(||, BinExpr(/, UnExpr(-, IntegerLit(2)), BinExpr(::, UnExpr(!, BooleanLit(False)), BinExpr(<=, Id(b), UnExpr(-, Id(c))))), BinExpr(-, BinExpr(%, BinExpr(+, FuncCall(foo, []), ArrayCell(arr, [Id(a)])), UnExpr(-, IntegerLit(3))), IntegerLit(2))))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_complex_exp1(self):
        input = r"""
        a:integer = 2--2;
        b:integer = 2-2-2-2--2;
        c:integer = ----2;
        d:integer = 1---2;
        """
        expect = r"""Program([
	VarDecl(a, IntegerType, BinExpr(-, IntegerLit(2), UnExpr(-, IntegerLit(2))))
	VarDecl(b, IntegerType, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(-, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2))))
	VarDecl(c, IntegerType, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(2))))))
	VarDecl(d, IntegerType, BinExpr(-, IntegerLit(1), UnExpr(-, UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_prog(self):
        input = r"""
        main: function void(){
            a: integer = 0; 
            {
                inner = a;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), BlockStmt([AssignStmt(Id(inner), Id(a))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_prog1(self):
        input = r"""
        all: auto;

        foo: function auto (out arr: array[4] of string, incr: integer){
            for (i=0, i<=4, i+1)
                arr[i] = (arr[i]+incr)*(4&&a)%2;
        }

        main: function void(){
            a: integer = 0;
            b: array[1_2] of float = {1.1, .E-3, 1_1_2.002E+2};
            return foo(b, a);
        }
        """
        expect = """Program([
	VarDecl(all, AutoType)
	FuncDecl(foo, AutoType, [OutParam(arr, ArrayType([4], StringType)), Param(incr, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(%, BinExpr(*, BinExpr(+, ArrayCell(arr, [Id(i)]), Id(incr)), BinExpr(&&, IntegerLit(4), Id(a))), IntegerLit(2))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, ArrayType([12], FloatType), ArrayLit([FloatLit(1.1), FloatLit(0.0), FloatLit(11200.2)])), ReturnStmt(FuncCall(foo, [Id(b), Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_prog2(self):
        input = r"""
        count: integer = 0;
        loop_cond: boolean = true; 
        main: function void(){
            while(loop_cond)
                if (count % 12 == 0) continue;
            do{
                // nullable
            } while (count <= true || false);
            return arr[main(foo(arr[main()]))];
        }
        """
        expect = """Program([
	VarDecl(count, IntegerType, IntegerLit(0))
	VarDecl(loop_cond, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(loop_cond), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(12)), IntegerLit(0)), ContinueStmt())), DoWhileStmt(BinExpr(<=, Id(count), BinExpr(||, BooleanLit(True), BooleanLit(False))), BlockStmt([])), ReturnStmt(ArrayCell(arr, [FuncCall(main, [FuncCall(foo, [ArrayCell(arr, [FuncCall(main, [])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_prog3(self):
        input = r"""
        count: integer = 0;
        loop_cond: boolean = true; 
        main: function void(){
            while(loop_cond)
                if (count % 12 == 0)
                    do{
                        for (i=0, i<=4, i+1){
                            if (i%2==0)
                                arr[i] = (arr[i]+incr)*(4&&a)%2;
                            else
                                {
                                    foo("string\"", _0id, "string\t\"");
                                }
                        }
                    } while (count <= true || false);
            return arr[main(foo(arr[main()]))];
        }
        """
        expect = r"""Program([
	VarDecl(count, IntegerType, IntegerLit(0))
	VarDecl(loop_cond, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(loop_cond), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(12)), IntegerLit(0)), DoWhileStmt(BinExpr(<=, Id(count), BinExpr(||, BooleanLit(True), BooleanLit(False))), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(%, BinExpr(*, BinExpr(+, ArrayCell(arr, [Id(i)]), Id(incr)), BinExpr(&&, IntegerLit(4), Id(a))), IntegerLit(2))), BlockStmt([CallStmt(foo, StringLit(string\"), Id(_0id), StringLit(string\t\"))]))]))])))), ReturnStmt(ArrayCell(arr, [FuncCall(main, [FuncCall(foo, [ArrayCell(arr, [FuncCall(main, [])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_prog4(self):
        input = r"""
        // Variable declarations
        a: integer = 1_2_3_4;
        b: float = 1_2_3.0011E+1;
        c: string = "true\"false\n\t\"True\\False";
        d: array[1_2] of boolean = {true, "faLse", a::b, c};
        __01, id_09, True : auto = 1, {1,2,3}, "str\"in\'g";
        //*function decls*//
        
        func: function auto (inherit a:integer, out b: float, inherit out _0c: array[0] of string){
            for (d[foo(arr[0])] = (d[0]*a)/b||c%(!false), "string" != "\"\"", arr[foo(a&&b||c)] )
                foo(arr[0]);
            break;
        }

        /*more function*///*/
        foo: function array[0] of boolean(){
            while (arr[0] <= foo(arr[1_2, func(1.2e+3)]))
                if (count(arr) % (a||b&&c/d) == 0) continue;
                else 
                    if (a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2))))) {
                        arr[1, foo(2), arr[9], 1_2, .e-12] = arr[1, foo(2), arr[9], 1_2, .e-12];
                    }
                    else return func("string\t\"inner\b\f\"\nanother \\ line");
                foo();
        }
        
        main: function void(){
            do{
                for (foo = arr[arr[1,2]], (a&&b+12-!2)/12, 1)
                    if (a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2))))) continue;
                    else break;
                    while (count(arr) % (a||b&&c/d) == 0){
                        //nullable
                    }
            }while(a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2)))));
            return;
        }
        """
        expect = r"""Program([
	VarDecl(a, IntegerType, IntegerLit(1234))
	VarDecl(b, FloatType, FloatLit(1230.011))
	VarDecl(c, StringType, StringLit(true\"false\n\t\"True\\False))
	VarDecl(d, ArrayType([12], BooleanType), ArrayLit([BooleanLit(True), StringLit(faLse), BinExpr(::, Id(a), Id(b)), Id(c)]))
	VarDecl(__01, AutoType, IntegerLit(1))
	VarDecl(id_09, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(True, AutoType, StringLit(str\"in\'g))
	FuncDecl(func, AutoType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(_0c, ArrayType([0], StringType))], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(d, [FuncCall(foo, [ArrayCell(arr, [IntegerLit(0)])])]), BinExpr(||, BinExpr(/, BinExpr(*, ArrayCell(d, [IntegerLit(0)]), Id(a)), Id(b)), BinExpr(%, Id(c), UnExpr(!, BooleanLit(False))))), BinExpr(!=, StringLit(string), StringLit(\"\")), ArrayCell(arr, [FuncCall(foo, [BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c))])]), CallStmt(foo, ArrayCell(arr, [IntegerLit(0)]))), BreakStmt()]))
	FuncDecl(foo, ArrayType([0], BooleanType), [], None, BlockStmt([WhileStmt(BinExpr(<=, ArrayCell(arr, [IntegerLit(0)]), FuncCall(foo, [ArrayCell(arr, [IntegerLit(12), FuncCall(func, [FloatLit(1200.0)])])])), IfStmt(BinExpr(==, BinExpr(%, FuncCall(count, [Id(arr)]), BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(/, Id(c), Id(d)))), IntegerLit(0)), ContinueStmt(), IfStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(1), FuncCall(foo, [IntegerLit(2)]), ArrayCell(arr, [IntegerLit(9)]), IntegerLit(12), FloatLit(0.0)]), ArrayCell(arr, [IntegerLit(1), FuncCall(foo, [IntegerLit(2)]), ArrayCell(arr, [IntegerLit(9)]), IntegerLit(12), FloatLit(0.0)]))]), ReturnStmt(FuncCall(func, [StringLit(string\t\"inner\b\f\"\nanother \\ line)]))))), CallStmt(foo, )]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), BlockStmt([ForStmt(AssignStmt(Id(foo), ArrayCell(arr, [ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])])), BinExpr(/, BinExpr(&&, Id(a), BinExpr(-, BinExpr(+, Id(b), IntegerLit(12)), UnExpr(!, IntegerLit(2)))), IntegerLit(12)), IntegerLit(1), IfStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), ContinueStmt(), BreakStmt())), WhileStmt(BinExpr(==, BinExpr(%, FuncCall(count, [Id(arr)]), BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(/, Id(c), Id(d)))), IntegerLit(0)), BlockStmt([]))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_multi_full_vardecl(self):
        input = """
        x, y: integer = 1*2, 2+3;
        a: string = "abc" :: "def";
        d: integer = a[1+2, 1*5];
        c: string = a(1, f("abc"));
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(d, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
	VarDecl(c, StringType, FuncCall(a, [IntegerLit(1), FuncCall(f, [StringLit(abc)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_ifstmt(self):
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello";
        else a[0] = "in else";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(in else)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_dowhile(self):
        input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(c, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(c), StringLit()), BlockStmt([CallStmt(readString, StringLit(abc)), AssignStmt(Id(c), BinExpr(::, Id(c), StringLit(abc))), CallStmt(printString, Id(c))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_funcdecl_full(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_func_decl_59(self):
        input = """main:function string (){a = 2; b =1; break;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(1)), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_func_decl_60(self):
        input = """main:function string (){a = "hello"; b = 1; c = 0.123; d = f; e = foo(); f = false; return 1_2;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(hello)), AssignStmt(Id(b), IntegerLit(1)), AssignStmt(Id(c), FloatLit(0.123)), AssignStmt(Id(d), Id(f)), AssignStmt(Id(e), FuncCall(foo, [])), AssignStmt(Id(f), BooleanLit(False)), ReturnStmt(IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_func_decl_61(self):
        input = """main:function string (){return foo(1 - 2, a, "True");}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, [BinExpr(-, IntegerLit(1), IntegerLit(2)), Id(a), StringLit(True)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_func_decl_62(self):
        input = """main: function void() {
                x,y,z: integer = 1,2,{1,2,2};
                {a=3;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(2)])), BlockStmt([AssignStmt(Id(a), IntegerLit(3))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_func_decl_63(self):
        input = """main: function void() {
                if(a==1) a=1;
                if(a==1) a=2; else a=3;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_func_decl_64(self):
        input = """main: function void() {
                if(a==1) a=2; 
                else {
                        a=3;
                        if (a==4) a = 1;
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), IntegerLit(3)), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), AssignStmt(Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_func_decl_65(self):
        input = """main: function void() {
                a: auto = -var[a||3==b*!-g[12]];
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, UnExpr(-, ArrayCell(var, [BinExpr(==, BinExpr(||, Id(a), IntegerLit(3)), BinExpr(*, Id(b), UnExpr(!, UnExpr(-, ArrayCell(g, [IntegerLit(12)])))))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_func_decl_66(self):
        input = """main: function void() {
                a: auto = a/a==b/b-((asdf)::(asdf));
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(==, BinExpr(/, Id(a), Id(a)), BinExpr(-, BinExpr(/, Id(b), Id(b)), BinExpr(::, Id(asdf), Id(asdf)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_func_decl_67(self):
        input = """main: function void() {
                a = (a < b) < (c < d);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<, BinExpr(<, Id(a), Id(b)), BinExpr(<, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_func_decl_68(self):
        input = """main: function void() {
                a = (a > (b > c)) > d;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(>, Id(a), BinExpr(>, Id(b), Id(c))), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_func_decl_69(self):
        input = """main: function void () {}
            sum: function auto () {}
            _VAR1: integer;
            _VAR2: string = "string";"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(sum, AutoType, [], None, BlockStmt([]))\n\tVarDecl(_VAR1, IntegerType)\n\tVarDecl(_VAR2, StringType, StringLit(string))\n])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_func_decl_70(self):
        input = """main: function void() {
                while(123123){
                    if(you==me) print("hell no man");
                    else if(you==him) print("maybe");
                    else print("this is ok now");
                }
            }"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(IntegerLit(123123), BlockStmt([IfStmt(BinExpr(==, Id(you), Id(me)), CallStmt(print, StringLit(hell no man)), IfStmt(BinExpr(==, Id(you), Id(him)), CallStmt(print, StringLit(maybe)), CallStmt(print, StringLit(this is ok now))))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_func_decl_58(self):
        input = """main:function string (){}
        main:function string (){}
        main:function string (){}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([]))
	FuncDecl(main, StringType, [], None, BlockStmt([]))
	FuncDecl(main, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_95(self):
        input ="""main: function void() {
                a: boolean = 2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))

    def test_96(self):
        input = """
            main: function boolean () {}
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(var, StringType, BinExpr(::, StringLit(hello), StringLit(world)))]), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))