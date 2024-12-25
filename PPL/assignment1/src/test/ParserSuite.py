import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        input = """
        class A{
            func x() :void{}
        }
        class B <- A{func x() :void{/*cmt*/}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
        input = """
        class Program {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):
        input = """
        class gah4123 <- abc{ }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program4(self):
        input = """
        class Shape {
var @numOfShape: int = 0;
const immutableAttribute: int = 0;
var length, width: int;
}
    
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):
        input = """
        class Shape {
    func @getNumOfShape():int {
        return @numOfShape;
    }
}         
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test_simple_program6(self):
        input = """
        class Shape <- Retangle {
    func getArea():int {
        return self.length * self.width;
    }
}   
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_simple_program7(self):
        input = """
        class Shape <- Rectangle {
    func getArea():int {
        return self.length * self.width / 2;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_simple_program8(self):
        input = """
        class Program {
            func @main() : void {   
                s := new Rectangle(3,4);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program9(self):
        input = """
        class Example2 {
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
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program10(self):
        input = """
        class Example2 {
    func @abcd() : void {
        bed[3] := [2.3, 4.2, 102e3];
        afa[3+x.foo(2)] := afa[bed[2]] +3;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

#     def test_simple_program11(self):
#         input = """
#         class Example2 {
#     func @getNumOfShape():float {
#         const r,s;
#         var a: [5]int
#         // list of statements
#         r:=2.0;
#         s:=r*r*self.pi;
#         a[0]:= s;
#         return s;
#     }
# }
        
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))

    def test_simple_program12(self):
        input = """
        class Somese {
    func @main():void {
        if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_simple_program13(self):
        input = """
        class Example2 {
    func @main():void {
        for a := 0; b < 10; c := d + 1 {
            bed[3] := [2.3, 4.2, 102e3];
        }
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_simple_program14(self):
        input = """
        class Person {
        var age: int;
        const name: string;

        func setName():void {}
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_simple_program15(self):
        input = """
        
 class Person {
        var age: [6]int;
        const name: [3]string;

        func getName():void {}
}
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_simple_program16(self):
        input = """
         class Person {

        var age: int;
        const name: string;

        func getAge():int {return self.age;}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

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
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_program18(self):
        input = """
         class Test {
    func abc():void {
        self.aPI := 3.14;
        value := x.foo(5);
        l[3] := value * 2;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

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
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_simple_program20(self):
        input = """
        class Test {
    func square(x:int):float {
        return x * x;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_simple_program21(self):
        input = """
        class Test {
    func mul(x:int, y:int, z:int):int {
        var multi:int;
        multi:= x*y*z;
        return multi;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    
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
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_simple_program23(self):
        input = """
         class Test {
    func compare(x:int, y:int):int {
        var com:int;
        if x>y{com:=1;}
        if x<y{com:=2;} else{com:=3;}
        return com;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

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
        self.assertTrue(TestParser.test(input, expect, 224))

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
        self.assertTrue(TestParser.test(input, expect, 225))
    
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
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_simple_program27(self):
        input = """
        class Test {
    func abc(b:[5] int):int {}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_simple_program28(self):
        input = """
        class Test {
  var a: [5]int;
  const b:bool;
  const c:[4]string;
  func abc(b:[5] string):string {
    return self.b[3];
  }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_simple_program29(self):
        input = """
        class Test {
    const a, b: float = 5.14, 2.3-e415;
    var c:float= 31.441+E41;
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    
    def test_simple_program30(self):
        input = """
        class Test {
    const a, b: bool = false, false;
    var c:bool= true;
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_simple_program31(self):
        input = """
        class Test <-Test1{
    func @abc():void {
        return self.asa;
  }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_simple_program32(self):
        input = """
        class Test {
    
}

class Test <-Test1{
    
}

class Test <-Test2{
    
}

class Test1 <-Test3{
    
}

class Test2 <-Test4{
    
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_simple_program33(self):
        input = """
        class Test {
    func @abc():void {
        if  !a && b {j := j - 1;} else {j := j + 1;}
    } 
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_simple_program34(self):
        input = """
        class Test {
    func @abc():void {
        if {j := 0;}  true {j := j - 1;} else {j := j + 1;}
    } 
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_simple_program35(self):
        input = """
        class Test {
    func @abc():void {
        for i := 2; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_simple_program36(self):
        input = """
        class Test {
    func @abc():void {
        for i := 2; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
}

class Test <- Test1{
    func @abcde():int {
        for i := 2; i < 100; i := i * 3 {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

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

class Test <- Test2{
    func @abcd():bool {
    } 
}

class Test <- Test3{
    func @abcd():string {
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test_simple_program38(self):
        input = """
        class Test {
    var @a, @b : int = 0, 0;
}

class Test <- Test1{
    var @c, @d : int = 0, 0;
}

class Test <- Test2{
    var e, f: int = 0, 0;
}

class Test <- Test3{
    var g, h: int = 0, 0;
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_simple_program39(self):
        input = """
        class Test {
    func @abc():void {
        for i := 2; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
        }
    } 
    func constructor(){}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_simple_program40(self):
        input = """
        class Test {
    func @abc():void {
        for i := 2; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
            break;
        }
    } 
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_simple_program41(self):
        input = """
        class Test {
    func @abc():void {
        for i := 2; i < 1000; i := i * i {
            io.@writeInt(i);
            i:= i-1;
            continue;
        }
    } 
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_simple_program42(self):
        input = """
        class Test {
    func @abc():bool {
        if  a==b {return true;} else {return false;}
    } 
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

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
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_simple_program44(self):
        input = """
        class Test {
    func @abcd():int {
        x.b[2] := x.m()[3];
        var r, s: int;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_simple_program45(self):
        input = """
        class Test {
    func @main():int {
        x.b[2] := x.m()[3];
        var r, s: int;
        return 50;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_simple_program46(self):
        input = """
        class Test {
    func @main():void {
        io.@writeInt(30);
    }
}

        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_simple_program47(self):
        input = """
        class Test {
    func @main():void {
    }
}

class Test2 {
    func @main2():void {
    }
}

class Test <- abc123{
    func @main123():void {
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_simple_program48(self):
        input = """
        class Test {
    func num():int {
        return num;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_simple_program49(self):
        input = """
        class Test {
    func getb(b:int):int {
        return b%10;
    }
}

        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

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
        self.assertTrue(TestParser.test(input, expect, 250))

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
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_simple_program52(self):
        input = """
        class Shape <- Retangle {
    func getArea():int {
        return self.@length * self.@width;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_simple_program53(self):
        input = """
        class @Shape <- Retangle {
    func getArea():int {
        return self.length * self.@width;
    }
}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    
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
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_simple_program55(self):
        input = """
        class Test {
    var abc:string = "adasv2n1wd212j";
    const @fasa:string = "dvsdngewik";
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_simple_program56(self):
        input = """
        class Test {
    func @main():void {
        var abc:string="fasfafj";
        abc:="fefjfa";
        abc:="erfeafj";
        var e1: string;
        const e2:string;
        e1:=abc;
        e2:=abc;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_simple_program57(self):
        input = """
        class Test {
    func @main():bool {
        return true;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_simple_program58(self):
        input = """
        class Test {
    func @main():bool {
        return false;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_simple_program59(self):
        input = """
        class Test {
    func @main():float {
        return 1.;
    }
}
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_simple_program60(self):
        input = """
        class Test {
    func @main():string {
        return "agva";
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_simple_program61(self):
        input = """
        class Test {
    func @main():void {
        var abc:string="fasfafj";
        var e1: string="afabw";
        var e2:string;
        e2:=abc^e1;
    }
} 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
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
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_simple_program63(self):
        input = """
        class Test {
    func @main():int {
        return 2*3;
    }
}         
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_simple_program64(self):
        input = """
        class Test {
    func @main():void {
        Shape.@getNumOfShape();
    }
}     
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_simple_program65(self):
        input = """
        class Test {
    func @main():string {
        return "abc" ^ "def";
    }
}   

       
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_simple_program66(self):
        input = """
        class Student {
    var age: int = 10;
    const name: string = "Harry";
    var height: int;
 }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

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
        self.assertTrue(TestParser.test(input, expect, 267))

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
        self.assertTrue(TestParser.test(input, expect, 268))

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
        self.assertTrue(TestParser.test(input, expect, 269))
    
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
        self.assertTrue(TestParser.test(input, expect, 270))

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
        self.assertTrue(TestParser.test(input, expect, 271))

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
        self.assertTrue(TestParser.test(input, expect, 272))

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
        self.assertTrue(TestParser.test(input, expect, 273))

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
        self.assertTrue(TestParser.test(input, expect, 274))

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
        self.assertTrue(TestParser.test(input, expect, 275))

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
        self.assertTrue(TestParser.test(input, expect, 276))

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
        self.assertTrue(TestParser.test(input, expect, 277))
    
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
        self.assertTrue(TestParser.test(input, expect, 278))

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
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_simple_program80(self):
        input = """
        class Operator
{
    func @main():int {
        return 124124 % 412 ;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_simple_program81(self):
        input = """
        class Operator
{
    func @main():int {
        return 124124 % 412 * (31 + 51);
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_simple_program82(self):
        input = """
        class Test {
    func @main():int {
        var valuee:int = 20;
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
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_simple_program83(self):
        input = """
        class Test {
    func @main():int {
        var valuee:int = 20;
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
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_simple_program84(self):
        input = """
        class Test {
    func @main():void {
        var r, s: int;
        r := 20;
        var a, b: [5]int;
        s := r * self.space;
        a[0] := s;
        b[4] :=r;
        var str : string = "agaf";
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_simple_program85(self):
        input = """
        class Test {
    func @main():void {
        a[(3+x.foo(2))/5*3-25] := a[b[2]] +3*a[4]/3;
    }
}        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test_simple_program86(self):
        input = """
        class Test {
    func @main():void {
        var RETURN:string;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_simple_program87(self):
        input = """
        class Return {
    func @main():int {
        return 319313*424124141;
    }
}  
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

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
        self.assertTrue(TestParser.test(input, expect, 288))

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
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_simple_program90(self):
        input = """
        class Returnn {
    func @main():void {
        return;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_simple_program91(self):
        input = """
        class Returnn {
    func @main():bool {
        return a && b;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_simple_program92(self):
        input = """
        class Returnn {
    func @main():bool {
        return a || b;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_simple_program93(self):
        input = """
        class Returnn {
    func @main():bool {
        return a <= b;
    }
}  
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    
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
        self.assertTrue(TestParser.test(input, expect, 294))

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
        self.assertTrue(TestParser.test(input, expect, 295))

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
        self.assertTrue(TestParser.test(input, expect, 296))

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
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_simple_program98(self):
        input = """
        class Test {
    var a: [3]int = [1,2,3];
} 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_simple_program99(self):
        input = """
        class Returnn {
    func @main():bool {
        return true && false;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_simple_program100(self):
        input = """
        class Returnn {
    func @main():bool {
        return true || false;
    }
}  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

