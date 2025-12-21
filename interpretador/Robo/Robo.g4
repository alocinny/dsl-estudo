grammar Robo;


program: comando*;

comando
	: avancar #Move
	| repetir #Repete
	| girar #Turn
	| voltar #Back
	;

avancar: 'AVANCE' INT;
repetir: 'REPITA' INT comando+ 'FIM-REPITA';
girar: 'GIRE' INT 'GRAUS' 'A' dir;
dir: 'DIREITA' | 'ESQUERDA';
voltar: 'VOLTE' INT;

INT: [0-9]+;

WS: [ \t\r\n] -> skip;
