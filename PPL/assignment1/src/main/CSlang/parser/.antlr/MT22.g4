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
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

array_type: ARRAY OPENSQ dimension CLOSESQ OF atomic;
dimension: INTLIT (COMMA INLIT)*;
boolean: TRUE | FALSE;
type: atomic | array_type | VOID | AUTO;
atomic: INT | FLOAT | STRING | boolean;

arraylit: OPENBR expr_list CLOSEBR;
expr_list: expr (COMMA expr)*;





vardec: id_list COLON type (OPENSQ ASSIGN expr_list2 CLOSESQ)? SEMICO;
id_list: ID (COMMA ID)?;

param: (OPENSQ INHERIT CLOSESQ)? (OPENSQ out CLOSESQ)? ID COLON type;

funcdec: ID COLON FUNCTION type OPENCC param_list CLOSECC (OPENSQ INHERIT ID CLOSESQ)?;
param_list: param (COMMA param)*;

indexOp: ID OPENSQ expr_list3 CLOSESQ;
expr: expr1 STRCONCAT expr1 | expr1;
expr1: expr2 (EQ|DIF|SMALLER|GREATER|GREATER_EQAL|SMALLER_EQAL) expr2| expr2 ;
expr2: expr2 (AND|OR) expr3| expr3;
expr3: expr3 (PLUS|MINUS) expr4| expr4; 
expr4: expr4 (MUL|DIV|MOD) expr5| expr5; 
expr5: (NOT) expr5| expr6;
expr6: (MINUS) expr6| expr7; 
expr7: indexOp | expr8; 
//expr8: ID|numOperand|booleanOperand|stringOperand|relationalOperand|callexpr|subexpr|arraylit;
expr8: ID | INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit;

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
assign_statement: expr ASSIGN expr SEMICO;
if_statement: IF OPENCC expr CLOSECC statement (ELSE statement)?;
for_statement: FOR OPENCC ID ASSIGN expr COMMA expr COMMA expr CLOSECC statement;
while_con: WHILE OPENCC expr CLOSECC;
while_statement: while_con statement;
dowhile_statement: DO block_statement while_con;
break_statement: BREAK SEMICO;
continue_statement: CONTINUE SEMICO;
return_statement: RETURN expr? SEMICO;
//call_statement:;
block_statement: OPENBR (statement|vardec)* CLOSEBR;




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
INTLIT: [0]|[1-9][0-9_]* {self.text = self.text.replace("_", "")} ;
FLOATLIT: INTPART+ DOTPART? EXPPART | INTPART+ DOTPART EXPPART? | DOTPART EXPPART; {self.text = self.text.replace("_", "")} ;
fragment DOTPART: DOT DIGIT* ;
fragment EXPPART: (eE) [+-]? DIGIT+ ;
fragment INTPART: [0]|[1-9]+[0-9_]*;
fragment DIGIT: [0-9];

fragment StringCharacter: ~["'\\\r\n] | EscapeSequence | '\'""';
fragment EscapeSequence: '\\' [btnfr'\\];
STRINGLIT: '"' StringCharacter* '"'
    {
        self.text = (self.text)[1:-1]
    }
    ;

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