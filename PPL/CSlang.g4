grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: ID EOF ;

/****************************************************************************/
/*																	 		*/
/*								3.Lexers									*/
/* 																			*/
/****************************************************************************/
//3.1 DOWN
//3.2
LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;
//3.3
ID: [_a-zA-Z][_a-zA-Z0-9]*;
AID: '@'[_a-zA-Z0-9]+;
//3.4
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
//3.5
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
//3.6
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
//3.7
BOOLLIT: TRUE | FALSE;
INTLIT: DIGIT+;

fragment DOTPART: DOT DIGIT* ;
fragment EXPPART: [eE] [+-]? DIGIT+ ;
FLOATLIT: DIGIT+ DOTPART? EXPPART | DIGIT+ DOTPART EXPPART? ;

fragment StringCharacter: ~[\b\t\n\f\r"\\] | EscapeSequence;
fragment EscapeSequence: '\\' [btnfr"\\];
STRINGLIT: '"' StringCharacter* '"'
    {
        self.text = (self.text)[1:-1]
    };

arraylit : OPENSQ litlist CLOSESQ ;
litlist : literal (COMMA literal)* ;
literal : INTLIT
        | FLOATLIT
        | BOOLLIT
        | STRINGLIT ;	

/****************************************************************************/
/*																	 		*/
/*								4.Type										*/
/* 																			*/
/****************************************************************************/

array_type: (INT | FLOAT | BOOLEAN | STRING) OPENSQ [1-9][0-9]* CLOSESQ;

/****************************************************************************/
/*																	 		*/
/*								5.Expressions								*/
/* 																			*/
/****************************************************************************/
expressions: expr CONCAT expr | expr;
expr: expr1 (EQUAL|DIF|LESS|LESS_EQUAL|GREATER|GREATER_EQUAL) expr1 | expr1;
expr1: expr1 (AND | OR) expr2 | expr2;
expr2: expr2 ( PLUS | MINUS) expr3 | expr3;
expr3: expr3 (MUL | DIV | MOD | BSLASH) expr4 | expr4;
expr4: NOT expr4 | expr5;
expr5: MINUS expr5 | expr6;
expr6: expr7 OPENSQ expr CLOSESQ | expr7; ???????->chua biet
expr9:
	expr9 DOT ID (LB list_of_expr? RB)?
	| ID DOT ID (LB list_of_expr? RB)?
	| expr10;
expr10: NEW ID LB (list_of_expr)? RB expr10? | expr11;
expr11: LB expr RB | ID | literal | THIS | NIL;

/****************************************************************************/
/*																	 		*/
/*								6.Statements 								*/
/* 																			*/
/****************************************************************************/

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

if_statement: IF block_statement? expressions block_statement (ELSE block_statement)?;
for_statement: FOR statement SEMICO expressions SEMICO statement block_statement;
break_statement: BREAK SEMICO;
continue_statement: CONTINUE SEMICO;
return_statement: RETURN expressions? SEMICO;
block_statement: OPENBR statement* CLOSEBR;

fragment DIGIT: [0-9];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines (3.1)


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;