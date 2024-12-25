grammar BKIT;
// 1852247
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
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

 // program  : VAR COLON ID SEMI EOF ;
program : vardecls? funcdecls EOF ;
vardecls: vardecl+ ;
funcdecls: funcdecl* ;

// Global variable declaration part
vardecl: VAR COLON varlist SEMI;
varlist: var (COMMA var)* ;
var: var_array | var_scalar ;
var_scalar: ID (ASSIGN literal)?;
var_array: ID index_op+ (ASSIGN literal)?;

// Function declaration part
funcdecl: FUNCTION COLON ID (PARAMETER COLON paralist)? body ;
paralist: var (COMMA var)* ;
body: BODY COLON nullstmt ENDBODY DOT ;

ID: [a-z][A-Za-z_0-9]* ;

/* Comment */
COMMENT: '**' .*? '**' -> skip ;

/* Keywords */
BODY: 'Body' ;
BREAK: 'Break' ;
CONTINUE: 'Continue';
DO: 'Do' ;
ELSE: 'Else' ;
ELSEIF: 'ElseIf' ;
ENDBODY: 'EndBody' ;
ENDIF: 'EndIf' ;
ENDFOR: 'EndFor' ;
ENDWHILE: 'EndWhile' ;
FOR: 'For' ;
FUNCTION: 'Function' ;
IF: 'If' ;
PARAMETER: 'Parameter' ;
RETURN: 'Return' ;
THEN: 'Then' ;
VAR: 'Var';
WHILE: 'While';
ENDDO: 'EndDo' ;


ASSIGN: '=';
/* Arithmetic operators */
// Int Type
ADD: '+' ;
SUB: '-' ;
MULTIPLY: '*' ;
DIVIDE: '\\' ;
REMAINDER: '%' ;

// Float Type
FLOAT_ADD: '+.' ;
FLOAT_SUB: '-.' ;
FLOAT_MULTIPLY: '*.' ;
FLOAT_DIVIDE: '\\.' ;
FLOAT_REMAINDER: '%.' ;

/* Boolean Type */
NOT: '!' ;
AND: '&&' ;
OR: '||' ;

/* Relational operators */
// Int type
EQUAL: '==' ;
NOT_EQUAL: '!=' ;
LESS: '<' ;
LESS_EQUAL: '<=' ;
GREATER: '>' ;
GREATER_EQUAL: '>=' ;

// FLOAT type
FLOAT_NOT_EQUAL: '=/=' ;
FLOAT_LESS: '<.' ;
FLOAT_LESS_EQUAL: '<=.' ;
FLOAT_GREATER: '>.' ;
FLOAT_GREATER_EQUAL: '>=.' ;

/* SEPARATORS */
SEMI: ';' ;
COLON: ':' ;
DOT: '.' ;
COMMA: ',' ;
LR: '(';
RR: ')';
LS: '[';
RS: ']';
LC: '{';
RC: '}';

/* LITERALS */
// Integer literal
fragment DEC: '0'|[1-9][0-9]* ;
fragment HEX: [0][xX][0-9A-F]+ ;
fragment OCT: [0][oO][0-7]+ ;
INTLIT: DEC|HEX|OCT ;


// Float literal
fragment WITH_DOT: '.'[0-9]* ;
fragment WITH_EXP: [eE][+-]?[0-9]+ ;
FLOATLIT: [0-9]+ WITH_DOT? WITH_EXP | [0-9]+ WITH_DOT WITH_EXP? ;

// Boolean literal
BOOLLIT: 'True' | 'False' ;

//String literal
fragment StringCharacter: ~["'\\\r\n] | EscapeSequence | '\'"';
fragment EscapeSequence: '\\' [btnfr'\\];
STRINGLIT: '"' StringCharacter* '"'
    {
        self.text = (self.text)[1:-1]
    }
    ;


// Array literal
arraylit : LC litlist RC ;
litlist : literal (COMMA literal)* ;
literal : INTLIT
        | FLOATLIT
        | BOOLLIT
        | STRINGLIT
        | arraylit ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// Expression
expression: expr1 (EQUAL|NOT_EQUAL|FLOAT_NOT_EQUAL|LESS|LESS_EQUAL|GREATER|GREATER_EQUAL|FLOAT_LESS|FLOAT_LESS_EQUAL|FLOAT_GREATER|FLOAT_GREATER_EQUAL) expr1 | expr1;
expr1: expr1 (AND|OR) expr2 | expr2;
expr2: expr2 (ADD|FLOAT_ADD|SUB|FLOAT_SUB) expr3 | expr3 ;
expr3: expr3 (MULTIPLY|FLOAT_MULTIPLY|DIVIDE|FLOAT_DIVIDE|REMAINDER|FLOAT_REMAINDER) expr4 | expr4 ;
expr4: NOT expr4 | expr5;
expr5: (SUB|FLOAT_SUB) expr5 | expr6;
expr6: funccall | literal | LR expression RR | assignvar;


// Index operator
element_expr: (ID|funccall) index_op+ ;
funccall: ID LR exprlist? RR ;
index_op: (LS expression RS) ;


nullstmt: vardeclstmt* otherstmt* ;
stmtlst: vardeclstmt+ otherstmt* | vardeclstmt* otherstmt+ ;
otherstmt: assignstmt|ifstmt|forstmt|whilestmt|dowhilestmt|breakstmt|continuestmt|callstmt|returnstmt ;
// Variable declaration statement
vardeclstmt: vardecl;

// Assignment
assignstmt: assignvar ASSIGN expression SEMI ;
assignvar: ID index_op* ;
// If Statement
ifstmt: ifthenStmt elseStmt ;
ifthenStmt: IF expression THEN stmtlst (ELSEIF expression THEN stmtlst)* ;
elseStmt: (ELSE stmtlst)? ENDIF DOT ;

// For statement
forstmt: FOR LR ID ASSIGN expression COMMA expression COMMA expression RR DO stmtlst ENDFOR DOT ;

// While statement
whilestmt: WHILE expression DO stmtlst ENDWHILE DOT;

// Do-while statement
dowhilestmt: DO stmtlst WHILE expression ENDDO DOT ;

// Break statement
breakstmt: BREAK SEMI ;

// Continue statement
continuestmt: CONTINUE SEMI ;

// Return statement
returnstmt: RETURN expression? SEMI ;

// Call stmt
callstmt: ID LR exprlist RR SEMI ;
exprlist: expression (COMMA expression)* ;

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
UNTERMINATED_COMMENT: '**'.*?;
