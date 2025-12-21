grammar Logica;

formula
		: 'all' VAR ',' formula #QuantAll
		| 'some' VAR ',' formula #QuantExist
		| formula '->' formula #Implies
		| 'not' formula #CombinadorNot
		| formula 'or' formula #CombinadorOr
		| formula 'and'	formula #CombinadorAnd
		| PRED '(' exp (',' exp)* ')' #Predicado
		| '(' formula ')' #Parens
		;

exp 
    : VAR   #Var
    | CONST #Const
    ;

VAR   : [a-z] ;       
CONST : [0-9] ;       
PRED  : [A-Z] ;       
WS    : [ \t\n\r]+ -> skip ;
