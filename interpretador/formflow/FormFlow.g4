grammar FormFlow;

formulario: 'form' ID '{' question* 'end' '}';

question: 'question' ID ':' tipo STR configs*;

tipo: 'text' | 'int' | 'choice' | 'float';

configs
	: 'min' NUM #ConfigMin
	| 'max'NUM #ConfigMax
	| 'options' STR (',' STR)* #ConfigOptions
	| 'ask_if' ID '==' STR #ConfigIf
	;

ID   : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM  : [0-9]+('.'[0-9]+)? ;
STR  : '"' (~'"')* '"' ;
WS   : [ \t\n\r]+ -> skip ;
