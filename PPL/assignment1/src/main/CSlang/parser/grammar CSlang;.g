grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
//////////////////////////////////////////////////////
// CONSTTTTTTTTTTT Keywords
CLASS: 'class';
CONSTRUCTOR: 'constructor';
FUNC: 'func';
CONST: 'const';
VAR: 'var';
IF: 'if';
ELSE: 'else';
FOR: 'for';
CONTINUE: 'continue';
BREAK: 'break';
RETURN: 'return';
NULL: 'null';
SELF: 'self';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
NEW: 'new';
VOID: 'void';
TRUE: 'true';
FALSE: 'false';

// Operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
INT_DIV: '\\';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
VAR_ASSIGN: '=';
N_EQ: '!=';
LT: '<';
LT_EQ: '<=';
GT: '>';
GT_EQ: '>=';
ASSIGN: ':=';
CONCAT: '^';
MOD: '%';

// Seperators
DOT: '.';
COLON: ':';
COMMA: ',';
SEMI: ';';
L_BRACKET: '{';
R_BRACKET: '}';
L_PAREN: '(';
R_PAREN: ')';
LSQ_BRACKET: '[';
RSQ_BRACKET: ']';
INHERIT: '<-';

// Comment
OPEN_COMMENT: '/*';
CLOSE_COMMENT: '*/';
BLOCK_COMMENT: OPEN_COMMENT .*? CLOSE_COMMENT -> skip;

START_LINE_COMMENT: '//';
LINE_COMMENT: START_LINE_COMMENT (~[\r\f\n])* -> skip;

// CONSTTTTTTTTTT

program: classDecl+ EOF;

// Class Declaration
classDecl: CLASS classNameDecl L_BRACKET memDecl R_BRACKET;
classNameDecl: (ID INHERIT ID) | ID;
// Member Declaration
memDecl: (attrDecl | methodDecl | constructor)*;

// Method Declaration
constructor: FUNC CONSTRUCTOR methodParaDecl blockStmt;
methodDecl:
	FUNC identifier methodParaDecl functTypeDecl blockStmt;

functTypeDecl: COLON functionType;
methodParaDecl: L_PAREN multiTypeDecl? R_PAREN;

// Statement
blockStmt: L_BRACKET stmt* R_BRACKET;
stmt:
	assignStmt
	| ifStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| invoStmt
	| varDeclStmt
  | blockStmt;
varDeclStmt: varMutability idList COLON varType SEMI
            | varMutability varDeclStmtTail SEMI;
varDeclStmtTail: identifier COLON varType VAR_ASSIGN expr
            | identifier COMMA varDeclStmtTail COMMA expr;
assignStmt: lhs ASSIGN expr SEMI;
lhs: identifier | memberAccess | ID arrayAccess;
memberAccess: (identifier | SELF) (DOT lhs)+;
arrayAccess: LSQ_BRACKET expr RSQ_BRACKET;

ifStmt: IF blockStmt? expr blockStmt (ELSE blockStmt)?;

forStmt: FOR condForStmt SEMI expr SEMI condForStmt blockStmt;
condForStmt: ID ASSIGN expr;
continueStmt: CONTINUE SEMI;
breakStmt: BREAK SEMI;

returnStmt: RETURN SEMI | RETURN expr SEMI;

invoStmt: (instanceMethodInvo | staticMethodInvo) SEMI;
staticMethodInvo: (ID DOT)? STATIC_ID L_PAREN nullableExprList R_PAREN;
instanceMethodInvo:
	expr DOT identifier L_PAREN nullableExprList R_PAREN;

// Expression
nullableExprList: exprList |;
exprList: (expr COMMA exprList) | expr;
expr: (expr1 CONCAT expr1) | expr1;
expr1:
	(expr2 (EQ | N_EQ | LT | LT_EQ | GT | GT_EQ) expr2)
	| expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | INT_DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7:
	expr8 (LSQ_BRACKET expr RSQ_BRACKET)
	| expr8; // Array Index

expr8: expr8 DOT expr9 | expr9; // Instance invocation
expr9: expr10 DOT expr10 | expr10; // Static invocation
expr10:
	NEW ID L_PAREN nullableExprList R_PAREN
	| exprLit; // new object
exprLit:
	(
		L_PAREN expr R_PAREN
		| identifier
		| STRING_LIT
		| INT_LIT
		| FLOAT_LIT
		| bool_lit
		| arrayLit
		| SELF
		| methodAccess
		| NULL
	);

methodAccess: identifier L_PAREN nullableExprList R_PAREN;

arrayLit:
	LSQ_BRACKET elementLit (COMMA elementLit)* RSQ_BRACKET;

// Var Declaration
varMutability: (VAR | CONST);
attrDecl: varMutability idList COLON varType SEMI
            | varMutability attrDeclTail SEMI;
attrDeclTail: identifier COLON varType VAR_ASSIGN expr
            | identifier COMMA attrDeclTail COMMA expr;
varValueDecl: VAR_ASSIGN exprList;
// TYPES
multiTypeDecl: idListTypeDecl (COMMA idListTypeDecl)*;
idListTypeDecl: idList typeDecl;
typeDecl: COLON varType;
idList: identifier (COMMA identifier)*;

functionType: primitiveType | arrayType | classType;
varType: nonVoidPrimitiveType | arrayType | classType;
arrayType: LSQ_BRACKET INT_LIT RSQ_BRACKET elementType;
elementType: nonVoidPrimitiveType | classType;
elementLit:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| bool_lit
	| classType;
primitiveType: BOOL | INT | FLOAT | STRING | VOID;
nonVoidPrimitiveType: BOOL | INT | FLOAT | STRING;
classType: ID;

identifier: STATIC_ID | ID;

// Literals
STATIC_ID: '@' [_a-zA-Z0-9]+;
ID: [_a-zA-Z] ([_a-zA-Z0-9])*;

INT_LIT: [0-9]+;
ARR_LEN_LIT:
	[1-9] [0-9]*; // Array Length, Don't know why it don't work

FLOAT_LIT: INT_LIT (DECIMAL? EXPONENT | DECIMAL);
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: ('e' | 'E') (MINUS | PLUS)? [0-9]+;

STRING_LIT:
	'"' ('\\' [btnfr"'\\] | ~[\r\n\\"])* '"' {
		result = str(self.text)
		self.text = result[1:-1]
	};
fragment STRING_QUOTE: '"';
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [btnfr"'\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\';
bool_lit: TRUE | FALSE;

// Lexical Structure
WS: [ \t\r\n\b\f]+ -> skip;

// check Again
UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF) {
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};