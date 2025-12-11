grammar FormFlow;

// --- Parser Rules (Sintático) ---

prog: formDef;

formDef: 'form' ID '{' question* 'end' '}';

question: 'question' ID ':' typeDef constraints*;

typeDef: ('text' | 'int' | 'float' | 'choice') STRING;

constraints
    : 'min' NUMBER          # MinVal
    | 'max' NUMBER          # MaxVal
    | 'options' stringList  # OptionsVal
    | 'ask_if' ID '==' STRING # Conditional
    ;

stringList: STRING (',' STRING)*;

// --- Lexer Rules (Léxico) ---

ID      : [a-zA-Z_][a-zA-Z0-9_]*;
STRING  : '"' .*? '"';
NUMBER  : [0-9]+ ('.' [0-9]+)?;
WS      : [ \t\r\n]+ -> skip; // Ignora espaços