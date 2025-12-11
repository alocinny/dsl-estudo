grammar GameCfg;

prog: config;

config: 'config' ID LBRACE section+ RBRACE;

section: 'section' ID LBRACE set+ RBRACE;
    
set: 'set' ID EQUAL val;

val
    : STRING #StrVal
    | INT #IntVal
    | BOOLEAN #BooVal
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
LBRACE: '{';
RBRACE: '}';
RESOLUTION: 'resolution';
VSYNC: 'vsync';
EQUAL: '=';
MASTER_VOL: 'master_vol';
MUSIC_VOL: 'music_vol';
STRING: '"' .*? '"';
INT: [0-9]+;
BOOLEAN: 'True' | 'False'

WS: [ \t\r\n] -> skip;