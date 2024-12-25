// TO HOANG DAO  1852309

grammar MT22;

@lexer::header {
from lexererr import *
}


options{
	language=Python3;
}



program: decls EOF ;

decls: decl decls | decl;
decl: funcdec |vardec;

vardec: (var_assign | var_declare) SEMICO;
var_assign: ID COMMA var_assign COMMA expr | ID COLON var_type ASSIGN expr;
var_declare: id_list COLON var_type;
id_list: ID COMMA id_list | ID;

funcdec: ID COLON FUNCTION type_list OPENCC param_list? CLOSECC (INHERIT ID)? funcbody;
funcbody: block_statement;
param: INHERIT? OUT? ID COLON var_type;
param_list: param COMMA param_list| param;

funccall: ID OPENCC expr_list? CLOSECC ;

dimension: INTLIT COMMA dimension | INTLIT;
var_type: atomic | array_type | AUTO;
type_list: atomic | array_type | VOID | AUTO;
array_type: ARRAY OPENSQ dimension CLOSESQ OF atomic;

boolean: TRUE | FALSE;
atomic: INTEGER | FLOAT | STRING | BOOLEAN;

arraylit: OPENBR expr_list? CLOSEBR;

expr: expr1 STRCONCAT expr1 | expr1;
expr1: expr2 (EQ|DIF|SMALLER|GREATER|GREATER_EQAL|SMALLER_EQAL) expr2| expr2 ;
expr2: expr2 (AND|OR) expr3| expr3;
expr3: expr3 (PLUS|MINUS) expr4| expr4; 
expr4: expr4 (MUL|DIV|MOD) expr5| expr5; 
expr5: (NOT) expr5| expr6;
expr6: (MINUS) expr6| expr7; 
expr7: indexOp | expr8; 
expr8: ID | INTLIT | FLOATLIT | boolean | STRINGLIT | arraylit | funccall | OPENCC expr CLOSECC;
indexOp: ID OPENSQ expr_list CLOSESQ;

statement: assign_statement 
| if_statement 
| for_statement 
| while_statement
| dowhile_statement
| break_statement
| continue_statement
| return_statement
| call_statement
| block_statement ;
lhs: ID|indexOp;
assign_statement: lhs ASSIGN expr SEMICO;
if_statement: IF OPENCC expr CLOSECC statement (ELSE statement)?;
for_statement: FOR OPENCC lhs ASSIGN expr COMMA expr COMMA expr CLOSECC statement;
while_statement: while_con statement;
dowhile_statement: DO block_statement while_con SEMICO;
while_con: WHILE OPENCC expr CLOSECC;
break_statement: BREAK SEMICO;
continue_statement: CONTINUE SEMICO;
return_statement: RETURN expr? SEMICO;
call_statement: ID OPENCC expr_list? CLOSECC SEMICO;
block_statement: OPENBR (statement|vardec)* CLOSEBR;
expr_list: expr (COMMA expr)*;

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines, return, backspace, and form feed

LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

AUTO: 'auto';
BREAK: 'break';
DO: 'do';
CONTINUE: 'continue';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
INTEGER: 'integer';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
RETURN: 'return';
VOID: 'void';
OUT: 'out';
FUNCTION: 'function';
OF: 'of';
ARRAY: 'array';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
INHERIT: 'inherit';

PLUS: '+';
NOT: '!';
DIF: '!=';
MINUS: '-';
MUL:'*';
AND: '&&';
SMALLER: '<';
OR: '||';
SMALLER_EQAL: '<=';
DIV: '/';
EQ: '==';
GREATER: '>';
MOD: '%';
GREATER_EQAL: '>=';
STRCONCAT: '::';

DOT: '.';
COLON: ':';
COMMA : ',' ;
SEMICO : ';' ;
OPENCC: '(';
CLOSECC: ')';
OPENSQ: '[';
CLOSESQ: ']';
OPENBR: '{';
CLOSEBR: '}';
ASSIGN: '=';


ID: [_a-zA-Z][_a-zA-Z0-9]*;
INTLIT: [0] | [1-9]([_]?[0-9])* {self.text = self.text.replace('_', '')} ;  
FLOATLIT: (INTPART+ DOTPART? EXPPART | INTPART+ DOTPART | DOTPART EXPPART) {self.text = self.text.replace('_', '')} ;
fragment DOTPART: DOT DIGIT* ;
fragment EXPPART: ('e'|'E') [+-]? DIGIT+ ;
fragment INTPART: [0]|[1-9]+[0-9_]*;
fragment DIGIT: [0-9];

fragment StringCharacter: ~["'\\\r\n] | EscapeSequence | '\\"';
fragment EscapeSequence: '\\' [btnfr'\\];
STRINGLIT: '"' StringCharacter* '"'
    {
        self.text = (self.text)[1:-1]
    }
    ;

fragment ESC_ILLEGAL: '\\' ~[bfnrt'\\] | ~'\\';
UNCLOSE_STRING: ["](~[\\'"\b\f\r\n\t]|EscapeSequence)*EOF?{
    y = str(self.text)
    raise UncloseString(y[1:])
};
ILLEGAL_ESCAPE: ["](~[\\'"\b\f\r\n\t]|EscapeSequence)*('\\'(~[bfrnt'"\\])){
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
ERROR_CHAR: . {
    raise ErrorToken(self.text)
};