grammar Receita;

receita: inst*;

inst
	:'Ingrediente' ID #Declaracao
	| 'Adicione' INT 'de' ID #Add
	| 'Misturar' 'por' INT 'minutos' #Misturar
	| 'Assar' 'por' INT 'minutos' #Assar
	;

ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\n\r]+ -> skip;
