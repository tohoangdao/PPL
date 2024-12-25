import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lex1(self):
        self.assertTrue(TestLexer.test(""" 
                                       "This is a string" 
                                       """, "abc,<EOF>", 101))

    def test_lex2(self):
        self.assertTrue(TestLexer.test("whAt","whAt,<EOF>",102))

    def test_lex3(self):
        self.assertTrue(TestLexer.test("HelloWorld","HelloWorld,<EOF>",103))

    def test_lex4(self):
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",104))

    def test_lex5(self):
        self.assertTrue(TestLexer.test("hElLoiTsMe","hElLoiTsMe,<EOF>",105))

    def test_lex6(self):
        self.assertTrue(TestLexer.test("tAke one of thIs","tAke,one,of,thIs,<EOF>",106))

    def test_lex7(self):
        self.assertTrue(TestLexer.test("          ","<EOF>",107))

    def test_lex8(self):
        self.assertTrue(TestLexer.test("under_score_","under_score_,<EOF>",108))

    def test_lex9(self):
        self.assertTrue(TestLexer.test("escape\nafter","escape,after,<EOF>",109))

    def test_lex10(self):
        self.assertTrue(TestLexer.test("123onetwothree","123,onetwothree,<EOF>",110))

    def test_lex11(self):
        self.assertTrue(TestLexer.test("onetwo12three3","onetwo12three3,<EOF>",111))

    def test_lex12(self):
        self.assertTrue(TestLexer.test("_g2414","_g2414,<EOF>",112))

    def test_lex13(self):
        self.assertTrue(TestLexer.test("/* Single line comment*/","<EOF>",113))

    def test_lex14(self):
        self.assertTrue(TestLexer.test("/* Multi \n line \n comment */","<EOF>",114))

    def test_lex15(self):
        self.assertTrue(TestLexer.test("@go404","@go404,<EOF>",115))

    def test_lex16(self):
        self.assertTrue(TestLexer.test("\"'Palace 2018'\"", """"'Palace 2018'",<EOF>""", 116))

    def test_lex17(self):
        self.assertTrue(TestLexer.test("/* alo another*/comment/* what */","comment,<EOF>",117))

    def test_lex18(self):
        self.assertTrue(TestLexer.test("else if  true false", "else,if,true,false,<EOF>", 118))

    def test_lex19(self):
        self.assertTrue(TestLexer.test("break continue", "break,continue,<EOF>", 119))

    def test_lex20(self):
        self.assertTrue(TestLexer.test("True true False false", "True,true,False,false,<EOF>", 120))

    def test_lex21(self):
        self.assertTrue(TestLexer.test("else if if else", "else,if,if,else,<EOF>", 121))

    def test_lex22(self):
        self.assertTrue(TestLexer.test("123 void 456 continue", "123,void,456,continue,<EOF>", 122))

    def test_lex23(self):
        self.assertTrue(TestLexer.test("1+1==2", "1,+,1,==,2,<EOF>", 123))

    def test_lex24(self):
        self.assertTrue(TestLexer.test("continu", "continu,<EOF>", 124))

    def test_lex25(self):
        self.assertTrue(TestLexer.test("class Shape", "class,Shape,<EOF>", 125))

    def test_lex26(self):
        self.assertTrue(TestLexer.test("=+-* \%", "=,+,-,*,\,%,<EOF>", 126))

    def test_lex27(self):
        self.assertTrue(TestLexer.test("11 > 2", "11,>,2,<EOF>", 127))

    def test_lex28(self):
        self.assertTrue(TestLexer.test("func @main():void", "func,@main,(,),:,void,<EOF>", 128))

    def test_lex29(self):
        self.assertTrue(TestLexer.test("=++.--.", "=,+,+,.,-,-,.,<EOF>", 129))

    def test_lex30(self):
        self.assertTrue(TestLexer.test("a*.b \ 11.2E2", "a,*,.,b,\,11.2E2,<EOF>", 130))

    def test_lex31(self):
        self.assertTrue(TestLexer.test("6.e2 /. 3", "6.e2,/,.,3,<EOF>", 131))

    def test_lex32(self):
        self.assertTrue(TestLexer.test("a && b || !c", "a,&&,b,||,!,c,<EOF>", 132))

    def test_lex33(self):
        self.assertTrue(TestLexer.test("if (a>b) && (b<c)","if,(,a,>,b,),&&,(,b,<,c,),<EOF>",133))

    def test_lex34(self):
        self.assertTrue(TestLexer.test("abc|||ef","abc,||,Error Token |",134))

    def test_lex35(self):
        self.assertTrue(TestLexer.test("9 >= 2 < 3","9,>=,2,<,3,<EOF>",135))

    def test_lex36(self):
        self.assertTrue(TestLexer.test("<<>> ==!=","<,<,>,>,==,!=,<EOF>",136))

    def test_lex37(self):
        self.assertTrue(TestLexer.test("> == >==",">,==,>=,=,<EOF>",137))

    def test_lex38(self):
        self.assertTrue(TestLexer.test("9 >= 1.22 < 4.3","9,>=,1.22,<,4.3,<EOF>",138))

    def test_lex39(self):
         self.assertTrue(TestLexer.test("<= / :===","<=,/,:=,==,<EOF>",139))

    def test_lex40(self):
        self.assertTrue(TestLexer.test("===%==/..:=","==,=,%,==,/,.,.,:=,<EOF>",140))

    def test_identifier41(self):
        self.assertTrue(TestLexer.test("\"'Yanxi Palace - 2018'\"", "'Yanxi Palace - 2018',<EOF>", 141))

    def test_lex42(self):
        self.assertTrue(TestLexer.test("1 * (3 + 6) != 12.5","1,*,(,3,+,6,),!=,12.5,<EOF>",142))

    def test_lex43(self):
        self.assertTrue(TestLexer.test("(||[&&}+-)","(,||,[,&&,},+,-,),<EOF>",143))

    def test_lex44(self):
        self.assertTrue(TestLexer.test("once upon; a time, there is.","once,upon,;,a,time,,,there,is,.,<EOF>",144))

    def test_lex45(self):
        self.assertTrue(TestLexer.test("a[0] := 1;","a,[,0,],:=,1,;,<EOF>",145))

    def test_lex46(self):
        self.assertTrue(TestLexer.test("123456","123456,<EOF>",146))

    def test_lex47(self):
        self.assertTrue(TestLexer.test("-100","-,100,<EOF>",147))

    def test_lex48(self):
        self.assertTrue(TestLexer.test("new constructor class", "new,constructor,class,<EOF>", 148))

    def test_lex49(self):
        self.assertTrue(TestLexer.test("self.abc", "self,.,abc,<EOF>", 149))

    def test_lex50(self):
        self.assertTrue(TestLexer.test("1234.self", "1234.,self,<EOF>", 150))

    def test_lex51(self):
        self.assertTrue(TestLexer.test("()).(null)", "(,),),.,(,null,),<EOF>", 151))

    def test_lex52(self):
        self.assertTrue(TestLexer.test("0O77","0,O77,<EOF>",152))

    def test_lex53(self):
        self.assertTrue(TestLexer.test("gag.@gag", "gag,.,@gag,<EOF>", 153))

    def test_lex54(self):
        self.assertTrue(TestLexer.test("123ab456","123,ab456,<EOF>",154))

    def test_lex55(self):
        self.assertTrue(TestLexer.test("12.35","12.35,<EOF>",155))

    def test_lex56(self):
        self.assertTrue(TestLexer.test("33..33","33.,.,33,<EOF>",156))

    def test_lex57(self):
        self.assertTrue(TestLexer.test("12e3","12e3,<EOF>",157))

    def test_lex58(self):
        self.assertTrue(TestLexer.test("12e-3","12e-3,<EOF>",158))

    def test_lex59(self):
        self.assertTrue(TestLexer.test("12.0e3","12.0e3,<EOF>",159))

    def test_lex60(self):
        self.assertTrue(TestLexer.test("50.E8","50.E8,<EOF>",160))

    def test_lex61(self):
        self.assertTrue(TestLexer.test("12000.120000e-1","12000.120000e-1,<EOF>",161))

    def test_lex62(self):
        self.assertTrue(TestLexer.test("12.12e-","12.12,e,-,<EOF>",162))

    def test_lex63(self):
        self.assertTrue(TestLexer.test("123.e456fgh","123.e456,fgh,<EOF>",163))

    def test_lex64(self):
        self.assertTrue(TestLexer.test("we have 12.Ee","we,have,12.,Ee,<EOF>",164))

    def test_lex65(self):
        self.assertTrue(TestLexer.test("30.  e5","30.,e5,<EOF>",165))

    def test_lex66(self):
        self.assertTrue(TestLexer.test("true false","true,false,<EOF>",166))

    def test_lex67(self):
        self.assertTrue(TestLexer.test("TrueEFFalse","TrueEFFalse,<EOF>",167))

    def test_lex68(self):
        self.assertTrue(TestLexer.test("12.3.4","12.3,.,4,<EOF>",168))

    def test_lex69(self):
        self.assertTrue(TestLexer.test("trueeffalse", "trueeffalse,<EOF>", 169))

    def test_lex70(self):
        self.assertTrue(TestLexer.test("if(a == true)  a = false;", "if,(,a,==,true,),a,=,false,;,<EOF>", 170))

    def test_lex71(self):
        self.assertTrue(TestLexer.test("if(a := trrue)", "if,(,a,:=,trrue,),<EOF>", 171))

    def test_lex72(self):
        self.assertTrue(TestLexer.test(
            """
                ""
                "String"
                " "
                "?"
                "-"
                "//"
                "Mulitiple Characters"
            """,

            """"","String"," ","?","-","//","Mulitiple Characters",<EOF>""",
            172
        ))

    def test_lex73(self):
        self.assertTrue(TestLexer.test(
            """
            ""
            "string"
            'string'
            "string'
            'string"
            """,

            """"","string",Error Token '""",
            173
        ))

    def test_lex74(self):
        self.assertTrue(TestLexer.test(
            """
            ""
            12 32.43 43.E12 4e-1 true "false" false "012" 1.32 1.
            "String"
            """,

            """"",12,32.43,43.E12,4e-1,true,"false",false,"012",1.32,1.,"String",<EOF>""",
            174
        ))

    def test_lex75(self):
        self.assertTrue(TestLexer.test(
            """
            " hello lexer
            """,

            """Unclosed String: " hello lexer""",
            175
        ))

    def test_lex76(self):
        self.assertTrue(TestLexer.test(
            """
            "Newline
                multiple lines
            "
            """,

            """Unclosed String: "Newline""",
            176
        ))

    def test_lex77(self):
        self.assertTrue(TestLexer.test(
            """
            "\"abc
            """,

            """"",abc,<EOF>""",
            177
        ))

    def test_lex78(self):
        self.assertTrue(TestLexer.test(
            """
            s = "string          '
            "a = 4
            g = 9
            """,

            """s,=,Unclosed String: "string          '""",
            178
        ))

    def test_lex79(self):
        self.assertTrue(TestLexer.test(
            """
            " abc \n xyz "
            " abc \\n xyz "
            """,

            """Unclosed String: " abc """,
            179
        ))

    def test_lex80(self):
        self.assertTrue(TestLexer.test(
            """
            " hello lexer \t \b \n \""     asdf
            """,

            """Unclosed String: " hello lexer """,
            180
        ))

    def test_lex81(self):
        self.assertTrue(TestLexer.test(
            """
            "Backspace  \b"
            "Formfeed   \f"
            "Return     \r"
            "Newline    \n"
            "Tab        \t"
            "Double quote       \""
            "Backslash  \\ "
            """,

            """Unclosed String: "Backspace  """,
            181
        ))

    def test_lex82(self):
        self.assertTrue(TestLexer.test("for i := 0; i < 100; i := i + 1 ", "for,i,:=,0,;,i,<,100,;,i,:=,i,+,1,<EOF>", 182))

    def test_lex83(self):
        self.assertTrue(TestLexer.test("i := i+1;", "i,:=,i,+,1,;,<EOF>", 183))

    def test_lex84(self):
        self.assertTrue(TestLexer.test("if(!a) {abar4[4]:=6}", "if,(,!,a,),{,abar4,[,4,],:=,6,},<EOF>", 184))

    def test_lex85(self):
        self.assertTrue(TestLexer.test("const aa11, bb42: int = 1 + 5, 2;", "const,aa11,,,bb42,:,int,=,1,+,5,,,2,;,<EOF>", 185))

    def test_lex86(self):
        self.assertTrue(TestLexer.test("var @x41, @ycae1 : int = 0, 0;", "var,@x41,,,@ycae1,:,int,=,0,,,0,;,<EOF>", 186))

    def test_lex87(self):
        self.assertTrue(TestLexer.test("var @abc : bool", "var,@abc,:,bool,<EOF>", 187))

    def test_lex88(self):
        self.assertTrue(TestLexer.test("aca[41]", "aca,[,41,],<EOF>", 188))

    def test_lex89(self):
        self.assertTrue(TestLexer.test("new thing", "new,thing,<EOF>", 189))

    def test_lex90(self):
        self.assertTrue(TestLexer.test("afa[3+x.foo(2)]", "afa,[,3,+,x,.,foo,(,2,),],<EOF>", 190))

    def test_lex91(self):
        self.assertTrue(TestLexer.test("return abc", "return,abc,<EOF>", 191))

    def test_lex92(self):
        self.assertTrue(TestLexer.test("return true", "return,true,<EOF>", 192))

    def test_lex93(self):
        self.assertTrue(TestLexer.test("return a <= b;", "return,a,<=,b,;,<EOF>", 193))

    def test_lex94(self):
        self.assertTrue(TestLexer.test("return 123*456", "return,123,*,456,<EOF>", 194))

    def test_lex95(self):
        self.assertTrue(TestLexer.test("class People <- Student", "class,People,<,-,Student,<EOF>", 195))

    def test_lex96(self):
        self.assertTrue(TestLexer.test("const acxx:= new People();", "const,acxx,:=,new,People,(,),;,<EOF>", 196))

    def test_lex97(self):
        self.assertTrue(TestLexer.test("func @main():float {}", "func,@main,(,),:,float,{,},<EOF>", 197))

    def test_lex98(self):
        self.assertTrue(TestLexer.test("e:=x*y;", "e,:=,x,*,y,;,<EOF>", 198))

    def test_lex99(self):
        self.assertTrue(TestLexer.test("return this.length*this.width;", "return,this,.,length,*,this,.,width,;,<EOF>", 199))

    def test_lex100(self):
        self.assertTrue(TestLexer.test("11, bb42: int = 1 + 5, 2;", "11,,,bb42,:,int,=,1,+,5,,,2,;,<EOF>", 200))      
