grammar CSlang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}




BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
NULL: 'null';
CLASS: 'class';
CONSTRUCTOR: 'constructor';
VAR: 'var';
SELF: 'self';
NEW: 'new';
VOID: 'void';
CONST: 'const';
FUNC: 'func';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
BSLASH: '\\';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
EQ: '=';
DIF: '!=';
LESS: '<' ;
LESS_EQUAL: '<=' ;
GREATER: '>' ;
GREATER_EQUAL: '>=' ;
ASSIGN: ':=';
CONCAT: '^';
NEWOP: NEW;
MOD: '%';

DOT: '.';
COMMA: ',';
SEMICO: ';';
COLON: ':';
OPENCC: '(';
CLOSECC: ')';
OPENSQ: '[';
CLOSESQ: ']';
OPENBR: '{';
CLOSEBR: '}';

program: (class_dec)* EOF ;


class_dec: CLASS super_part? ID OPENBR member* CLOSEBR;
super_part: ID LESS MINUS;
member: attribute | method;

attribute: const_dec | var_dec;
const_dec: CONST id_list COLON at_type EQ expressions_list SEMICO;
var_dec: VAR id_list COLON at_type (EQ expressions_list)? SEMICO;
id_list: iden (COMMA iden)*;
expressions_list: expressions (COMMA expressions)*;

method: method_dec | method_con;
method_dec: FUNC iden OPENCC parameter_list? CLOSECC COLON func_type block_statement;
parameter_list: parameter (COMMA parameter)*;
parameter: id_list COLON at_type;

method_con: FUNC CONSTRUCTOR OPENCC parameter_list? CLOSECC block_statement;
at_type: 
	INT 
	| FLOAT 
	| STRING 
	| BOOL
	| array_type;
func_type: at_type | VOID;

array_type: OPENSQ INTLIT CLOSESQ (INT | FLOAT | BOOL | STRING);

expressions: expr CONCAT expr | expr;
expr: expr1 (EQUAL|DIF|LESS|LESS_EQUAL|GREATER|GREATER_EQUAL) expr1 | expr1;
expr1: expr1 (AND | OR) expr2 | expr2;
expr2: expr2 ( PLUS | MINUS) expr3 | expr3;
expr3: expr3 (MUL | DIV | MOD | BSLASH) expr4 | expr4;
expr4: NOT expr4 | expr5;
expr5: MINUS expr5 | expr6;
expr6: expr7 OPENSQ expressions CLOSESQ | expr7; 
expr7: expr7 DOT ID | expr7 DOT ID OPENCC expr_list? CLOSECC| expr8;
expr8: (expr9 DOT)? At | (expr9 DOT)? At OPENCC expr_list? CLOSECC| expr9;
expr9: NEW ID OPENCC expr_list? CLOSECC | expr10;
expr10: OPENCC expressions CLOSECC | iden | INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit | SELF;  //not use boollit use true false directly
expr_list: expressions (COMMA expressions)*;

statement: 
	vardec_statement
	| assign_statement
	| if_statement
	| for_statement
	| break_statement
	| continue_statement   
	| method_statement
	| return_statement
	| block_statement;

vardec_statement: attribute;
assign_statement: expressions ASSIGN expressions SEMICO;
if_statement: IF pre_statement? expressions block_statement (ELSE block_statement)?;
pre_statement: block_statement;
for_statement: FOR for_condition SEMICO expressions SEMICO for_condition block_statement;
for_condition: expressions ASSIGN expressions; 
break_statement: BREAK SEMICO;
continue_statement: CONTINUE SEMICO;
method_statement: expr8 SEMICO;
return_statement: RETURN expressions? SEMICO;
block_statement: OPENBR statement* CLOSEBR;

arraylit : OPENSQ litlist CLOSESQ ;
litlist : literal (COMMA literal)* ;
literal : INTLIT
        | FLOATLIT
        | boollit
        | STRINGLIT ;	

LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

iden: ID | At;
At: '@' [_a-zA-Z0-9]+;
ID: [_a-zA-Z][_a-zA-Z0-9]*;

boollit: TRUE | FALSE;
INTLIT: DIGIT+;

fragment DOTPART: DOT DIGIT* ;
fragment EXPPART: [eE] [+-]? DIGIT+ ;
FLOATLIT: DIGIT+ DOTPART? EXPPART | DIGIT+ DOTPART EXPPART? ;

fragment StringCharacter: ~["'\\\r\n] | EscapeSequence | '\'""';
fragment EscapeSequence: '\\' [btnfr'\\];
STRINGLIT: '"' StringCharacter* '"'
    {
        self.text = (self.text)[1:-1]
    }
    ;

fragment DIGIT: [0-9];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines (3.1)

fragment ESC_ILLEGAL: '\\' ~[bfnrt'\\] | ~'\\';
ERROR_CHAR: .;
UNCLOSE_STRING: '"' StringCharacter* ([\b\f\n\r\t"'\\] | EOF)
    {
        self.text = (self.text)[1:]
    };
ILLEGAL_ESCAPE: '"' StringCharacter* ESC_ILLEGAL
    {
        self.text = (self.text)[1:]
    };