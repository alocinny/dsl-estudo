# Generated from Receita.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,27,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,0,
        0,2,0,2,0,0,28,0,7,1,0,0,0,2,24,1,0,0,0,4,6,3,2,1,0,5,4,1,0,0,0,
        6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,1,1,0,0,0,9,7,1,0,0,0,10,11,
        5,1,0,0,11,25,5,8,0,0,12,13,5,2,0,0,13,14,5,9,0,0,14,15,5,3,0,0,
        15,25,5,8,0,0,16,17,5,4,0,0,17,18,5,5,0,0,18,19,5,9,0,0,19,25,5,
        6,0,0,20,21,5,7,0,0,21,22,5,5,0,0,22,23,5,9,0,0,23,25,5,6,0,0,24,
        10,1,0,0,0,24,12,1,0,0,0,24,16,1,0,0,0,24,20,1,0,0,0,25,3,1,0,0,
        0,2,7,24
    ]

class ReceitaParser ( Parser ):

    grammarFileName = "Receita.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Ingrediente'", "'Adicione'", "'de'", 
                     "'Misturar'", "'por'", "'minutos'", "'Assar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_receita = 0
    RULE_inst = 1

    ruleNames =  [ "receita", "inst" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ReceitaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.InstContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.InstContext,i)


        def getRuleIndex(self):
            return ReceitaParser.RULE_receita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceita" ):
                listener.enterReceita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceita" ):
                listener.exitReceita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceita" ):
                return visitor.visitReceita(self)
            else:
                return visitor.visitChildren(self)




    def receita(self):

        localctx = ReceitaParser.ReceitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_receita)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 150) != 0):
                self.state = 4
                self.inst()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ReceitaParser.RULE_inst

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(InstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ReceitaParser.InstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ReceitaParser.INT, 0)
        def ID(self):
            return self.getToken(ReceitaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class MisturarContext(InstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ReceitaParser.InstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ReceitaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMisturar" ):
                listener.enterMisturar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMisturar" ):
                listener.exitMisturar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisturar" ):
                return visitor.visitMisturar(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracaoContext(InstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ReceitaParser.InstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ReceitaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)


    class AssarContext(InstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ReceitaParser.InstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ReceitaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssar" ):
                listener.enterAssar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssar" ):
                listener.exitAssar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssar" ):
                return visitor.visitAssar(self)
            else:
                return visitor.visitChildren(self)



    def inst(self):

        localctx = ReceitaParser.InstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_inst)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ReceitaParser.DeclaracaoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(ReceitaParser.T__0)
                self.state = 11
                self.match(ReceitaParser.ID)
                pass
            elif token in [2]:
                localctx = ReceitaParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(ReceitaParser.T__1)
                self.state = 13
                self.match(ReceitaParser.INT)
                self.state = 14
                self.match(ReceitaParser.T__2)
                self.state = 15
                self.match(ReceitaParser.ID)
                pass
            elif token in [4]:
                localctx = ReceitaParser.MisturarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(ReceitaParser.T__3)
                self.state = 17
                self.match(ReceitaParser.T__4)
                self.state = 18
                self.match(ReceitaParser.INT)
                self.state = 19
                self.match(ReceitaParser.T__5)
                pass
            elif token in [7]:
                localctx = ReceitaParser.AssarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(ReceitaParser.T__6)
                self.state = 21
                self.match(ReceitaParser.T__4)
                self.state = 22
                self.match(ReceitaParser.INT)
                self.state = 23
                self.match(ReceitaParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





