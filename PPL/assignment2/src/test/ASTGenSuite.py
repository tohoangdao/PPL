import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class gafa {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program1(self):
        """Simple program: class main {} """
        input = """class main {} class main3{} class main3{}"""
        expect = """Program([ClassDecl(Id(main),[]),ClassDecl(Id(main3),[]),ClassDecl(Id(main3),[])])"""
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_program4(self):
        """Simple program: class main {} """
        input = """
        class Shape {
    func getNumOfShape():int {
        return numOfShape;
    }
}  
"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_simple_program5(self):
        """Simple program: class main {} """
        input = """
        class Shape <-ava{

    }
}  
"""
        expect = """Program([ClassDecl(Id(ava),Id(Shape),[])])"""
        self.assertTrue(TestAST.test(input,expect,305))
    
    def test_simple_program6(self):
        input = """
        class Shape <- Retangle {
    func getArea():int {
        return self.length * self.width;
    }
}   
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_program7(self):
        input = """
        class Shape <- Rectangle {
    func getArea():int {
        return self.length * self.width / 3;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_program8(self):
        input = """
        class Program {
            func @main() : void {   
                s := new Rectangle(3,4);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_program9(self):
        input = """
        class Example3 {
    var a, b, c: float;
    const x, y, z: bool;
    var g, h, y: int;
    const a: string;
        /*
            =======================================
            Comment here
            =======================================
        */
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_simple_program10(self):
        input = """
        class Example3 {
    func @abcd() : void {
        bed[3] := [3.3, 4.3, 103e3];
        afa[3+x.foo(3)] := afa[bed[3]] +3;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 310))

#     def test_simple_program11(self):
#         input = """
#         class Example3 {
#     func @getNumOfShape():float {
#         const r,s;
#         var a: [5]int
#         // list of statements
#         r:=3.0;
#         s:=r*r*self.pi;
#         a[0]:= s;
#         return s;
#     }
# }
        
#         """
#         expect = "successful"
#         self.assertTrue(TestAST.test(input, expect, 311))

    def test_simple_program12(self):
        input = """
        class Somese {
    func @main():void {
        if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_simple_program13(self):
        input = """
        class Example3 {
    func @main():void {
        for a := 0; b < 10; c := d + 1 {
            bed[3] := [3.3, 4.3, 103e3];
        }
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_simple_program14(self):
        input = """
        class Person {
        var age: int;
        const name: string;

        func setName():void {}
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_simple_program15(self):
        input = """
        
 class Person {
        var age: [6]int;
        const name: [3]string;

        func getName():void {}
}
        
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_simple_program16(self):
        input = """
         class Person {

        var age: int;
        const name: string;

        func getAge():int {return self.age;}
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_simple_program17(self):
        input = """
         class Test {
        func abc():void {}
        func xyz():int {}
        func asf():string {}
        func aasdsf():bool {}
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_simple_program18(self):
        input = """
         class Test {
    func abc():void {
        self.aPI := 3.14;
        value := x.foo(5);
        l[3] := value * 3;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_simple_program19(self):
        input = """
        class Test {
  var @abc: int = 0;
  const vzxf: int = 0;
  var str: string;
  func abc(@abc: int):int {
        return abc;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_simple_program20(self):
        input = """
        class Test {
    func square(x:int):float {
        return x * x;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_main_program21(self):
        input = """
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
            }
        }
        class main {
            const x, y, z: int = 1, 2, 3;
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))]),ClassDecl(Id(main),[AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(z),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test_simple_program22(self):
        input = """
         class Test {
    func compare(x:int, y:int):bool {
        var com:bool;
        com:= x==y;
        return com;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simple_program22(self):
        input = """
         class Test {
    func compare(x:int, y:int):int {
        var com:int;
        if x>y{com:=1;}
        if x<y{com:=2;} else{com:=2;}
        return com;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simple_program24(self):
        input = """
         class Test {
    func @main():void {
        var valuee:int = 100;
        for i := 0; i < 10; i := i + 1 {
            valuee:= valuee+i;
        }
        var multi:int = 100;
        multi:=valuee*multi;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simple_program25(self):
        input = """
        class Test {
    func @main():void {
        var valuee:int = 0;
        for i := 0; i < 10; i := i + 1 {
            valuee:= valuee+i;
            continue;
        }
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 325))
    
    def test_simple_program26(self):
        input = """
        class Test {
    func @main():int {
        var valuee:int = 0;
        for i := 0; i < 10; i := i + 1 {
            valuee:= valuee+i;
            break;
        }
        return valuee;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_simple_program27(self):
        input = """
        class Test {
    func abc(b:[5] int):int {}
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_simple_program28(self):
        input = """
        class Test {
  var a: [5]int;
  const b:bool;
  const c:[4]string;
  func abc(b:[5] string):string {
    return self.b[2];
  }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_simple_program29(self):
        input = """
        class Test {
    const a, b: float = 5.14, 2.2-e415;
    var c:float= 21.441+E41;
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_simple_program30(self):
        input = """
        class Test {
    const a, b: bool = false, false;
    var c:bool= true;
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_simple_program31(self):
        input = """
        class Test <-Test1{
    func @abc():void {
        return self.asa;
  }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_simple_program32(self):
        input = """
        class Test {
    
}

class Test <-Test1{
    
}

class Test <-Test3{
    
}

class Test1 <-Test3{
    
}

class Test3 <-Test4{
    
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_simple_program33(self):
        input = """
        class Test {
    func @abc():void {
        if  !a && b {j := j - 1;} else {j := j + 1;}
    } 
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_simple_program34(self):
        input = """
        class Test {
    func @abc():void {
        if {j := 0;}  true {j := j - 1;} else {j := j + 1;}
    } 
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_simple_program35(self):
        input = """
        class Test {
    func @abc():void {
        for i := 3; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_main_program36(self):
        input = """
        class Program {
            func @main():void {
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(@main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@writeInt),[Id(i)])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,336))

    def test_simple_program37(self):
        input = """
        class Test {
    func @abc():void {
    } 
}

class Test <- Test1{
    func @abcd():float {
    } 
}

class Test <- Test3{
    func @abcd():bool {
    } 
}

class Test <- Test3{
    func @abcd():string {
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 337))
    
    def test_simple_program38(self):
        input = """
        class Test {
    var @a, @b : int = 0, 0;
}

class Test <- Test1{
    var @c, @d : int = 0, 0;
}

class Test <- Test3{
    var e, f: int = 0, 0;
}

class Test <- Test3{
    var g, h: int = 0, 0;
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_simple_program39(self):
        input = """
        class Test {
    func @abc():void {
        for i := 3; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
    func constructor(){}
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_simple_program40(self):
        input = """
        class Test {
    func @abc():void {
        for i := 3; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
            break;
        }
    } 
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_simple_program41(self):
        input = """
        class Test {
    func @abc():void {
        for i := 3; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
            continue;
        }
    } 
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_simple_program42(self):
        input = """
        class Test {
    func @abc():bool {
        if  a==b {return true;} else {return false;}
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_simple_program43(self):
        input = """
        class Test {
    func @abc():bool {
        if a==b {return true;} else {return false;}
    } 

    func @abcd(): int {
        a := 10;
        return 5;
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_simple_program44(self):
        input = """
        class Test {
    func @abcd():int {
        x.b[3] := x.m()[3];
        var r, s: int;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_simple_program45(self):
        input = """
        class Test {
    func @main():int {
        x.b[3] := x.m()[3];
        var r, s: int;
        return 50;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 345))
    
    def test_simple_program46(self):
        input = """
        class Test {
    func @main():void {
        io.@writeInt(30);
    }
}

        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_simple_program47(self):
        input = """
        class Test {
    func @main():void {
    }
}

class Test3 {
    func @main3():void {
    }
}

class Test <- abc133{
    func @main133():void {
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_simple_program48(self):
        input = """
        class Test {
    func num():int {
        return num;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_simple_program49(self):
        input = """
        class Test {
    func getb(b:int):int {
        return b%10;
    }
}

        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_simple_program50(self):
        input = """
        class Test {
    func @main():void {
        var x, y : int = 100, 10;
        a:=x+y;
        b:=x-y;
        c:=x%y;
        d:=x/y;
        e:=x*y;
    }
}     
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_simple_program51(self):
        input = """
        class Test {
    func @main(): void {
        var x, y : int = 100, 10;
        a := x+y;
        b:=x-y;
        c:=x%y;
        d:=x/y;
        e:=x*y;
        if a>0 && b<0 {e:=d;}
        if a>0 || c<0 {c:=d;}
        if e>0 && b<0 {a:=d;} 
    }
}     
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_simple_program52(self):
        input = """
        class Shape <- Retangle {
    func getArea():int {
        return self.@length * self.@width;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_simple_program53(self):
        input = """
        class @Shape <- Retangle {
    func getArea():int {
        return self.length * self.@width;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_simple_program54(self):
        input = """
        class @Shape <- Retangle {
    var length, width : float = 3.5,5.3e41;
    func getArea():float {
        return self.length * self.width;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_simple_program55(self):
        input = """
        class Test {
    var abc:string = "adasv3n1wd313j";
    const @fasa:string = "dvsdngewik";
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_simple_program56(self):
        input = """
        class Test {
    func @main():void {
        var abc:string="fasfafj";
        abc:="fefjfa";
        abc:="erfeafj";
        var e1: string;
        const e3:string;
        e1:=abc;
        e3:=abc;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_simple_program57(self):
        input = """
        class Test {
    func @main():bool {
        return true;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_simple_program58(self):
        input = """
        class Test {
    func @main():bool {
        return false;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_simple_program59(self):
        input = """
        class Test {
    func @main():float {
        return 1.;
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_simple_program60(self):
        input = """
        class Test {
    func @main():string {
        return "agva";
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_simple_program61(self):
        input = """
        class Test {
    func @main():void {
        var abc:string="fasfafj";
        var e1: string="afabw";
        var e3:string;
        e3:=abc^e1;
    }
} 
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 361))
    
    def test_simple_program62(self):
        input = """
        class Test {
    func @main():void {
        var abc:int;
        abc:= self.a() + b[3] + x.c[0];
    }
}         
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_simple_program63(self):
        input = """
        class Test {
    func @main():int {
        return 3*3;
    }
}         
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_simple_program64(self):
        input = """
        class Test {
    func @main():void {
        Shape.@getNumOfShape();
    }
}     
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_simple_program65(self):
        input = """
        class Test {
    func @main():string {
        return "abc" ^ "def";
    }
}   

       
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_main_program66(self):
        input = """
        class Program {
            func @main():void {
                io.@writeInt(i);
                io.@readInt();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(@writeInt),[Id(i)]),Call(Id(io),Id(@readInt),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,366))

    def test_simple_program67(self):
        input = """
        class Student {
    var age: int = 10;
    const name: string = "Harry";
    var height,weight: int;

    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_simple_program68(self):
        input = """
        class Student {
    var age: int = 10;
    const name: string = "Harry";
    var height,weight: int;

    func setAge():void {
        self.age:=15;
    }
}
       
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_simple_program69(self):
        input = """
        class Student {
    var age: int = 10;
    const name: string = "Harry";
    var height,weight: int;

    func setHeight():void {
    }
    func setWeight():void {
    }
}
   
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test_simple_program70(self):
        input = """
        class Student {
    var age: int = 10;
    const name: string = "Harry";
    var height,weight: int;

    func setHeight(height:float):void {
    }
    func setWeight():void {
        weight:= 4.5;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_simple_program71(self):
        input = """
        class Student
{
    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_simple_program72(self):
        input = """
        class People
{
    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
}


class People <- Student
{
    
    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_simple_program73(self):
        input = """
        class People
{
    var maxAge: int = 100;
}


class People <- Student
{
    var age: int = 10;
}

class Student <- Parent
{
    var pAge:int = 40;
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_simple_program74(self):
        input = """
        class People
{
    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
}


class People <- Student
{
 
    func getName():string {
        acxx:= new People();
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
}

class Student <- Parent
{

    func getName():string {
        return name;
    }
    func getAge():int {
        return age;
    }

    func getHeight():float {
        return @height;
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_simple_program75(self):
        input = """
        class Vehicle
{
    func getWeight():float {
    }
}


class Vehicle<-Car
{
}

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_simple_program76(self):
        input = """
        class Vehicle
{
    func vehicle():string {
        return "vehicle";
    }
}


class Vehicle<-Car
{
    func car():string {
        return "car";
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_simple_program77(self):
        input = """
        
class Operator
{
    func @main():float {
        return 1.1/4.1;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test_simple_program78(self):
        input = """
        class Operator
{
    func @main():float {
        return -1.3e1;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_simple_program79(self):
        input = """
        class Operator
{
    func @main():float {
        return -1.3e1 + 4.1 *41.0 ;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_simple_program80(self):
        input = """
        class Operator
{
    func @main():int {
        return 134134 % 413 ;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_simple_program81(self):
        input = """
        class Operator
{
    func @main():int {
        return 134134 % 413 * (31 + 51);
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_simple_program82(self):
        input = """
        class Test {
    func @main():int {
        var valuee:int = 30;
        for i := 0; i < 10; i := i + 1 {
            valuee:= valuee+i;
            if valuee > i {valuee:= valuee*i;} else {i:=i+1;}
            break;
        }
        return valuee;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_simple_program83(self):
        input = """
        class Test {
    func @main():int {
        var valuee:int = 30;
        if valuee > 0 {
            for i := 0; i < 10; i := i + 1 {
                valuee:= valuee+i;              
                continue;
            }
        } 
        else {i:=i+1;}
        return valuee;
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_simple_program84(self):
        input = """
        class Test {
    func @main():void {
        var r, s: int;
        r := 30;
        var a, b: [5]int;
        s := r * self.space;
        a[0] := s;
        b[4] :=r;
        var str : string = "agaf";
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_simple_program85(self):
        input = """
        class Test {
    func @main():void {
        a[(3+x.foo(3))/5*3-35] := a[b[3]] +3*a[4]/3;
    }
}        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def test_simple_program86(self):
        input = """
        class Test {
    func @main():void {
        var RETURN:string;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_simple_program87(self):
        input = """
        class Return {
    func @main():int {
        return 319313*434134141;
    }
}  
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_simple_program88(self):
        input = """
        class Operator
{
    func @main():void {
        break;
        continue;
        var @x, @y : bool = a==b, a!=b;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_simple_program89(self):
        input = """
        class Operator
{
    func @main():void {
        var @x, @y : bool = a==b, a!=b;
        x:= a>=b;
        y:= a[4] < self.b;
    }
}
  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_simple_program90(self):
        input = """
        class Returnn {
    func @main():void {
        return;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_simple_program91(self):
        input = """
        class Returnn {
    func @main():bool {
        return a && b;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_simple_program92(self):
        input = """
        class Returnn {
    func @main():bool {
        return a || b;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_simple_program93(self):
        input = """
        class Returnn {
    func @main():bool {
        return a <= b;
    }
}  
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test_simple_program94(self):
        input = """
        class Returnn {
    func @main():bool {
        a:=b+1;
        return a <= b;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_simple_program95(self):
        input = """
        class Test {
    func @main():void {
        a:=b+1;
        c:=a+1;
        d:=c+1;
        b:=d+1;
        return;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_simple_program96(self):
        input = """
        class Test {
    func swap():void {
        c:=a;
        a:=b;
        b:=c;
        return;
    }
}  
        
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_simple_program97(self):
        input = """
        class Test {
    func swap(a:int,b:int):void {
        var c:int;
        c:=a;
        a:=b;
        b:=c;
        return;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_simple_program98(self):
        input = """
        class Test {
    var a: [3]int = [1,3,3];
} 
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_simple_program99(self):
        input = """
        class Returnn {
    func @main():bool {
        return true && false;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_simple_program100(self):
        input = """
        class Returnn {
    func @main():bool {
        return true || false;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 400))

