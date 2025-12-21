# Generated from Robo.g4 by ANTLR 4.13.1
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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,3,1,3,1,3,4,3,33,8,3,11,3,12,3,34,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,
        0,7,8,47,0,17,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,29,1,0,0,0,8,38,
        1,0,0,0,10,44,1,0,0,0,12,46,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,
        16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,17,1,0,
        0,0,20,25,3,4,2,0,21,25,3,6,3,0,22,25,3,8,4,0,23,25,3,12,6,0,24,
        20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,
        0,26,27,5,1,0,0,27,28,5,10,0,0,28,5,1,0,0,0,29,30,5,2,0,0,30,32,
        5,10,0,0,31,33,3,2,1,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,3,0,0,37,7,1,0,0,0,38,39,5,4,
        0,0,39,40,5,10,0,0,40,41,5,5,0,0,41,42,5,6,0,0,42,43,3,10,5,0,43,
        9,1,0,0,0,44,45,7,0,0,0,45,11,1,0,0,0,46,47,5,9,0,0,47,48,5,10,0,
        0,48,13,1,0,0,0,3,17,24,34
    ]

class RoboParser ( Parser ):

    grammarFileName = "Robo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AVANCE'", "'REPITA'", "'FIM-REPITA'", 
                     "'GIRE'", "'GRAUS'", "'A'", "'DIREITA'", "'ESQUERDA'", 
                     "'VOLTE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "WS" ]

    RULE_program = 0
    RULE_comando = 1
    RULE_avancar = 2
    RULE_repetir = 3
    RULE_girar = 4
    RULE_dir = 5
    RULE_voltar = 6

    ruleNames =  [ "program", "comando", "avancar", "repetir", "girar", 
                   "dir", "voltar" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RoboParser.ComandoContext)
            else:
                return self.getTypedRuleContext(RoboParser.ComandoContext,i)


        def getRuleIndex(self):
            return RoboParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RoboParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 534) != 0):
                self.state = 14
                self.comando()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RoboParser.RULE_comando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoveContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RoboParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def avancar(self):
            return self.getTypedRuleContext(RoboParser.AvancarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMove" ):
                return visitor.visitMove(self)
            else:
                return visitor.visitChildren(self)


    class RepeteContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RoboParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def repetir(self):
            return self.getTypedRuleContext(RoboParser.RepetirContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepete" ):
                listener.enterRepete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepete" ):
                listener.exitRepete(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepete" ):
                return visitor.visitRepete(self)
            else:
                return visitor.visitChildren(self)


    class BackContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RoboParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def voltar(self):
            return self.getTypedRuleContext(RoboParser.VoltarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBack" ):
                listener.enterBack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBack" ):
                listener.exitBack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBack" ):
                return visitor.visitBack(self)
            else:
                return visitor.visitChildren(self)


    class TurnContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RoboParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def girar(self):
            return self.getTypedRuleContext(RoboParser.GirarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurn" ):
                listener.enterTurn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurn" ):
                listener.exitTurn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTurn" ):
                return visitor.visitTurn(self)
            else:
                return visitor.visitChildren(self)



    def comando(self):

        localctx = RoboParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = RoboParser.MoveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.avancar()
                pass
            elif token in [2]:
                localctx = RoboParser.RepeteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.repetir()
                pass
            elif token in [4]:
                localctx = RoboParser.TurnContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.girar()
                pass
            elif token in [9]:
                localctx = RoboParser.BackContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.voltar()
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


    class AvancarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RoboParser.INT, 0)

        def getRuleIndex(self):
            return RoboParser.RULE_avancar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvancar" ):
                listener.enterAvancar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvancar" ):
                listener.exitAvancar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvancar" ):
                return visitor.visitAvancar(self)
            else:
                return visitor.visitChildren(self)




    def avancar(self):

        localctx = RoboParser.AvancarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_avancar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(RoboParser.T__0)
            self.state = 27
            self.match(RoboParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RoboParser.INT, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RoboParser.ComandoContext)
            else:
                return self.getTypedRuleContext(RoboParser.ComandoContext,i)


        def getRuleIndex(self):
            return RoboParser.RULE_repetir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetir" ):
                listener.enterRepetir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetir" ):
                listener.exitRepetir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetir" ):
                return visitor.visitRepetir(self)
            else:
                return visitor.visitChildren(self)




    def repetir(self):

        localctx = RoboParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repetir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(RoboParser.T__1)
            self.state = 30
            self.match(RoboParser.INT)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.comando()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 534) != 0)):
                    break

            self.state = 36
            self.match(RoboParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GirarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RoboParser.INT, 0)

        def dir_(self):
            return self.getTypedRuleContext(RoboParser.DirContext,0)


        def getRuleIndex(self):
            return RoboParser.RULE_girar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGirar" ):
                listener.enterGirar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGirar" ):
                listener.exitGirar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGirar" ):
                return visitor.visitGirar(self)
            else:
                return visitor.visitChildren(self)




    def girar(self):

        localctx = RoboParser.GirarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_girar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(RoboParser.T__3)
            self.state = 39
            self.match(RoboParser.INT)
            self.state = 40
            self.match(RoboParser.T__4)
            self.state = 41
            self.match(RoboParser.T__5)
            self.state = 42
            self.dir_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RoboParser.RULE_dir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDir" ):
                listener.enterDir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDir" ):
                listener.exitDir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDir" ):
                return visitor.visitDir(self)
            else:
                return visitor.visitChildren(self)




    def dir_(self):

        localctx = RoboParser.DirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoltarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RoboParser.INT, 0)

        def getRuleIndex(self):
            return RoboParser.RULE_voltar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoltar" ):
                listener.enterVoltar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoltar" ):
                listener.exitVoltar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoltar" ):
                return visitor.visitVoltar(self)
            else:
                return visitor.visitChildren(self)




    def voltar(self):

        localctx = RoboParser.VoltarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_voltar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(RoboParser.T__8)
            self.state = 47
            self.match(RoboParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





