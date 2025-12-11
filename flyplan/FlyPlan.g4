grammar FlyPlan;

prog: defmission;

defmission: 'mission' ID LBRACE command+ RBRACE;

command
    : config #ConfigCmd
    | goto #GotoCmd
    ; 

config: 'config' 'speed' FLOAT;

goto: 'goto' ID COLON instruction+;

instruction
    : pos #PosInst
    | action #Actioninst
    | hover #HoverInst
    ;

pos: 'pos' INT INT INT;
action: 'action' (TAKEOFF | LAND);
hover: 'hover' INT;

TAKEOFF: 'takeoff';
LAND: 'land';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
INT: [0-9]+;
FLOAT: [0-9]+ ('.'[0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]-> skip;