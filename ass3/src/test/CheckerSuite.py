import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """
        bar1: function void (c: integer) inherit bar
        {
            super(d, c);
        }
        bar: function void (a: integer, inherit d: auto) {
        
        }
        bar2: function void (x: integer) inherit bar1
        {
            super(d);
        }
        main: function void() {
        
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
        x: integer = bar(1, 2) + 1;
        bar: function auto (m: auto, n: auto)
        {
            return m + n;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """p, q, r: string = \"20\", \"30\", \"40\";
        main: function void()
        {
            s = q :: (p :: r);
            printString(s);
        }"""
        expect = "Undeclared Identifier: s"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """y: integer = 65;
        factorial: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * factorial(n - 1);
        }
        increment: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta_value: integer = factorial(3);
            increment(y, delta_value);
            printInteger(y);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
        bar: function integer (inherit m: integer, n: integer)
        {
            
        }
        bar1: function integer(o: string) inherit bar
        {
            super(m, n);
        }
        main: function void() {
        
        }"""
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """a, b: boolean = true, bar(1, 2);
        bar: function auto (x: auto, y: integer)
        {
            return x == y;
        }
        baz: function void(z: auto)
        {
            
        }
        main: function void() {
            baz(2022);
            baz(3.75);
        }"""
        expect = "Type mismatch in statement: CallStmt(baz, FloatLit(3.75))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
        bar: function auto (m: auto, n: integer)
        {
            m = m + n;
            return m;
        }
        main: function void() {
            x: integer = bar(1, 2);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
        bar: function auto (p: auto, q: integer)
        {
            p = p + q;
            return p;
        }
        baz: function void()
        {
            y: integer = bar(2.5, 3);
        }
        main: function void() {
        
        }"""
        expect = "Type mismatch in expression: FuncCall(bar, [FloatLit(2.5), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
        bar: function auto (u: auto, v: integer)
        {
            u = u + v;
            return u;
        }
        baz: function void() inherit bar
        {
            u: integer = 1;
            super(2, 3);
        }
        main: function void() {
        
        }"""
        expect = "Invalid statement in function: baz"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
        increase : function void (out n : integer, a: float) inherit bar {} 
        bar : function auto (inherit m: float, n: integer){} 
        main: function void()
        {
        
        }"""
        expect = "Invalid statement in function: increase"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
        bar: function void (inherit m: integer) inherit baz {}
        main: function void()
        {
        
        }"""
        expect = "Undeclared Function: baz"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
        bar: function void() inherit bar1{
            super("University", true);
        }
        bar1: function void (inherit y: string, inherit y: boolean) {}
        main: function void() {}"""
        expect = "Redeclared Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
        bar: function integer() {
            bar: integer = 2022;
        }
        main: function void() {
            bar: integer = bar();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
        bar: function auto (m: auto, n: integer)
        {
            return m + n;
        }
        p: integer = bar(1, 2) + 1;
        main: function void() {
            p = bar(1.2, 3);
        }"""
        expect = "Type mismatch in expression: FuncCall(bar, [FloatLit(1.2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
        y: auto = 5.6;
        bar: function void(b: integer) {}
        main: function void() {
            bar(y);
        }"""
        expect = "Type mismatch in statement: CallStmt(bar, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
        bar: function void(b: integer) {}
        baa: integer = 3;
        main: function void() {
        
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
        bar: function void (b: integer) inherit c {
            preventDefault();
        }
        c: function string (inherit d: string) {}
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
        bar: function auto (n: integer) {
            if (n < 10)
            {
                return n;
            }
            else
            {
                return 5.75;
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(5.75))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        func2: function auto(){
            return "abc";
        }
        main: function void(){
            b: auto = func2() + 3.3;
        }
        
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(func2, []), FloatLit(3.3))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
        main: function void(){
            b: integer = func2() + 3;
        }
        func2: function auto() inherit bar {
            return 1;
        }
        bar: function integer(){
            return 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        func2: function auto() inherit bar {
            super(30);
            y: integer = 30;
        }
        bar: function integer(inherit y: integer) {
            
        }
        main: function void(){
            b: integer = func2() + 3;
        }"""
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        func2: function auto(c: integer) inherit bar {
            super(30);
            return c;
        }
        bar: function integer(inherit y: integer) {
            
        }
        main: function void(){
            b: integer = func2() + 3;
        }"""
        expect = "Type mismatch in expression: FuncCall(func2, [])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        factorial: function integer (m: integer) {
            factorial(2022);
        }
        main: function void() {
            delta_value: integer = factorial(4);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
        factorial: function integer (m: integer) {
            if (m <= 1)
            {
                return 1;
            }
            return factorial(m - 1) + factorial(m - 2);
        }
        main: function void() {
            delta_value: integer = factorial(4);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
        bar: function auto () {
            return 2022;
        }
        main: function void() {
            delta_value: integer = bar();
            printInteger(delta_value);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
        z: boolean = true;
        bar: function auto () {
            return z;
        }
        main: function void() {
            delta_value: integer = bar();
            printInteger(delta_value);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(delta_value, IntegerType, FuncCall(bar, []))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_case_426 (self):
        input = """
        z: boolean = true;
        bar: function auto () {
            return z;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_case_427 (self):
        input = """
        z: integer = 3;
        b: integer = readInteger();
        factorial: function integer() 
        {
            
        }
        bar: function auto () {
            return b;
        }
        main: function void() {
            z = bar();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_case_428 (self):
        input = """
        bar : function void (b : auto){}                  // Line 1
        main : function void () {
            bar(true);                                    // Line 3
            baz();                                        // Line 4
        }
        baz : function void (){                           // Line 6                    
            bar(3);                                       // Line 7
        } """
        expect = "Type mismatch in statement: CallStmt(bar, IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_case_429 (self):
        input = """
        bar: function void (b : auto) {}
        main: function void () {
            bar(2018);
            baz();
        }
        baz: function void (){                    
            bar(3);
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_case_430 (self):
        input = """
        bar: function void (b: auto) inherit baz {
            preventDefault();
        }
        main: function void () {
            bar(2018);
            baz(20);
        }
        baz: function void (inherit b: integer){                 
            bar(3);
        } """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_case_431 (self):
        input = """
        bar: function void (b: auto) inherit baz {
            preventDefault();
            c = c + 1;
        }
        main: function void () {
            bar(2018);
            baz(20, 1998);
        }
        baz: function void (inherit b: integer, inherit c: integer){                 
            bar(3);
        } """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_case_432 (self):
        input = """
        x: array [3, 2] of integer = {{1, "2"}, {1, 2}, {1, 2}};
        main: function void () {
            
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_case_433 (self):
        input = """
        bar: function integer(b: auto)
        {
            if (b < 20)
            {
                return 1;
            }
            return 2.7;
        }
        main: function void () {
            
        }"""
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(2.7))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_case_434 (self):
        input = """
        bar: function integer(b: auto) inherit bar1
        {
            preventDefault();
            if (b < 20)
            {
                y: integer = 5;
                return y;
            }
            return 3;
        }
        bar1: function integer(inherit y: integer)
        {
            preventDefault();
        }
        main: function void () {
            
        }"""
        expect = "Invalid statement in function: bar1"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_case_435 (self):
        input = """
        bar: function integer(b: auto) inherit bar1
        {
            preventDefault();
            y: integer = 20;
            if (b < 20)
            {
                y: integer = 5;
                return y;
            }
            return y;
        }
        bar1: function integer(inherit y: integer)
        {
            
        }
        main: function void () {
            
        }"""
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_case_436 (self):
        input = """
        main : function void() inherit bar {
            super(1.0, 2.0, 3.0);
        }
        bar : function auto(inherit y: string, inherit z: auto, x: auto){
            return y + x + z;
        }"""
        expect = "Type mismatch in statement: CallStmt(super, FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_case_437 (self):
        input = """
        main:function void() inherit bar {
            super(12);
            y:auto = bar(1);
            bar2();
            arr: array[2,2] of integer = {{1, 2.7}, {1,2}};
            arr[1,2] = 1;
        }
        bar:function float (y: integer){
            return y + 1.2;
        }
        bar2: function void(){}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), FloatLit(2.7)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_case_438 (self):
        input = """
        bar : function void() {}
        bar : function auto ( b : integer , c : integer ) inherit baz {}
        main: function void() {}"""
        expect = "Redeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_case_439 (self):
        input = """
        y: auto = bar(1, 2);
        bar: function auto() { }
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(bar, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_case_440 (self):
        input = """
        z: auto = {4,5,6};
        y: auto = z[1,2];
        main: function void() {}"""
        expect = "Type mismatch in expression: ArrayCell(z, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_case_441 (self):
        input = """
        bar: function float (out z: auto, y: auto)
        {
            z = 5;
            return z + y;
        }
        main: function void() {
            b: auto = bar(2.0, 2);
            c: float = b + z;
        }"""
        expect = "Type mismatch in expression: FuncCall(bar, [FloatLit(2.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_case_442 (self):
        input = """
        bar: function boolean (n: integer)
        {
            y: float;
            i: integer;
            if (n < 2)
            {
                return false;
            }
            if (n % 2 == 0)
            {
                return n == 2;
            }

            for (i = 2, i * i <= n, 1)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        main: function void() {
            n: integer = readInteger();
            printBoolean(bar(n));
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_case_443 (self):
        input = """
        main: function void() {
            n: integer = readInteger();
            printBoolean(bar(n));
        }
        bar: function void(n: integer) {}"""
        expect = "Type mismatch in statement: CallStmt(printBoolean, FuncCall(bar, [Id(n)]))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_case_444 (self):
        input = """
        main: function void() {
            n: integer = readInteger();
            if (bar(n))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        bar: function boolean(n: integer) {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_case_445 (self):
        input = """
        main: function void() {
            n: float = readInteger();
            if (bar(n) && bar(n + 1))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        bar: function boolean(n: float) {}"""
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_case_446 (self):
        input = """
        bar: function auto(b: auto, c: string) inherit baz {
            super(1, b, baz()); // 1
        }
        baz: function auto (y: auto, z: boolean, x: float) {}
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(baz, [])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_case_447 (self):
        input = """
        bar: integer = 2018;
        bar1: function auto()
        {
            return bar;
        }
        main: function void()
        {
            bar: auto = bar1();
            printBoolean(bar);
        }"""
        expect = "Type mismatch in statement: CallStmt(printBoolean, Id(bar))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_case_448(self):
        input = """y, z, x: integer = 20, 30, 40;
        main: function void()
        {
            y = z + x;
            printInteger(y);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_case_449(self):
        input = """y, z, x: float = 2.75, 1.98, 3.17;
        main: function void()
        {
            r = y + z + x;
            printFloat(r);
        }"""
        expect = """Undeclared Identifier: r"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_case_450(self):
        input = """y, z: string = "Baba", "Mama";
        main: function void()
        {
            x = z :: y;
            r = (x :: z) :: y;
            w = x :: (z :: y);
            printString(r);
            printString(w);
        }"""
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_case_451(self):
        input = """main: function void(){
                a[3 + 5, 2 * x] = y[4] - 7;
                return;
            }"""
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_case_452(self):
        input = """
            a: integer = 20;
            b: function void() {
                x: integer = 3;
            }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_case_453(self):
        input = """main: function void(){
                i: integer = 3;
                do
                {
                    i = i + 1;
                }   
                while (i < 200);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_case_454(self):
        input = """main: function void(){
                i: integer = 3;
                do {
                    i = i + 1;
                } while (i < 20);
                printInteger(i);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_case_455(self):
        input = """a: array[3] of integer = {1, 2, 3};
            main: function void() {
                
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_case_456(self):
        input = """foo: function void () inherit bar {
                if (a < b)
                    if (c < d)
                        printString("True");
                    else
                        printString("False");
            }
            main: function void() {}
            bar: integer = 2;"""
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_case_457(self):
        input = """main: function auto () { return; }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_case_458(self):
        input = """x: integer = 2018;
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            decr: function void(out n: integer, delta: integer) {
                n = n - delta;
            }
            main: function void() {
                delta: integer = fact(3_2);
                decr(x, delta);
                printInteger(x);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_case_459(self):
        input = """main: function void () {
                a: array [2, 2] of float;
                i, j: integer;
                for (i = 0, i < 2, i + 1) {
                    for (j = 0, j < 2, j + 1) {
                        a[i, j] = readFloat();
                    }
                }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_case_460(self):
        input = """main: function void () {
                a: array [2, 2] of float;
                i, j: integer;
                for (i = 0, i < 2, i + 1) {
                    for (j = 0, j < 2, j + 1) {
                        a[i, j] = readFloat();
                    }
                }
                for (i = 0, i < 2, i + 1) {
                    for (j = 0, j < 2, j + 1) {
                        printFloat(a[i, j]);
                    }
                }
            }"""
        expect = "Undeclared Function: printFloat"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_case_461(self):
        input = """x: integer = 2018;
            fibo: function integer (n: integer) {
                if (n <= 1) return 1;
                else return fibo(n - 1) + fibo(n - 2);
            }
            decr: function void(out n: integer, delta: integer) {
                n = n - delta;
            }
            main: function void() {
                delta: integer = fibo(100);
                decr(x, delta);
                printInteger(x);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_case_462(self):
        input = """main: function void() {
                a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
                return;
            }"""
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_case_463(self):
        input = """a: integer = foo();
            foo: function string() { }
            main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_case_464(self):
        input = """a : integer = foo(1, 2);
            foo : function integer (a : auto, b: auto) {
                a = 1;
                b = 2;
                return a + b;
            }
            main: function void() {}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_case_465(self):
        input = """a : integer = foo(1, 2);
            foo : function integer (a : auto, b: auto) {
                x: auto = a + b;
                return x;
            }
            main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_case_466(self):
        input = """a: auto;
            main: function void() {}"""
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_case_467(self):
        input = """x: integer;
            y: float;
            z: boolean;
            goo: function void(x: integer, y: float) {
            
            }
            t: array[10] of float;
            foo: function auto() {
                
            }
            a: string = \"Hello World\";"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_case_468(self):
        input = """
            x: array [1,1,2] of integer = {{{1, 2, 3}, {4, 5, 6}}};
            y: auto = x[0, 1+1-0, 1];
            main: function void() {
                
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_case_469(self):
        input = """
            goo: function void(a: auto, b: auto)
            {
                x: string = a + b;
            }
            main: function void() {}
            foo1: function void(inherit out a: integer) inherit foo {
                super(x, y, z);
            }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_case_470(self):
        input = """foo: function integer () {return 1;}
            x: array [1,1,2] of integer = {{{1, 2, 3}, {4, 5, 6}}};
            y: auto = x[1, foo(),3];"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_case_471(self):
        input = """x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
            y: auto = x[2 < 3];
            main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(x, [BinExpr(<, IntegerLit(2), IntegerLit(3))])"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_case_472(self):
        input = """
            a: function integer (a: integer)
            {
                if (a <= 1)
                {
                    return a;
                }
                return a(a - 1) + a(a - 2);
            }
            main: function void()
            {
                printInteger(a(2018));
            }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_case_473(self):
        input = """
            a: float = foo(1, 2) + 1.5;
            foo: function auto(a: integer, b: integer) {
                return a + b; 
            }
            main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_case_474(self):
        input = """
            main: function void () {
                a: integer = foo();//1
                b: float = "Error";//2
            }
            foo: function auto() {
                c: string = "Error";//3
                if("Error")//4
                    return 123;//5
                else
                    return 456;//6
                return "123"; //7
            }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, StringLit(Error))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_case_475(self):
        input = """
            func1: function auto (d: integer, c: integer, e: auto) {
                g: integer = -e;
                f: integer = e;
            }
            main: function void () {
                a: integer = func1(2, 3, 2.9);
            }"""
        expect = """Type mismatch in expression: FuncCall(func1, [IntegerLit(2), IntegerLit(3), FloatLit(2.9)])"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_case_476(self):
        input = """foo: function void(b: auto, c: auto)
            {
                a: integer = b + c == c;
            }
            main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, BinExpr(+, Id(b), Id(c)), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_case_477(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
                printInteger(a + 2 * b + 3 * c);
            }
            main: function void() {
                foo(2, 3, 4);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_case_478(self):
        input = """foo: function void (a: integer, b: integer) {
                c: integer = 2018;
                printInteger(a + 2 * b + 3 * c);
            }
            main: function void() {
                foo(2, 3);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_case_479(self):
        input = """
            foo: function auto (b: integer, b: float) { 
                return 3;
                return "hello";
                a: string = 123;
            }
            main: function void() {}"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_case_480(self):
        input = """foo: function void (a: integer, b: integer) {
            i: integer;
            for (i = a, i <= b, i + 1) {
                c: integer = a + i;
                printInteger(c);
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_case_481(self):
        input = """foo: function void () {
            do
            {
                printInteger(1);
            }   
            while (true);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_case_482(self):
        input = """foo: function void () {
            while (true)
                break;
            return;
        }
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_case_483(self):
        input = """foo: function void () {
            if (true) {
                if (!true) {
                    
                }
                else return;
            }
            return;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_case_484(self):
        input = """foo: function void () {
            if (!true) {
                if (true) {
                    a: integer = 10;
                    a = a + 1;
                    return;
                }
                else
                    return;
            }
            else {
                a: integer = 1;
                while (a < 20)
                    a = a + 1;
                printInteger(a);
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_case_485(self):
        input = """foo: function array [10] of integer(a: array [10] of integer) {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                a[i] = a[i] * 2 + 1;
            }
            return a;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_case_486(self):
        input = """foo: function void (out N: integer, i: integer) {
            j: integer;
            for (j = 0, j < i, j + 1) {
                if (N % j == 0) {
                    N = N - j;
                }
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_case_487(self):
        input = """foo1: function void (out N: integer, i: integer) {
            N = N * i;
        }
        main: function void() {
            N: integer = 2018;
            foo1(N, 3);
            printInteger(N);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_case_488(self):
        input = """foo1: function void (out s: string, N: integer) {
            i: integer;
            for (i = 0, i < N, i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])"""
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_case_489(self):
        input = """
        inc : function void (a : integer) inherit foo{
            a = 1;
        }
        foo : function auto (inherit n: float, inherit n: integer){
        }
        main: function void() {
        }"""
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_case_490(self):
        input = """
        test1 : function string(y : auto) {
            y = 2; // line 2
            return "";
        }
        main: function void () {
            x: string = test1(true); // line 6
        }"""
        expect = """Type mismatch in expression: FuncCall(test1, [BooleanLit(True)])"""
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_case_491(self):
        input = """foo: function boolean (inherit out a: integer, b: float) inherit goo {}
        main: function void() {}"""
        expect = """Undeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_case_492(self):
        input = """foo: function boolean (a: integer, b: float) {
            i: integer;
            for (i = 0, i < 5, i + 1) {
                x, y, z: integer = 10, 20, 30;
                return (x + a + y + b) > (y + a + z + b);
            }
        }
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_case_493(self):
        input = """foo1: function void (a: integer, b: float) {
            c: float = a + b;
            writeFloat(c);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_case_494(self):
        input = """foo2: function void (a: integer) {
            printString(\"Test\");
            a = a + 1;
            printInteger(a);
        }
        main: function void() {
            foo2(10);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_case_495(self):
        input = """a,b,c: boolean = true, false, true;
        main: function void() {
            a = b && c;
            printBoolean(a);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_case_496(self):
        input = """foo: function void() {
            if (true)
            {
                a, b, c: integer = 10, 20, 30;
                printInteger(a + b + c);
            }
            else
            {
                x, y: float = 2.3e2, -2.3e2;
                writeFloat(x + y);
            }   
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_case_497(self):
        input = """a_20: boolean = (2 < 3) < 4;
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<, BinExpr(<, IntegerLit(2), IntegerLit(3)), IntegerLit(4))"""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_case_498(self):
        input = """foo: function string (a: string, b: integer) {
            return (a :: a[b]);
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(a, [Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_case_499(self):
        input = """x: integer = 65;
        y: function integer(x: integer) {
            return x + 1;
        }
        z: float = 65.20;
        t: function float(z: float) {
            return z * 2.0;
        }
        main: function void() {
            y: integer = y(x);
            t: float = t(z);
            printInteger(y);
            writeFloat(t);
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 499))
