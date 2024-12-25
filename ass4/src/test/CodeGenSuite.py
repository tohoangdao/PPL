import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = """main:function void() {
            printString(\"abc\");
        }"""
        output = """abc
"""
        self.assertTrue(TestCodeGen.test(input, output, 500))

    def test_1(self):
        input = """main:function void() {
            printInteger(1411);
        }"""
        output = """1411
"""
        self.assertTrue(TestCodeGen.test(input, output, 501))
    
    def test_2(self):
        input = """main:function void() {
            printString("string");
        }"""
        output = """string
"""
        self.assertTrue(TestCodeGen.test(input, output, 502))
        
    def test_3(self):
        input = """main:function void() {
            printInteger(123456);
        }"""
        output = """123456
"""
        self.assertTrue(TestCodeGen.test(input, output, 503))
    
    def test_4(self):
        input = """
        num:integer;
        main:function void() {
            num:integer = 400;
            printInteger(num);
        }"""
        output = """400
"""
        self.assertTrue(TestCodeGen.test(input, output, 504))
        
    def test_5(self):
        input = """
        //num:integer = 1;
        num:arranum2 [4] of integer = {10,20,30,40};
        main:function void() {
            i:integer;
            for (i = 0, i < 4, 1) {
                printInteger(num[i]);
            }
        }"""
        output = """10\n20\n30\n40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 505))
    
    def test_6(self):
        input = """
        //str:string = "abc" :: "123";
        
        main:function void() {
            str:string;
            str = "abc" :: "123" :: "ehe";
            printString(str);
        }"""
        output = """abc123ehe
"""
        self.assertTrue(TestCodeGen.test(input, output, 506))
        
    def test_7(self):
        input = """
        main:function void() {
            printInteger(12301%162);
        }"""
        output = """151
"""
        self.assertTrue(TestCodeGen.test(input, output, 507))
    
    def test_8(self):
        input = """
        main:function void() {
            printFloat(12412/523);
        }"""
        output = """23.732313
"""
        self.assertTrue(TestCodeGen.test(input, output, 508))
        
    def test_9(self):
        input = """
        main:function void() {
            
            printBoolean(!false);
        }"""
        output = """true
"""
        self.assertTrue(TestCodeGen.test(input, output, 509))
    
    def test_10(self):
        input = """
        main:function void() {
            num:integer = 1;
            while (true) {
                num = num + 1;
                if (num == 10) break;
            }
            printInteger(num);
        }"""
        output = """10
"""
        self.assertTrue(TestCodeGen.test(input, output, 510))
        
    def test_11(self):
        input = """
        main:function void() {
            num:integer = 1;
            do {
                num = num + 1;
            } while(num < 10);
            printInteger(num);
        }"""
        output = """10
"""
        self.assertTrue(TestCodeGen.test(input, output, 511))
    
    def test_12(self):
        input = """
        main:function void() {
            num,i:integer = 1, 0;
            for (i = 1, i < 100, 1) num = num + 1;
            printInteger(num);
        }"""
        output = """100
"""
        self.assertTrue(TestCodeGen.test(input, output, 512))
    
    def test_13(self):
        input = """
        num:integer;
        main:function void() {
            num = 123;
            printInteger(num);
        }"""
        output = """123
"""
        self.assertTrue(TestCodeGen.test(input, output, 513))
    
    def test_14(self):
        input = """
        num:arranum2 [4] of integer;
        main:function void() {
            num[0] = 10;
            num[1] = 20;
            num[2] = 30;
            num[3] = 40;
            i: integer;
            for (i = 0, i < 4, 1) {
                printFloat(num[i]);
            }
        }"""
        output = """10.0\n20.0\n30.0\n40.0\n"""
        self.assertTrue(TestCodeGen.test(input, output, 514))
        
    def test_15(self):
        input = """
        num:arranum2 [4] of integer;
        main:function void() {
            num[0] = 10;
            num[1] = 20;
            num[2] = 30;
            num[3] = 40;
            i: integer = num[0];
            printInteger(i);
            for (i = 0, i < 4, 1) {
                printInteger(num[i]);
            }
        }"""
        output = """10\n10\n20\n30\n40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 515))
        
    def test_16(self):
        input = """
        self:function float(num:float) {
            return num;
        }
        main:function void() {
            printFloat(self(10));
        }"""
        output = """10.0\n"""
        self.assertTrue(TestCodeGen.test(input, output, 516))
    
    def test_17(self):
        input = """
        num:auto = 10;
        main:function void() {
            printInteger(num);
        }"""
        output = """10\n"""
        self.assertTrue(TestCodeGen.test(input, output, 517))

    def test_18(self):
        input = """
        num:arranum2[2,2] of integer;
        main:function void() {
            i,j:integer;
            for (i = 0, i < 2, 1) {
                for (j = 0, j < 2, 1) {
                    num[i,j] = 4;
                }
            }
            printInteger(num[1,1]);
        }"""
        output = """4\n"""
        self.assertTrue(TestCodeGen.test(input, output, 518))
    
    def test_19(self):
        input = """
        main:function void() {
            i,j:integer;
            num:arranum2[2] of integer = {10,40};
            
            printInteger(num[1]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 519))
    
    def test_20(self):
        input = """
        main:function void() {
            num:integer;
            for (num = 1, num < 15, 1) continue;    
            printInteger(num);
        }"""
        output = """15\n"""
        self.assertTrue(TestCodeGen.test(input, output, 520))
    def test_21(self):
        input = """
        main:function void() {
            arr:arranum2[1,1,1,1] of integer = {{{{40}}}};
            
            printInteger(arr[0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 521))
    
    def test_22(self):
        input = """
        main:function void() {
            arr:arranum2[1,1,1,1,1] of integer = {{{{{40}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 522))
    
    def test_23(self):
        input = """
        main:function void() {
            arr:arranum2[1,1,1,1,1] of integer = {{{{{40}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 523))
        
    def test_24(self):
        input = """
        main:function void() {
            arr:arranum2[1,1,1,1,2] of integer = {{{{{40,50}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 524))
        
    def test_25(self):
        input = """
        main:function void() {
            arr:arranum2[1,1,1,2,2] of integer = {{{{{40,50},{60,70}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 525))
    
    def test_26(self):
        input = """
        arr:arranum2[1,1,1,2,2] of integer = {{{{{40,50},{60,70}}}}};
        
        main:function void() {
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 526))
        
    def test_27(self):
        input = """
        FactorialRecursive:function integer(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:integer = 10;
            printInteger(FactorialRecursive(num));
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 527))
        
    def test_28(self):
        input = """
        FactorialRecursive:function integer(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:auto = 10;
            printInteger(FactorialRecursive(num));
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 528))\
    
    def test_29(self):
        input = """
        num:auto = 10;
        
        main:function void() {
            printInteger(FactorialRecursive(num));
        }
        FactorialRecursive:function integer(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 529))
    
    def test_30(self):
        input = """
        
        FactorialRecursive:function integer(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:auto = 10;
            printInteger(FactorialRecursive(num));
        }
        num:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 530))
                
    def test_31(self):
        input = """
        
        FactorialRecursive:function integer(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:auto = 10;
            printInteger(FactorialRecursive(num));
        }
        num:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 531))
    
                        
    def test_32(self):
        input = """
        
        isLeapnum2ear: function boolean(num2ear:integer) {
return (num2ear % 4 == 0) && ((num2ear % 100 != 0) || (num2ear % 400 == 0));
}     
main:function void() {
isLeapnum2ear:integer = 2020;
printBoolean(isLeapnum2ear(isLeapnum2ear));
}          
        """
        output = """true\n"""
        self.assertTrue(TestCodeGen.test(input, output, 532))
    def test_32(self):
        input = """
//danum2s: integer = readInteger();
danum2s:integer = 10;
Danum2OfWeek: function string(danum2:integer) {
if (danum2 == 0) return "Sundanum2";
else if (danum2 == 1) return "Mondanum2";
else if (danum2 == 2) return "Tuesdanum2";
else if (danum2 == 3) return "Wednesdanum2";
else if (danum2 == 4) return "Thursdanum2";
else if (danum2 == 5) return "Fridanum2";
else if (danum2 == 6) return "Saturdanum2";
return "Wrong danum2 range";
}
main:function void() {
printString(Danum2OfWeek(danum2s));
}         
        """
        output = """Wrong danum2 range\n"""
        self.assertTrue(TestCodeGen.test(input, output, 532))
    
    def test_33(self):
        input = """
    num: integer = 65;
    fact: function integer (n: integer) {
        if (n == 0) return 1;
        else return n * fact(n - 1);
    }
    inc: function void(out n: integer, delta: integer) {
        n = n + delta;
    }
    main: function void() {
        delta: integer = fact(3);
        inc(num, delta);
        printInteger(num);
    }       
        """
        output = """71\n"""
        self.assertTrue(TestCodeGen.test(input, output, 533))
        
    def test_34(self):
        input = """
    main: function void() {
        i: integer;
        for (i = 1, i < 10, 1) {
            if (i % 2 == 0) continue;
            printInteger(i); 
        }
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 534))
        
    def test_35(self):
        input = """
    main: function void() {
        i: integer = 0;
        while (i < 10) {
            i = i + 1; 
            if (i % 2 == 0) continue;
            printInteger(i);
        }
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 535))
    
    def test_36(self):
        input = """
    main: function void() {
        i: integer = 0;
        do {
            i = i + 1; 
            if (i % 2 == 0) continue;
            printInteger(i);
        } while (i < 10);
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 536))
    
    def test_37(self):
        input = """
    foo:function auto(a:integer){
        return a;
    }    
    main:function void() {
        printInteger(foo(10));
    }
        """
        output = """10\n"""
        self.assertTrue(TestCodeGen.test(input, output, 537))
        
    def test_38(self):
        input = """
        
        FactorialRecursive:function auto(num:integer){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:auto = 10;
            printInteger(FactorialRecursive(num));
        }
        num:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 538))
    
    def test_39(self):
        input = """
        
        FactorialRecursive:function integer(num:auto){
            if (num == 1) return 1;
            return FactorialRecursive(num-1)*num;
        }
        main:function void() {
            num:auto = 10;
            printInteger(FactorialRecursive(num));
        }
        num:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 539))
    def test_540(self):
        input = """
        foo: function void(out num1: auto, out num2: auto)
        {
            num1 = num1 + 1;
            num2 = num2 + 1;
            printFloat(num1 + num2);
        }
        main: function void()
        {
            a, b: float = 1.0, 2.0;
            foo(a, b);
            printFloat(a);
            printFloat(b);
        }"""
        output = "5.0\n2.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, output, 540))
    def test_541(self):
        input = """
        foo: function void(out a: integer, out b: integer, c: integer)
        {
            b = b + 5;
            b = a + c + 4;
            printInteger(a);
            printInteger(b);
            printInteger(c);
        }
        main: function void()
        {
            j, k: integer = 10, 15;
            foo(j, j, j + k);
            printInteger(j);
            printInteger(k);
        }"""
        output = "10\n39\n25\n39\n15\n"
        self.assertTrue(TestCodeGen.test(input, output, 541))
    def test_542 (self):
        input = """
        a: integer = foo(1, 2) + 1;
        foo: function integer(a: integer, b: integer)
        {
            return a + b;
        }
        main: function void()
        {
            printInteger(a);
        }"""
        output = "4\n"
        self.assertTrue(TestCodeGen.test(input, output, 542))
    def test_543 (self):
        input = """
        a: integer = foo(1, 2) + 1;
        foo: function auto(a: auto, b: auto)
        {
            return a + b;
        }
        main: function void()
        {
            b: integer = foo(a, a + 1);
            printInteger(a);
            printInteger(b);
        }"""
        output = "4\n9\n"
        self.assertTrue(TestCodeGen.test(input, output, 543))
    def test_544 (self):
        input = """
        foo: function void (inherit out a: integer)
        {
            if (a % 2 == 1)
            {
                a = 3 * a + 1;
            }
            else
            {
                a = a / 2;
            }
        }
        bar: function integer(out b: integer) inherit foo
        {
            super(b);
            return a + b;
        }
        main: function void()
        {
            b: integer = 27;
            printInteger(bar(b));
        }"""
        output = "164\n"
        self.assertTrue(TestCodeGen.test(input, output, 544))
    def test_545 (self):
        input = """
        a: integer = 3;
        b: integer = 4;
        c: boolean = a * a + b * b == 25;
        main: function void()
        {
            printBoolean(c);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 545))
    def test_546 (self):
        input = """
        a: integer = readInteger(); // Input 3
        b: integer = readInteger(); // Input 0
        c: boolean = (b == 0) || (a / b >= 0);
        main: function void()
        {
            printBoolean(c);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 546))
    def test_547 (self):
        input = """
        a: integer = readInteger(); // Input 3
        b: integer = readInteger(); // Input 10
        c: boolean = (b < 0) && (a * b >= 0);
        main: function void()
        {
            printBoolean(c);
        }"""
        output = "false\n"
        self.assertTrue(TestCodeGen.test(input, output, 547))
    def test_548 (self):
        input = """
        foo: function boolean(a: boolean, b: boolean)
        {
            return (a && b) || (a || b);
        }
        main: function void()
        {
            a, b: boolean = readBoolean(), readBoolean(); // Input false, false
            printBoolean(foo(a, b));
        }"""
        output = "false\n"
        self.assertTrue(TestCodeGen.test(input, output, 548))
    def test_549 (self):
        input = """
        foo: function boolean(a: boolean, b: boolean)
        {
            return (a && b) && (a || b);
        }
        main: function void()
        {
            a, b: boolean = true, false;
            printBoolean(foo(a, b));
        }"""
        output = "false\n"
        self.assertTrue(TestCodeGen.test(input, output, 549))
    def test_550 (self):
        input = """
        foo: function boolean(a: boolean, b: boolean)
        {
            return (a && (!a || b)) && ((a || !b) || b);
        }
        main: function void()
        {
            a, b: boolean = true, true;
            printBoolean(foo(a, b));
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 550))
    def test_551 (self):
        input = """
        foo: function void (out a: integer, out b: integer, c: integer)
        {
            b = b + 10;
            a = a + c + 20;
            printInteger(a);
            printInteger(b);
            printInteger(c);
        }
        main: function void()
        {
            j, k: boolean = 10, 15;
            foo(j, j, k);
            printInteger(j);
            printInteger(k);
        }"""
        output = "45\n20\n15\n20\n15\n"
        self.assertTrue(TestCodeGen.test(input, output, 551))
    def test_552 (self):
        input = """
        min: function integer (a: integer, b: integer)
        {
            if (a < b)
            {
                return a;
            }
            return b;
        }
        main: function void()
        {
            a, b, c, d: integer = readInteger(), readInteger(), readInteger(), readInteger(); // Input 3 -1 10 6
            printInteger(min(min(min(a, b), c), d));
        }"""
        output = "-1\n"
        self.assertTrue(TestCodeGen.test(input, output, 552))
    def test_553 (self):
        input = """
        foo: function boolean(a: boolean, b: boolean)
        {
            if((a && (!a || b)) && ((a || !b) || b))
            {
                return true;
            }
            return false;
        }
        main: function void()
        {
            a, b: boolean = true, true;
            printBoolean(foo(a, b));
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 553))
    def test_554 (self):
        input = """
        manum1: function integer(a: integer, b: integer)
        {
            if (a > b)
            {
                return a;
            }
            return b;
        }
        manum1Ele: function integer(arr: arranum2 [10] of integer, n: integer)
        {
            if (n == 1)
            {
                return arr[0];
            }
            k: integer = manum1(arr[n - 1], manum1Ele(arr, n - 1));
            return k;
        }
        main: function void()
        {
            arr: arranum2[10] of integer = {-1, 3, 9, 6, 7, 8, 2, 0, 1, 4};
            n: integer = 10;
            printInteger(manum1Ele(arr, n));
        }"""
        output = "9\n"
        self.assertTrue(TestCodeGen.test(input, output, 554))
    def test_555 (self):
        input = """
        findEle: function integer (arr: arranum2[20] of integer, low: integer, high: integer, target: integer)
        {
            if (low <= high)
            {
                mid: integer = low + (high - low) / 2;
                if (arr[mid] == target)
                {
                    return mid;
                }
                if (arr[mid] < target)
                {
                    return findEle(arr, mid + 1, high, target);
                }
                return findEle(arr, 0, mid - 1, target);
            }
            return -1;
        }
        main: function void()
        {
            arr: arranum2[20] of integer = {-26, -15, -8, -3, 0, 4, 10, 21, 30, 45, 49, 51, 59, 67, 70, 71, 78, 89, 94, 100};
            printInteger(findEle(arr, 0, 19, 94));
        }"""
        output = "18\n"
        self.assertTrue(TestCodeGen.test(input, output, 555))
    def test_556 (self):
        input = """
        swapNumber: function void(out a: integer, out b: integer)
        {
            temp: integer = a;
            a = b;
            b = temp;
        }
        sort: function void (arr: arranum2[20] of integer, low: integer, high: integer)
        {
            if (low < high)
            {
                idnum1: integer = partition(arr, low, high);
                sort(arr, low, idnum1 - 1);
                sort(arr, idnum1 + 1, high);
            }
        }
        partition: function integer(arr: arranum2[20] of integer, low: integer, high: integer)
        {
            pivot, left, right: integer = arr[high], low, high - 1;
            while (true)
            {
                while ((left <= right) && (arr[left] < pivot))
                {
                    left = left + 1;
                }
                while ((right >= left) && (arr[right] > pivot))
                {
                    right = right - 1;
                }
                if (left >= right)
                {
                    break;
                }
                swapNumber(arr[left], arr[right]);
                left = left + 1;
                right = right - 1;
            }
            swapNumber(arr[left], arr[high]);
            return left;
        }
        main: function void()
        {
            arr: arranum2[20] of integer = {-26, 15, 8, -3, 0, 4, -10, 21, 30, 10, 49, -51, 59, 67, -70, 71, 33, -89, 27, 100};
            sort(arr, 0, 19);
            i: integer;
            for (i = 0, i < 20, 1)
            {
                printInteger(arr[i]);
            }
        }"""
        output = "-89\n-70\n-51\n-26\n-10\n-3\n0\n4\n8\n10\n15\n21\n27\n30\n33\n49\n59\n67\n71\n100\n"
        self.assertTrue(TestCodeGen.test(input, output, 556))
    def test_557 (self):
        input = """
        main: function void()
        {
            arr: arranum2[5] of integer = {-3, 9, 0, 1, 8};
            i: integer;
            for (i = 0, i <= 2, 1)
            {
                temp: integer = arr[i];
                arr[i] = arr[4 - i];
                arr[4 - i] = temp;
            }
            for(i = 0, i < 5, 1)
            {
                printInteger(arr[i]);
            }
        }"""
        output = "8\n1\n0\n9\n-3\n"
        self.assertTrue(TestCodeGen.test(input, output, 557))
    def test_558 (self):
        input = """
        swapNum: function void(out a: integer, out b: integer)
        {
            temp: integer = a;
            a = b;
            b = temp;
        }
        main: function void()
        {
            printString(\"Before swapping:\");
            a, b: integer = 4, 7;
            printInteger(a);
            printInteger(b);
            swapNum(a, b);
            printString(\"After swapping:\");
            printInteger(a);
            printInteger(b);
        }"""
        output = "Before swapping:\n4\n7\nAfter swapping:\n7\n4\n"
        self.assertTrue(TestCodeGen.test(input, output, 558))
    def test_559 (self):
        input = """num1: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(num1, delta);
            printInteger(num1);
        }"""
        output = "71\n"
        self.assertTrue(TestCodeGen.test(input, output, 559))
    def test_560 (self):
        input = """
        swap: function void(a: integer, b: integer)
        {
            temp: integer = a;
            a = b;
            b = temp;
        }
        main: function void() {
            a, b: integer = 4, 7;
            swap(a, b);
            printInteger(a);
            printInteger(b);
        }"""
        output = "4\n7\n"
        self.assertTrue(TestCodeGen.test(input, output, 560))
    def test_561 (self):
        input = """
        foo: function float (a: integer, b: integer)
        {
            if (b == 0)
            {
                return 0;
            }
            return (a * 1.0) / b;
        }
        main: function void() {
            a, b: integer = 4, 7;
            printFloat(foo(a, b));
        }"""
        output = "0.5714286\n"
        self.assertTrue(TestCodeGen.test(input, output, 561))
    def test_562 (self):
        input = """
        a: auto = foo(1, 2) + 1;
        foo: function auto (a: auto, b: auto)
        {
            return a + b;
        }
        main: function void() {
            printInteger(a);
        }"""
        output = "4\n"
        self.assertTrue(TestCodeGen.test(input, output, 562))
    def test_563 (self):
        input = """
        a, b, c: integer = 3, 4, 5;
        num1: auto = a * a + b * b == c * c;
        main: function void() {
            printBoolean(num1);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 563))
    def test_564 (self):
        input = """
        a: arranum2 [10] of integer = {3, 9, 1, 0, 6, 4, 5, 8, 7, 2};
        manum1: function integer(a: integer, b: integer)
        {
            if (a > b)
            {
                return a;
            }
            return b;
        }
        manum1Ele: function integer(arr: arranum2 [10] of integer, n: integer)
        {
            if (n == 1)
            {
                return arr[0];
            }
            k: integer = manum1(arr[n - 1], manum1Ele(arr, n - 1));
            return k;
        }
        main: function void() {
            printInteger(manum1Ele(a, 10));
        }"""
        output = "9\n"
        self.assertTrue(TestCodeGen.test(input, output, 564))
    def test_565 (self):
        input = """
        a: arranum2 [10] of integer = {3, 9, 1, 0, 6, 4, 5, 8, 7, 2};
        main: function void() {
            i: integer;
            for(i = 0, i < 5, 1)
            {
                temp: integer = a[i];
                a[i] = a[9 - i];
                a[9 - i] = temp;
            }
            for(i = 0, i < 10, 1)
            {
                printInteger(a[i]);
            }
        }"""
        output = "2\n7\n8\n5\n4\n6\n0\n1\n9\n3\n"
        self.assertTrue(TestCodeGen.test(input, output, 565))
    def test_566 (self):
        input = """
        a, b, c: string = "Hello", "World", (a :: " ") :: (b :: "!");
        main: function void() {
            printString(c);
        }"""
        output = "Hello World!\n"
        self.assertTrue(TestCodeGen.test(input, output, 566))
    def test_567 (self):
        input = """
        main: function void() {
            printString("Hello " :: "World!");
        }"""
        output = "Hello World!\n"
        self.assertTrue(TestCodeGen.test(input, output, 567))
    def test_568 (self):
        input = """
        main: function void() {
            c: integer = 1 + 2;
            d: float = 1.5 + 2;
            e: float = 3.7 + 9.1;
            printInteger(c);
            printFloat(d);
            printFloat(e);
        }"""
        output = "3\n3.5\n12.8\n"
        self.assertTrue(TestCodeGen.test(input, output, 568))
    def test_569 (self):
        input = """
        powMod: function integer (a: integer, b: integer, m: integer)
        {
            if (b == 0)
            {
                return 1;
            }
            p: integer = ((powMod(a, b / 2, m) % m) * (powMod(a, b / 2, m) % m)) % m;
            if (b % 2 == 0)
            {
                return p;
            }
            return (p * (a % m)) % m;
        }
        main: function void() {
            num1, num2, m: integer = 3, 29, 1337;
            printInteger(powMod(num1, num2, m));
        }"""
        output = "978\n"
        self.assertTrue(TestCodeGen.test(input, output, 569))
    def test_570 (self):
        input = """
        factorial: function integer(n: integer, m: integer)
        {
            res, i: integer = 1, 1;
            for(i = 1, i <= n, 1)
            {
                res = ((res % m) * (i % m)) % m;
            }
            return res;
        }
        main: function void() {
            n, m: integer = 100, 1337;
            printInteger(factorial(n, m));
        }"""
        output = "1015\n"
        self.assertTrue(TestCodeGen.test(input, output, 570))
    def test_571 (self):
        input = """
        sumDigit: function integer(n: integer)
        {
            sum: integer = 0;
            while(n > 0)
            {
                sum = sum + (n % 10);
                n = n / 10;
            }
            return sum;
        }
        primes: function boolean(n: integer)
        {
            i: integer;
            for(i = 2, i * i <= n, 1)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }
            return n > 1;
        }
        main: function void() {
            n: integer = readInteger(); // Input 28
            i: integer;
            flag: boolean = false;
            for (i = n, i >= 10, -1)
            {
                if (primes(i) && primes(sumDigit(i)))
                {
                    printInteger(i);
                    flag = true;
                    break;
                }
            }
            if (!flag)
            {
                printInteger(0);
            }
        }"""
        output = "23\n"
        self.assertTrue(TestCodeGen.test(input, output, 571))
    def test_572 (self):
        input = """
        reverse: function integer (n: integer)
        {
            result, temp: integer = 0, n;
            if (temp < 0)
            {
                n = -n;
            }
            while (n > 0)
            {
                result = 10 * result + (n % 10);
                n = n / 10;
            }
            if (temp < 0)
            {
                return -result;
            }
            return result;
        }
        main: function void() {
            n: integer = readInteger(); // Input -28
            printInteger(reverse(n));
        }"""
        output = "-82\n"
        self.assertTrue(TestCodeGen.test(input, output, 572))
    def test_573 (self):
        input = """
        main: function void() {
            a: integer = 8;
            b: arranum2 [3] of integer = {1, 2, 3};
            b[2] = a;
            printInteger(b[2]);
        }"""
        output = "8\n"
        self.assertTrue(TestCodeGen.test(input, output, 573))
    def test_574 (self):
        input = """
        main: function void() {
            printInteger(foo(3, 9));
        }
        foo: function integer(a: integer, b: integer)
        {
            if (a < b)
            {
                return b;
            }
            return a;
        }"""
        output = "9\n"
        self.assertTrue(TestCodeGen.test(input, output, 574))
    def test_575 (self):
        input = """
        main: function void() {
            a, b: integer = 3, 4;
            swap(a, b);
            printInteger(a);
            printInteger(b);
        }
        swap: function void(out a: integer, out b: integer)
        {
            temp: integer = a;
            a = b;
            b = temp;
        }"""
        output = "4\n3\n"
        self.assertTrue(TestCodeGen.test(input, output, 575))
    def test_576 (self):
        input = """
        bar: function void (a: integer, out b: integer, c: integer)
        {
            a = a + 10;
            b = a + c + 4;
            printInteger(a);
            printInteger(b);
            printInteger(c);
        }
        main: function void() {
            j, k: integer = 10, 15;
            bar(j, j, j + k);
            printInteger(j);
            printInteger(k);
        }"""
        output = "20\n49\n25\n49\n15\n"
        self.assertTrue(TestCodeGen.test(input, output, 576))
    def test_577 (self):
        input = """
        concat: function string (a: string, b: string)
        {
            return a :: b;
        }
        main: function void() {
            a, b: string = "Hello ", "World!";
            printString(concat(a, b));
        }"""
        output = "Hello World!\n"
        self.assertTrue(TestCodeGen.test(input, output, 577))
    def test_578 (self):
        input = """
        accumulate: function integer (arr: arranum2 [10] of integer, low: integer, high: integer, init: integer)
        {
            if ((low > high) || (low < 0) || (low > 9) || (high <= 0) || (high > 10))
            {
                return init;
            }
            i: integer;
            for(i = low, i < high, 1)
            {
                init = init + arr[i];
            }
            return init;
        }
        main: function void() {
            arr: arranum2 [10] of integer = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            printInteger(accumulate(arr, 0, 10, 55));
        }"""
        output = "110\n"
        self.assertTrue(TestCodeGen.test(input, output, 578))
    def test_579 (self):
        input = """
        removeMin: function void(arr: arranum2 [10] of integer, out n: integer)
        {
            i: integer;
            min: integer = arr[0];
            for(i = 1, i < n, 1)
            {
                if (min > arr[i])
                {
                    min = arr[i];
                }
            }
            for(i = 0, i < n, 1)
            {
                if (arr[i] == min)
                {
                    n = n - 1;
                    j: integer;
                    for (j = i, j < n, 1)
                    {
                        arr[j] = arr[j + 1];
                    }
                    i = i - 1;
                }
            }
        }
        main: function void() {
            arr: arranum2 [10] of integer = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1};
            n: integer = 10;
            removeMin(arr, n);
            i: integer;
            for(i = 0, i < n, 1)
            {
                printInteger(arr[i]);
            }
        }"""
        output = "2\n3\n4\n5\n6\n7\n8\n9\n"
        self.assertTrue(TestCodeGen.test(input, output, 579))
    def test_580 (self):
        input = """
        main: function void() {
            printString("Hello World!");
        }"""
        output = "Hello World!\n"
        self.assertTrue(TestCodeGen.test(input, output, 580))
    def test_581 (self):
        input = """
        foo: function void(inherit a: integer, b: integer)
        {
            return;
        }
        bar: function void(c: integer) inherit foo
        {
            super(2, 1);
            printInteger(a);
        }
        main: function void() {
            bar(2);
        }"""
        output = "2\n"
        self.assertTrue(TestCodeGen.test(input, output, 581))
    def test_582 (self):
        input = """
        main: function void() {
            i: integer = 0;
            while(true)
            {
                if (i == 20)
                {
                    break;
                }
                i = i + 1;
            }
            printInteger(i);
        }"""
        output = "20\n"
        self.assertTrue(TestCodeGen.test(input, output, 582))
    def test_583 (self):
        input = """
        main: function void() {
            i: integer;
            for(i = 0, i < 10, i + 1)
            {
                printInteger(i);
            }
        }"""
        output = "0\n1\n3\n7\n"
        self.assertTrue(TestCodeGen.test(input, output, 583))
    def test_584 (self):
        input = """
        isAmstrong: function boolean (n: integer)
        {
            sum, temp: integer = 0, n;
            while (temp > 0)
            {
                digit: integer = temp % 10;
                sum = sum + digit * digit * digit;
                temp = temp / 10;
            }
            return sum == n;
        }
        main: function void() {
            a: integer = 153;
            printBoolean(isAmstrong(a));
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 584))
    def test_585 (self):
        input = """
        foo: function void (out a: integer)
        {
            if (a % 2 == 0)
            {
                a = a / 2;
            }
            else
            {
                a = 3 * a + 1;
            }
        }
        main: function void() {
            a: integer = 153;
            foo(a);
            printInteger(a);
        }"""
        output = "460\n"
        self.assertTrue(TestCodeGen.test(input, output, 585))
    def test_586 (self):
        input = """
        fibo: function integer(n: integer)
        {
            if (n <= 1)
            {
                return n;
            }
            return fibo(n - 1) + fibo(n - 2);
        }
        main: function void() {
            a: integer = 46;
            printInteger(fibo(a));
        }"""
        output = "1836311903\n"
        self.assertTrue(TestCodeGen.test(input, output, 586))
    def test_587 (self):
        input = """
        main: function void() {
            a, b, c: integer = 3, 4, 5;
            d: boolean = (a < 0) || (a * a + b * b == c * c) || (b < 0) || (c < 0);
            printBoolean(d);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 587))
    def test_588 (self):
        input = """
        main: function void() {
            a, b, c: integer = 3, 4, 5;
            d: boolean = a + b >= c;
            printBoolean(d);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 588))
    def test_589 (self):
        input = """
        main: function void() {
            a, b, c: integer = 3, 4, 5;
            d: boolean = !((a == b) || (b == c) || (c == a));
            printBoolean(d);
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 589))
    def test_590 (self):
        input = """
        abs: function float (a: float)
        {
            if (a < 0)
            {
                return -a;
            }
            return a;
        }
        foo: function boolean(a: float, b: float)
        {
            return abs(a) + abs(b) >= abs(a + b);
        }
        main: function void() {
            printBoolean(foo(2.1, -1.9));
        }"""
        output = "true\n"
        self.assertTrue(TestCodeGen.test(input, output, 590))
    def test_591 (self):
        input = """
        foo: function auto (a: integer, b: integer)
        {
            return a + b + 1.5;
        }
        main: function void() {
            num1: float = foo(1, 2) + 0.5;
            printFloat(num1);
        }"""
        output = "5.0\n"
        self.assertTrue(TestCodeGen.test(input, output, 591))
    def test_592 (self):
        input = """
        num1: integer = 65;
        inc: function void(out n: integer, delta: integer, dec: boolean)
        {
            if (dec == true)
            {
                n = n - delta;
            }
            else
            {
                n = n + delta;
            }
        }
        main: function void() {
            inc(num1, 3, false);
            printFloat(num1);
        }"""
        output = "68.0\n"
        self.assertTrue(TestCodeGen.test(input, output, 592))
    def test_593 (self):
        input = """
        num1: integer = 65;
        foo: function float (a: integer, b: integer)
        {
            if (b == 0)
            {
                return 0.0;
            }
            return (a * 1.0) / b;
        }
        main: function void() {
            a: float = foo(num1 - 4, 5);
            printFloat(a);
        }"""
        output = "12.2\n"
        self.assertTrue(TestCodeGen.test(input, output, 593))
    def test_594 (self):
        input = """
        num1, num2: integer = 65, 97;
        main: function void() {
            a: float = num1 + num2;
            printFloat(a);
        }"""
        output = "162.0\n"
        self.assertTrue(TestCodeGen.test(input, output, 594))
    def test_595 (self):
        input = """
        num1, num2, z: integer = 65, 97, num1 + num2;
        main: function void() {
            a: float = z + 2e3;
            printFloat(a);
        }"""
        output = "2162.0\n"
        self.assertTrue(TestCodeGen.test(input, output, 595))
    def test_596 (self):
        input = """
        foo: function void(num1: integer, num2: integer, z: float)
        {
            a: integer = num1 % num2;
            printFloat(a + z);
        }
        main: function void() {
            foo(20, 5, 0.99);
        }"""
        output = "0.99\n"
        self.assertTrue(TestCodeGen.test(input, output, 596))
    def test_597 (self):
        input = """
        main: function void() {
            a: arranum2 [1, 2] of integer = {{1, 2}};
            a[0, 0] = 3;
            a[0, 1] = a[0, 0] + a[0, 1];
            printInteger(a[0, 1]);
        }"""
        output = "5\n"
        self.assertTrue(TestCodeGen.test(input, output, 597))
    def test_598 (self):
        input = """
        main: function void() {
            a: arranum2 [10] of integer;
            i: integer;
            for(i = 0, i < 10, 1)
            {
                printInteger(a[i]);
            }
        }"""
        output = "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n"
        self.assertTrue(TestCodeGen.test(input, output, 598))
    def test_599 (self):
        input = """
        main: function void() {
            a: arranum2 [2, 3] of boolean;
            i, j: integer;
            for(i = 0, i < 2, 1)
            {
                for(j = 0, j < 3, 1)
                {
                    printBoolean(a[i, j]);
                }
            }
        }"""
        output = "false\nfalse\nfalse\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, output, 599))