import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier(self):
        """normal identifier"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        
    def test_lower_upper_id(self):
        """identifier with upper case"""
        self.assertTrue(TestLexer.checkLexeme("whAt","whAt,<EOF>",102))
        
    def test_error_first_upper_id(self):
        """identifier with first upper case"""
        self.assertTrue(TestLexer.checkLexeme("HelloWorld","Error Token H",103))
        
    def test_wrong_token(self):
        """identifier with symbol"""
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",104))
        
    def test_many_upper_id(self):
        """Many upper case in identifier"""
        self.assertTrue(TestLexer.checkLexeme("hElLoiTsMe","hElLoiTsMe,<EOF>",105))
        
    def test_id_blankspace(self):
        """many identifier"""
        self.assertTrue(TestLexer.checkLexeme("tAke one of thIs","tAke,one,of,thIs,<EOF>",106))
        
    def test_only_blankspace(self):
        """only blank space"""
        self.assertTrue(TestLexer.checkLexeme("          ","<EOF>",107))
        
    def test_id_underscore(self):
        """identifier with underscore"""
        self.assertTrue(TestLexer.checkLexeme("under_score_","under_score_,<EOF>",108))
        
    def test_id_escape(self):
        """identifier with escape"""
        self.assertTrue(TestLexer.checkLexeme("escape\nafter","escape,after,<EOF>",109))
        
    def test_error_id_number_init(self):
        """error identifier with number first"""
        self.assertTrue(TestLexer.checkLexeme("123onetwothree","123,onetwothree,<EOF>",110))
        
    def test_id_number(self):
        """identifier with number after"""
        self.assertTrue(TestLexer.checkLexeme("onetwo12three3","onetwo12three3,<EOF>",111))
        
    def test_only_underscore(self):
        """only underscore"""
        self.assertTrue(TestLexer.checkLexeme("_____","Error Token _",112))
        
    def test_single_line_cmt(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("** Single line comment **","<EOF>",113))
        
    def test_multi_line_cmt(self):
        """multi line comment"""
        self.assertTrue(TestLexer.checkLexeme("** Multi \n line \n comment **","<EOF>",114))
        
    def test_unclosed_cmt(self):
        """unclosed comment"""
        self.assertTrue(TestLexer.checkLexeme("** unclosed comment","Unterminated Comment",115))
        
    def test_unclosed_multi_cmt(self):
        """unclosed multi line comment"""
        self.assertTrue(TestLexer.checkLexeme("** un closed \n multi \n comment","Unterminated Comment",116))
        
    def test_id_between_comment(self):
        """identifier between comment"""
        self.assertTrue(TestLexer.checkLexeme("** alo another**comment** what **","comment,<EOF>",117))
        
    def test_normal_keyword(self):
        """Normal keyword"""
        self.assertTrue(TestLexer.checkLexeme("Else ElseIf Body EndIf True False","Else,ElseIf,Body,EndIf,True,False,<EOF>",118))
        
    def test_more_normal_keyword(self):
        """another normal keyword"""
        self.assertTrue(TestLexer.checkLexeme("Break EndDo Do Var  Parameter","Break,EndDo,Do,Var,Parameter,<EOF>",119))
        
    def test_keyword_id(self):
        """keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme("True true False false","True,true,False,false,<EOF>",120))
        
    def test_keyword_nospace(self):
        """keyword without space"""
        self.assertTrue(TestLexer.checkLexeme("ElseIfElseif","ElseIf,Else,if,<EOF>",121))
        
    def test_keyword_number(self):
        """number between keyword"""
        self.assertTrue(TestLexer.checkLexeme("123Do456EndDo","123,Do,456,EndDo,<EOF>",122))
        
    def test_keyword_underscore(self):
        """keyword with underscore"""
        self.assertTrue(TestLexer.checkLexeme("If_what","If,Error Token _",123))
        
    def test_equation(self):
        """integer type operator with number"""
        self.assertTrue(TestLexer.checkLexeme("1+1==2","1,+,1,==,2,<EOF>",124))
        
    def test_equation_id(self):
        """integer type operator with id"""
        self.assertTrue(TestLexer.checkLexeme("aBx*b2==6","aBx,*,b2,==,6,<EOF>",125))
        
    def test_many_arith_operator(self):
        """only  integer type operator"""
        self.assertTrue(TestLexer.checkLexeme("=+-* \%","=,+,-,*,\,%,<EOF>",126))
        
    def test_error_int_operator(self):
        """error token with int type operator"""
        self.assertTrue(TestLexer.checkLexeme("22 / 11 > 2","22,Error Token /",127))
        
    def test_unknown_symbol(self):
        """error unknown symbol"""
        self.assertTrue(TestLexer.checkLexeme("1*2~3","1,*,2,Error Token ~",128))
        
    def test_float_int_operator(self):
        """float type operator"""
        self.assertTrue(TestLexer.checkLexeme("=++.--.","=,+,+.,-,-.,<EOF>",129))
        
    def test_float_equation(self):
        """float type operator with id and float"""
        self.assertTrue(TestLexer.checkLexeme("a*.b \ 11.2E2","a,*.,b,\,11.2E2,<EOF>",130))
        
    def test_error_float_operator(self):
        """error token float type operator"""
        self.assertTrue(TestLexer.checkLexeme("6.e2 /. 3","6.e2,Error Token /",131))
        
    def test_bool_operator(self):
        """boolean type relation"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c","a,&&,b,||,!,c,<EOF>",132))
        
    def test_bool_if(self):
        """boolean relation in if"""
        self.assertTrue(TestLexer.checkLexeme("If (a>b) && (b<c)","If,(,a,>,b,),&&,(,b,<,c,),<EOF>",133))
        
    def test_error_bool_operator(self):
        """Error boolean relation"""
        self.assertTrue(TestLexer.checkLexeme("abc|||ef","abc,||,Error Token |",134))
        
    def test_int_relation(self):
        """int type relation with number"""
        self.assertTrue(TestLexer.checkLexeme("9 >= 2 < 3","9,>=,2,<,3,<EOF>",135))
        
    def test_many_int_relation(self):
        """ only int type relation"""
        self.assertTrue(TestLexer.checkLexeme("<<>> ==!=","<,<,>,>,==,!=,<EOF>",136))
        
    def test_error_int_relation(self):
        """error token int type relation"""
        self.assertTrue(TestLexer.checkLexeme("> == >==",">,==,>=,=,<EOF>",137))
        
    def test_float_relation(self):
        """float type relation"""
        self.assertTrue(TestLexer.checkLexeme("9 >=. 2 <. 3","9,>=.,2,<.,3,<EOF>",138))
        
    def test_many_float_relation(self):
        """only float type relation"""
        self.assertTrue(TestLexer.checkLexeme("<<. =/===","<,<.,=/=,==,<EOF>",139))
        
    def test_error_relation(self):
        """error token float type relation"""
        self.assertTrue(TestLexer.checkLexeme("===/==/.=","==,=/=,=,Error Token /",140))
        
    def test_all_separators(self):
        """ normal separators"""
        self.assertTrue(TestLexer.checkLexeme("()[]{}.,;:","(,),[,],{,},.,,,;,:,<EOF>",141))
        
    def test_separator_equation(self):
        """separators with word"""
        self.assertTrue(TestLexer.checkLexeme("1 * (3 + 6) != 12.5","1,*,(,3,+,6,),!=,12.5,<EOF>",142))
        
    def test_separator_operator(self):
        """only separators"""
        self.assertTrue(TestLexer.checkLexeme("(||[&&}+.-)","(,||,[,&&,},+.,-,),<EOF>",143))
        
    def test_separator_ID(self):
        """separators with id"""
        self.assertTrue(TestLexer.checkLexeme("once upon; a time, there is.","once,upon,;,a,time,,,there,is,.,<EOF>",144))
        
    def test_separator(self):
        """separators in var declare"""
        self.assertTrue(TestLexer.checkLexeme("a[0] = 1;","a,[,0,],=,1,;,<EOF>",145))
        
    def test_normal_int(self):
        """integer literal"""
        self.assertTrue(TestLexer.checkLexeme("123456","123456,<EOF>",146))
        
    def test_negative_int(self):
        """integer literal with sign"""
        self.assertTrue(TestLexer.checkLexeme("-100","-,100,<EOF>",147))
        
    def test_hex_int(self):
        """dexadecimal with lower case"""
        self.assertTrue(TestLexer.checkLexeme("0xFF","0xFF,<EOF>",148))
        
    def test_upper_hex_int(self):
        """dexadecimal with upper case"""
        self.assertTrue(TestLexer.checkLexeme("0XABC","0XABC,<EOF>",149))
        
    def test_error_hex(self):
        """hexadechimal error"""
        self.assertTrue(TestLexer.checkLexeme("0xxXXXXX","0,xxXXXXX,<EOF>",150))
        
    def test_octa_int(self):
        """octal with lower case"""
        self.assertTrue(TestLexer.checkLexeme("0o567","0o567,<EOF>",151))
        
    def test_upper_octa_int(self):
        """octal with upper case"""
        self.assertTrue(TestLexer.checkLexeme("0O77","0O77,<EOF>",152))
        
    def test_error_octa(self):
        """error octal"""
        self.assertTrue(TestLexer.checkLexeme("0oO123456","0,oO123456,<EOF>",153))
        
    def test_int_id(self):
        """integer literral with id"""
        self.assertTrue(TestLexer.checkLexeme("123ab456","123,ab456,<EOF>",154))
        
    def test_dot_float(self):
        """float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.35","12.35,<EOF>",155))
        
    def test_double_dot(self):
        """float literal with double dot"""
        self.assertTrue(TestLexer.checkLexeme("33..33","33.,.,33,<EOF>",156))
        
    def test_exp_float(self):
        """float literal with exponent"""
        self.assertTrue(TestLexer.checkLexeme("12e3","12e3,<EOF>",157))
        
    def test_exp_op_float(self):
        """float lit with exponent and operator"""
        self.assertTrue(TestLexer.checkLexeme("12e-3","12e-3,<EOF>",158))
        
    def test_dot_exp_float(self):
        """float lit with exponent and dot"""
        self.assertTrue(TestLexer.checkLexeme("12.0e3","12.0e3,<EOF>",159))
        
    def test_dot_capital_exp_float(self):
        """float lit with upper case exponent"""
        self.assertTrue(TestLexer.checkLexeme("50.E8","50.E8,<EOF>",160))
        
    def test_exp_operator_float(self):
        """float lit with exp, operator and dot"""
        self.assertTrue(TestLexer.checkLexeme("12000.120000e-1","12000.120000e-1,<EOF>",161))
        
    def test_wrong_exp(self):
        """wrong float lit """
        self.assertTrue(TestLexer.checkLexeme("12.12e-","12.12,e,-,<EOF>",162))
        
    def test_exp_float_id(self):
        """float lit with id"""
        self.assertTrue(TestLexer.checkLexeme("123.e456fgh","123.e456,fgh,<EOF>",163))
        
    def test_error_double_exp(self):
        """error float lit with two exp"""
        self.assertTrue(TestLexer.checkLexeme("we have 12.Ee","we,have,12.,Error Token E",164))
        
    def test_wrong_two_dot_float(self):
        """wrong float lit with two dot"""
        self.assertTrue(TestLexer.checkLexeme("12.3.4","12.3,.,4,<EOF>",165))
        
    def test_space_float(self):
        """float lit with space"""
        self.assertTrue(TestLexer.checkLexeme("30.  e5","30.,e5,<EOF>",166))
        
    def test_boolean(self):
        """normal boolen literal"""
        self.assertTrue(TestLexer.checkLexeme("TrueFalse","True,False,<EOF>",167))
        
    def test_id_boolean(self):
        """boolean literal with id"""
        self.assertTrue(TestLexer.checkLexeme("TrueeFFalse","True,eFFalse,<EOF>",168))
        
    def test_error_id_boolean(self):
        """error bool lit with id"""
        self.assertTrue(TestLexer.checkLexeme("TrueEFFalse","True,Error Token E",169))
        
    def test_blankspace_boolean(self):
        """boolean literal in program"""
        self.assertTrue(TestLexer.checkLexeme(" If(a == True) Then a = False;","If,(,a,==,True,),Then,a,=,False,;,<EOF>",170))
        
    def test_error_boolean(self):
        """Error boolean literal"""
        self.assertTrue(TestLexer.checkLexeme(" If(a == Trrue)","If,(,a,==,Error Token T",171))
        
    def test_normal_string(self):
        """normal string"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string" ""","This is a string,<EOF>",172))
        
    def test_blank_string(self):
        """null string"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """,",<EOF>",173))
        
    def test_only_space_string(self):
        """only blank space string"""
        self.assertTrue(TestLexer.checkLexeme(""" "         " ""","         ,<EOF>",174))
        
    def test_missing_string(self):
        """missing double quote string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Missing double quote ""","Unclosed String: Missing double quote ",175))
        
    def test_id_string(self):
        """string with id"""
        self.assertTrue(TestLexer.checkLexeme(""" abc"defghi" ""","abc,defghi,<EOF>",176))
        
    def test_id_op_string(self):
        """string with id and operator"""
        self.assertTrue(TestLexer.checkLexeme(""" print("like" + "this")""","print,(,like,+,this,),<EOF>",177))
        
    def test_string_in_string(self):
        """string in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "outside \'"inside\'" " ""","""outside '"inside'" ,<EOF>""",178))
        
    def test_unclosed_str_in_string(self):
        """unclosed string in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "open but not\'"close " ""","""open but not'"close ,<EOF>""",179))
        
    def test_unclosed_string(self):
        """normal unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" " Do not close this""","Unclosed String:  Do not close this",180))
        
    def test_unclosed_string_newline(self):
        """unclosed string with newline"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n ""","""Unclosed String: abc\\n """,181))
        
    def test_unclosed_string_esc(self):
        """unclosed string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "def \\n" ""","""def \\n,<EOF>""",182))
        
    def test_unclosed_string_id(self):
        """unclosed string with id"""
        self.assertTrue(TestLexer.checkLexeme("""abc def xyz "what is this ""","""abc,def,xyz,Unclosed String: what is this """,183))
        
    def test_escape(self):
        """normal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "newline \\n" ""","""newline \\n,<EOF>""",184))
        
    def test_escape_str_in_str(self):
        """escape of string inside string"""
        self.assertTrue(TestLexer.checkLexeme(""" "he said:\'"hello \\n guys\'" " ""","""he said:'"hello \\n guys'" ,<EOF>""",185))
        
    def test_error_str_in_tr(self):
        """error of string inside string"""
        self.assertTrue(TestLexer.checkLexeme(""" "he said:"hello \\n guys" " ""","he said:,hello,\,n,guys, ,<EOF>",186))
        
    def test_many_escape(self):
        """many escape in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "tab \\t and newline \\n" ""","""tab \\t and newline \\n,<EOF>""",187))
        
    def test_other_escape(self):
        """other escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "backspace \\b form feed \\f" ""","""backspace \\b form feed \\f,<EOF>""",188))
        
    def test_error_unknown_escape(self):
        """error unknown escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "unknown \\k escape" ""","Illegal Escape In String: unknown \k",189))
        
    def test_error_single_quote(self):
        """error single quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "single ' quote" ""","Unclosed String: single '",190))
        
    def test_error_double_quote(self):
        """error double quote"""
        self.assertTrue(TestLexer.checkLexeme("""this is "double " quote" ""","this,is,double ,quote,Unclosed String:  ",191))
        
    def test_lexer_statement(self):
        """check lexer in statement"""
        self.assertTrue(TestLexer.checkLexeme("For (i = 0, i < 5, 2) Do x=6; EndFor.","For,(,i,=,0,,,i,<,5,,,2,),Do,x,=,6,;,EndFor,.,<EOF>",192))
        
    def test_lexer_expression(self):
        """check lexer in expression"""
        self.assertTrue(TestLexer.checkLexeme("i = i+1;","i,=,i,+,1,;,<EOF>",193))
        
    def test_keyword_expression(self):
        """keyword and expression"""
        self.assertTrue(TestLexer.checkLexeme("If(!a) Then i = i+1; EndIf.","If,(,!,a,),Then,i,=,i,+,1,;,EndIf,.,<EOF>",194))
        
    def test_comment_in_string(self):
        """comment inside string"""
        self.assertTrue(TestLexer.checkLexeme(""" " inside **string** " """," inside **string** ,<EOF>",195))
        
    def test_multiply_comment(self):
        """multiply outside comment"""
        self.assertTrue(TestLexer.checkLexeme("** ***","*,<EOF>",196))
        
    def test_comment_multiply(self):
        """multiply inside comment"""
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",197))
        
    def test_lexer_vardecl(self):
        """check lexer in variable declare"""
        self.assertTrue(TestLexer.checkLexeme("Var: c, d = 6, e, f;","Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>",198))
        
    def test_lexer_function_call(self):
        """lexer in function call"""
        self.assertTrue(TestLexer.checkLexeme("""print("print this");""","print,(,print this,),;,<EOF>",199))
        
    def test_normal_program(self):
        """normal program lexer check"""
        self.assertTrue(TestLexer.checkLexeme("Function: main Body: x = 10; EndBody.","Function,:,main,Body,:,x,=,10,;,EndBody,.,<EOF>",200))

    def test_string(self):
        """normal string"""
        self.assertTrue(TestLexer.checkLexeme(""" ""This is a string"" ""","This is a string,<EOF>",400))