import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
        
    def test_simple_program(self):
        """ Simple program: int main() {} """
        input = """ Var: x; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))
        
    def test_wrong_miss_close(self):
        """ Miss variable """
        input = """ Var:; """
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))
        
    def test_null_program(self):
        """ Null program """
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))
        
    def test_blankspace_program(self):
        """ Program with only blank space """
        input = """                           """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))
        
    def test_var_decl(self):
        """ One var declare with assign """
        input = """ Var: a = 5; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))
        
    def test_many_var_decl(self):
        """ Many vars declare """
        input = """ Var: c, d = 6, e, f; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))
        
    def test_array_var_decl(self):
        """ Array var declare """
        input = """ Var: m, n[10]; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))
        
    def test_compo_var_decl(self):
        """ 2 dimension array var declare """
        input = """ Var: b[2][3] = {{2, 3, 4}, {4, 5, 6}}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))
        
    def test_another_intlit_var(self):
        """  """
        input = """ Var: abc[0o567][0XABC]; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))
        
    def test_wrong_func_decl(self):
        """ Wrong function declare """
        input = """ int main() {} """
        expect = "Error on line 1 col 1: int"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
        
    def test_program(self):
        """ Normal program """
        input = """
        Function: main
            Body:
                x = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
        
    def test_oneline_program(self):
        """ Normal one line program """
        input = """ Function: main Body: x = 10; EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
        
    def test_missing_dot(self):
        """ Missing dot at EndBody """
        input = """
        Function: main
            Body:
                x = 10;
            EndBody
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
        
    def test_missing_semicolon(self):
        """ Missing semicolon at assign statement """
        input = """
        Function: main
            Body:
                x = 10
            EndBody.
        """
        expect = "Error on line 5 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
        
    def test_program_comment(self):
        """ Commented program """
        input = """ ** Function: main Body: x = 10; EndBody. ** """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
        
    def test_cmt_in_program(self):
        """ Comments in program """
        input = """
        Function: main
            Body:
                ** Assign x equal to 10 **
                x = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))
        
    def test_multiline_cmt_program(self):
        """ Multi line comment in program """
        input = """
        Function: main
            Body:
                ** Assign
                x equal
                to 10 **
                x = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
        
    def test_wrong_position_program(self):
        """ Error var declare outside body """
        input = """
        x = 10;
        Function: main
            Body:
            EndBody.
        """
        expect = "Error on line 2 col 8: x"
        self.assertTrue(TestParser.checkParser(input, expect, 218))
        
    def test_composite_para(self):
        """ Composite parameter """
        input = """
        Function: main
            Body:
                x[0][0xE3] = 22;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))
        
    def test_empty_body(self):
        """ Empty body program """
        input = """
        Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))
        
    def test_var_stmt(self):
        """ Integer type operation """
        input = """
        Function: main
            Body:
                x = 1 + 2 * 3 \\ 4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))
        
    def test_op_expr_stmt(self):
        """ Integer type operation with separator """
        input = """
        Function: main
            Body:
                x = (1 + 1) * (4 - 5);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))
        
    def test_intlit_id_expr_stmt(self):
        """ Intlit  with id """
        input = """
        Function: main
            Body:
                x = 2 + y;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
        
    def test_error_assign_index(self):
        """ Wrong assign variable to index """
        input = """
        Function: main
            Body:
                x = [10];
            EndBody.
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.checkParser(input, expect, 224))
        
    def test_float_assign(self):
        """ Assign float to variable """
        input = """
        Function: main
            Body:
                x = 1.2 +. 3.4 -. 1.5;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
        
    def test_error_relation_expr(self):
        """ Wrong relation expression """
        input = """
        Function: main
            Body:
                a > b
            EndBody.
        """
        expect = "Error on line 4 col 18: >"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
        
    def test_para(self):
        """ Normal parameter """
        input = """
        Function: main
            Parameter: n
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
        
    def test_multi_para(self):
        """ Multiple parameters """
        input = """
        Function: main
            Parameter: n, i, f = 0
            Body:
            EndBody.
        """
        expect = "Error on line 3 col 31: ="
        self.assertTrue(TestParser.checkParser(input, expect, 228))
        
    def test_index_para(self):
        """ Index parameter """
        input = """
        Function: main
            Parameter: i[2]
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
        
    def test_ifstmt(self):
        """ Normal if statement """
        input = """
        Function: main
            Body:
                If a
                Then
                    b = 0;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
        
    def test_missing_endif(self):
        """ Error no EndIf """
        input = """
        Function: main
            Body:
                If a
                Then
                    b = 0;
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
        
    def test_else_ifstmt(self):
        """ If statement with else """
        input = """
        Function: main
            Body:
                If a
                Then
                    b = 0;
                Else 
                    c = 0;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
        
    def test_elseif_ifstmt(self):
        """ If statement with elseif """
        input = """
        Function: main
            Body:
                If a
                Then
                    b = 0;
                Elseif c
                Then
                    d = 0;
                Else Then
                    e = 0;
                EndIf.
            EndBody.
        """
        expect = "Error on line 7 col 23: c"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
        
    def test_expr_cond_ifstmt(self):
        """ Expression on if condition """
        input = """
        Function: main
            Body:
                If a == 0
                Then
                    b = 25 % b;
                Else 
                    c = (a + b);
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
        
    def test_expr_cond_ifstmt_2(self):
        """ Another Expression on if condition """
        input = """
        Function: main
            Body:
                If (a > 0) && (b != 0)
                Then
                    c = -b;
                Else
                    c = c \\ a;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
        
    def test_expr_float_ifstmt(self):
        """ Expression on if condition with float """
        input = """
        Function: main
            Body:
                If (a =/= 1.0) || (b <=. 2.0)
                Then
                    b = a*.b;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))
        
    def test_error_expr_ifstmt(self):
        """ Error expression in if statement """
        input = """
        Function: main
            Body:
                If a = 0
                Then
                    b = 0;
                EndIf.
            EndBody.
        """
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 237))
        
    def test_ifstmt_in_ifstmt(self):
        """ If statement in if statement """
        input = """
        Function: main
            Body:
                If a == 0
                Then If a < 3
                    Then
                       a = 2;
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))
        
    def test_equation_expr_ifstmt(self):
        """ If statement condition with equation """
        input = """
        Function: main
            Body:
                If (a+b==0) && (1-1!=0)
                Then
                    c = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))
        
    def test_returnstmt(self):
        """ Return statement """
        input = """
        Function: main
            Body:
                If a == 0
                Then
                    Return 0;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
        
    def test_many_returnstmt(self):
        """ Many return statement """
        input = """
        Function: main
            Body:
                If a == 0
                Then
                    Return 0;
                Else Then
                    Return a;
                EndIf.
            EndBody.
        """
        expect = "Error on line 7 col 21: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
        
    def test_recursive_ifstmt(self):
        """Recursive in function"""
        input = """
        Function: main
            Body:
                a = 5;
                If a > 0
                Then
                    main(a - 1);
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_oneline_for_loop(self): 
        """ One line for statement """
        input = """ For (i = 0, i < 5, 2) Do x=6; EndFor. """
        expect = "Error on line 1 col 1: For"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_normal_for(self): 
        """ Normal for statement """
        input = """ Function: main
            Body:
                For (i = 0, i < 5, 2) 
                Do x=0; 
                EndFor.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_funccall_for(self): 
        """ Function call in for statement """
        input = """ Function: main
            Body:
                For (i = 0, i < 5, 2) 
                Do print(i); 
                EndFor.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_error_expr_for(self): 
        """ Error expression in for statement """
        input = """ Function: main
            Body:
                For (i == 0, i < 5, i=i+1) 
                Do print(i); 
                EndFor.
            EndBody. """
        expect = "Error on line 3 col 23: =="
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_if_for(self): 
        """ If statement in for statement """
        input = """ Function: main
            Body:
                For (i = 0, i < 5, 2) 
                Do If !a
                    Then a=1;
                    EndIf. 
                EndFor.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_break_for(self):
        """ Break statement in for statement """
        input = """ Function: main
            Body:
                For (i = 0, i < 5, 2) 
                Do If !a
                    Then Break;
                    EndIf. 
                EndFor.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_continue_for(self): 
        """ Continue statement in for statement """
        input = """ Function: main
            Body:
                For (i = 0, i < 5, 2) 
                Do If !a
                    Then Break;
                    Else Continue;
                    EndIf. 
                EndFor.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_return_for(self): 
        """ Return statement in for """
        input = """ Function: main
        Body:
            For (i = 0, i < 5, i+1) Do
                If !a
                Then Return 0;
                Else Continue;
                EndIf. 
            EndFor.
        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_empty_condition_for(self): 
        """ Empty condition in for statement """
        input = """ Function: main
            Body:
                For (,,) 
                Do print(i); 
                EndFor.
            EndBody. """
        expect = "Error on line 3 col 21: ,"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_composite_for(self): 
        """ Error composite in for statement """
        input = """ Function: main
            Body:
                For (i[0] = 0, i < 5, i=i+1) 
                Do print(i); 
                EndFor.
            EndBody. """
        expect = "Error on line 3 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_while(self): 
        """ One line while statement """
        input = """ Function: main Body: While i < 5 Do a[0] = b +. 1.0; i = i + 1; EndWhile. EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_normal_while(self): 
        """ Normal multiline while statement """
        input = """ Function: main 
            Body:
                While i < 5 
                Do 
                    a[0] = b +. 1.0; 
                    i = i + 1; 
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_empty_condition_while(self): 
        """ Empty condition in while statement """
        input = """ Function: main 
            Body:
                While()
                Do 
                    a[0] = 10; 
                    i = i + 1; 
                EndWhile. 
            EndBody. """
        expect = "Error on line 3 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_if_while(self): 
        """ If statement in while statement """
        input = """ Function: main 
            Body:
                While x<2
                Do 
                    If a > 2
                    Then a=1;
                    EndIf.
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_break_while(self): 
        """ Break statement in while statement """
        input = """ Function: main 
            Body:
                While x<2
                Do 
                    If a > 2
                    Then Break;
                    EndIf.
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_continue_while(self): 
        """ Continue statement in while """
        input = """ Function: main 
            Body:
                While i<10
                Do 
                    If i == 4
                    Then 
                        i=i+1;
                    Continue;
                    EndIf.
                    print(i);
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_return_while(self): 
        """ Return statement in while """
        input = """ Function: main 
        Body:
            While i<10
            Do 
                If i == 4
                Then 
                    Return 3*i;
                EndIf. 
            EndWhile. 
        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_error_expr_while(self): 
        """ Error expr in while statement """
        input = """ Function: main 
            Body:
                While x+2
                Do 
                    If a > 2
                    Then Break;
                    EndIf.
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_empty_stmt_while(self): 
        """ Empty statement in while stmt """
        input = """ Function: main 
            Body:
                While x+2
                Do 
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_dowhile(self): 
        """ One line do while statement """
        input = """ Function: main Body: Do a[0] = b +. 1.0; i = i + 1; While i < 5 EndDo. EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_normal_dowhile(self): 
        """ Multiline do while statement """
        input = """ Function: main
            Body: 
                Do
                    x = a + b;
                    writeln(x);
                While(a > b)
                EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_empty_cond_dowhile(self): 
        """ Empty condition in do while statement """
        input = """ Function: main
            Body: 
                Do
                    x = a + b;
                    writeln(x);
                While 
                EndDo.
            EndBody. """
        expect = "Error on line 7 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_empty_expr_dowhile(self): 
        """ Empty expression in do while statement """
        input = """ Function: main
            Body: 
                Do 
                While(a==b)
                EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_if_dowhile(self): 
        """ If statement in do while statement """
        input = """ Function: main
            Body: 
            Do 
                If a > 2
                Then a=0;
                EndIf.
            While(a==b)
            EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_break_dowhile(self): 
        """ Break statement in do while statement """
        input = """ Function: main
            Body: 
            Do 
                If a > 2
                Then Break;
                EndIf.
            While(a==b)
            EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_continue_dowhile(self): 
        """ Continue statement in do while statement """
        input = """ Function: main
        Body: 
            Do 
                If a > 2
                Then Break;
                Else Continue;
                EndIf.
            While(a==b)
            EndDo.
        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_return_dowhile(self): 
        """ Return statement in dowhile """
        input = """ Function: main
            Body: 
            Do 
                If a > 2
                Then Return a;
                Else Continue;
                EndIf.
            While(a==b)
            EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_while_dowhile(self): 
        """ While statement in do while statement """
        input = """ Function: main
            Body: 
            Do 
                While i < 5 
                Do 
                    a[0] = b +. 1.0; 
                    i = i + 1; 
                EndWhile. 
            While a==b
            EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_error_enddo(self): 
        """ Many enddo """
        input = """ Function: main
        Body: 
            Do 
                If a > 2
                    Then a=0;
                EndIf.
            While(a==b)
            EndDo.
            EndDo.
        EndBody. """
        expect = "Error on line 9 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_many_stmt_dowhile(self): 
        """ Dowhile with many statement """
        input = """ Function: main
            Body: 
                Do 
                    If a > 2
                        Then a=0;
                    EndIf.
                While((a==b)&&(a<c))
                EndDo.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_many_stmt_while(self): 
        """ While with many statement """
        input = """ Function: main 
            Body:
                While (x<2)||(a==0)
                Do 
                    If a > 2
                        Then Break;
                    EndIf.
                EndWhile. 
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_boolean(self): 
        """ Boolean expression """
        input = """ 
            Function: main
                Body: 
                    x = !False;
                    y = (False || True) && (True || False);
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_index_op(self): 
        """ Index operator """
        input = """ 
            Function: main
                Body: 
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_complicated_index(self): 
        """ Complicated Index """
        input = """ Function: main
            Body: 
                x[a[3+foo(2)]][(2>1) && False] = y[1+1==2][True||False||1.2>.3.2][0];
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_vardecl_program(self): 
        """ Program with variable declare """
        input = """ Function: main
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_vardecl_not_first(self): 
        """ Variable declare not first statement """
        input = """ Function: main
            Body:
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Var: r = 10., v;
            EndBody. """
        expect = "Error on line 4 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_vardecl_not_first_instmt(self): 
        """ Variable declare not first in while statement """
        input = """ Function: main
            Body: 
            Var: i = 0;
                While i < 5 Do
                    Var: k = 10;
                    i = i + 1;
                EndWhile.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_vardecl_first(self): 
        """ Variable declare first """
        input = """ Function: main
            Body: 
                Var: i = 0;
                While i < 5 Do
                    Var: k = 10;
                    i = i + 1;
                EndWhile.
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_array_literal(self): 
        """ Array literal """
        input = """ Function: main
            Body: 
                a[3] = {10,15,20};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_two_dim_array(self): 
        """ Two dimension array literal """
        input = """ Function: main
            Body: 
                a[2][3] = {{10,15,20},{1,2,3}};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_array_with_space(self): 
        """ Array with blank space """
        input = """ Function: main
            Body: 
                a[3] = {10      ,   15   ,20};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_empty_item_array(self):
        """ Array with no item """
        input = """ Function: main
            Body: 
                a[3] = {};
            EndBody. """
        expect = "Error on line 3 col 24: }"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_array_empty_index(self): 
        """ Array with no index """
        input = """ Function: main
            Body: 
                a[] = {1,2,3};
            EndBody. """
        expect = "Error on line 3 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_empty_array(self): 
        """ Empty array """
        input = """ Function: main
            Body: 
                a[] = {};
            EndBody. """
        expect = "Error on line 3 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_different_item_array(self): 
        """ Array with different type of element """
        input = """ Function: main
            Body: 
                a[1] = {1,"abc",3};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_diff_item_indim_array(self): 
        """ Array with different type of element in dimension """
        input = """ Function: main
            Body: 
                a[2] = {{1,3},{"a","b"}};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_comment_array(self): 
        """ Comment inside array """
        input = """ Function: main
            Body: 
                a[3] = {1,3**comment**};
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_error_semi_array(self): 
        """ Array with semicolon inside """
        input = """ Function: main
            Body: 
                a[5] = {1;2;3};
            EndBody. """
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,290))
        
    def test_error_semi_dim(self): 
        """ Array with semicolon between subarray """
        input = """ Function: main
            Body: 
                a[2][3] = {{10,15,20};{1,2,3}};
            EndBody. """
        expect = "Error on line 3 col 37: ;"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    
    def test_array_for(self): 
        """ Array in for loop """
        input = """ Function: main
            Body:
                For (i[0] = 0, i < 5, i=i+1) 
                    Do a[i] = a[i] + 1; 
                EndFor.
            EndBody. """
        expect = "Error on line 3 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_empty_array_for(self): 
        """ Empty array in for loop """
        input = """ Function: main
        Body:
            For (i[0] = 0, i < 5, i=i+1) 
                Do a[] = a[] + 1; 
            EndFor.
        EndBody. """
        expect = "Error on line 3 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,293))
    
    def test_var_comment(self): 
        """ Comment in variable declare """
        input = """ 
            Var **this is vardecl**: x=2;
            Function: main
                Body:
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    
    def test_no_name_function(self): 
        """ Function without name """
        input = """ Function:
            Body: 
                a[3] = {10,15,20};
            EndBody. """
        expect = "Error on line 2 col 12: Body"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_sign_operator(self): 
        """ Sign operator """
        input = """ Function: main
            Body: 
                a = -10;
                b = -0o567;
                c = -0xFFE;
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_funccall(self): 
        """ Function call """
        input = """ Function: main
            Body: 
                print(x);
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_funccall_semi(self):
        """ Function call with semicolon inside """
        input = """ Function: main
            Body: 
                print(a,b,0,"abc");
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    
    def test_funccall_many_para(self): 
        """ Function call with many parameter """
        input = """ Function: main
            Body: 
                print(a;b;c=0);
            EndBody. """
        expect = "Error on line 3 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_funcall_funcall(self): 
        """ Function call inside function call """
        input = """ Function: main
            Body: 
                print(sum(add(22, 11)));
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
    def test_many_functions(self):
        """ Many functions in program """
        input = """ Var: x;
            Function: fact
            Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))
