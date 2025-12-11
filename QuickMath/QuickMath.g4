grammar QuickMath;

prog: program;

program: 'program' ID LBRACE commands+ RBRACE;

commands
    : stat #StatCmd
    | show #ShowCmd
    ;

stat: 'var' ID EQUAL INT;
show: 'show' expr;
expr
    : expr MULT expr #MultExpr
    | expr SUM expr #SumExpr
    | ID #IdExpr
    | INT #IntExpr
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
SUM: '+';
MULT: '*';
LBRACE: '{';
RBRACE: '}';
EQUAL: '=';
WS: [ \t\r\n] -> skip