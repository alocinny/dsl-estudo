# Generated from FormFlow.g4 by ANTLR 4.13.1
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
        4,1,20,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,27,
        8,1,10,1,12,1,30,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        42,8,3,10,3,12,3,45,9,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,3,0,0,4,0,2,
        4,6,0,1,1,0,7,10,54,0,8,1,0,0,0,2,20,1,0,0,0,4,31,1,0,0,0,6,50,1,
        0,0,0,8,9,5,1,0,0,9,10,5,17,0,0,10,14,5,2,0,0,11,13,3,2,1,0,12,11,
        1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,17,1,0,0,0,
        16,14,1,0,0,0,17,18,5,3,0,0,18,19,5,4,0,0,19,1,1,0,0,0,20,21,5,5,
        0,0,21,22,5,17,0,0,22,23,5,6,0,0,23,24,3,4,2,0,24,28,5,19,0,0,25,
        27,3,6,3,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,
        0,29,3,1,0,0,0,30,28,1,0,0,0,31,32,7,0,0,0,32,5,1,0,0,0,33,34,5,
        11,0,0,34,51,5,18,0,0,35,36,5,12,0,0,36,51,5,18,0,0,37,38,5,13,0,
        0,38,43,5,19,0,0,39,40,5,14,0,0,40,42,5,19,0,0,41,39,1,0,0,0,42,
        45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,51,1,0,0,0,45,43,1,0,0,
        0,46,47,5,15,0,0,47,48,5,17,0,0,48,49,5,16,0,0,49,51,5,19,0,0,50,
        33,1,0,0,0,50,35,1,0,0,0,50,37,1,0,0,0,50,46,1,0,0,0,51,7,1,0,0,
        0,4,14,28,43,50
    ]

class FormFlowParser ( Parser ):

    grammarFileName = "FormFlow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'form'", "'{'", "'end'", "'}'", "'question'", 
                     "':'", "'text'", "'int'", "'choice'", "'float'", "'min'", 
                     "'max'", "'options'", "','", "'ask_if'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "STR", "WS" ]

    RULE_formulario = 0
    RULE_question = 1
    RULE_tipo = 2
    RULE_configs = 3

    ruleNames =  [ "formulario", "question", "tipo", "configs" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ID=17
    NUM=18
    STR=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormularioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FormFlowParser.ID, 0)

        def question(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormFlowParser.QuestionContext)
            else:
                return self.getTypedRuleContext(FormFlowParser.QuestionContext,i)


        def getRuleIndex(self):
            return FormFlowParser.RULE_formulario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormulario" ):
                listener.enterFormulario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormulario" ):
                listener.exitFormulario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormulario" ):
                return visitor.visitFormulario(self)
            else:
                return visitor.visitChildren(self)




    def formulario(self):

        localctx = FormFlowParser.FormularioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formulario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(FormFlowParser.T__0)
            self.state = 9
            self.match(FormFlowParser.ID)
            self.state = 10
            self.match(FormFlowParser.T__1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 11
                self.question()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(FormFlowParser.T__2)
            self.state = 18
            self.match(FormFlowParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FormFlowParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(FormFlowParser.TipoContext,0)


        def STR(self):
            return self.getToken(FormFlowParser.STR, 0)

        def configs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormFlowParser.ConfigsContext)
            else:
                return self.getTypedRuleContext(FormFlowParser.ConfigsContext,i)


        def getRuleIndex(self):
            return FormFlowParser.RULE_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion" ):
                listener.enterQuestion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion" ):
                listener.exitQuestion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion" ):
                return visitor.visitQuestion(self)
            else:
                return visitor.visitChildren(self)




    def question(self):

        localctx = FormFlowParser.QuestionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_question)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(FormFlowParser.T__4)
            self.state = 21
            self.match(FormFlowParser.ID)
            self.state = 22
            self.match(FormFlowParser.T__5)
            self.state = 23
            self.tipo()
            self.state = 24
            self.match(FormFlowParser.STR)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 47104) != 0):
                self.state = 25
                self.configs()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormFlowParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = FormFlowParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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


    class ConfigsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormFlowParser.RULE_configs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConfigIfContext(ConfigsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConfigsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FormFlowParser.ID, 0)
        def STR(self):
            return self.getToken(FormFlowParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigIf" ):
                listener.enterConfigIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigIf" ):
                listener.exitConfigIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigIf" ):
                return visitor.visitConfigIf(self)
            else:
                return visitor.visitChildren(self)


    class ConfigMaxContext(ConfigsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConfigsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(FormFlowParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigMax" ):
                listener.enterConfigMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigMax" ):
                listener.exitConfigMax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigMax" ):
                return visitor.visitConfigMax(self)
            else:
                return visitor.visitChildren(self)


    class ConfigMinContext(ConfigsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConfigsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(FormFlowParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigMin" ):
                listener.enterConfigMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigMin" ):
                listener.exitConfigMin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigMin" ):
                return visitor.visitConfigMin(self)
            else:
                return visitor.visitChildren(self)


    class ConfigOptionsContext(ConfigsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConfigsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(FormFlowParser.STR)
            else:
                return self.getToken(FormFlowParser.STR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigOptions" ):
                listener.enterConfigOptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigOptions" ):
                listener.exitConfigOptions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigOptions" ):
                return visitor.visitConfigOptions(self)
            else:
                return visitor.visitChildren(self)



    def configs(self):

        localctx = FormFlowParser.ConfigsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_configs)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = FormFlowParser.ConfigMinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(FormFlowParser.T__10)
                self.state = 34
                self.match(FormFlowParser.NUM)
                pass
            elif token in [12]:
                localctx = FormFlowParser.ConfigMaxContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(FormFlowParser.T__11)
                self.state = 36
                self.match(FormFlowParser.NUM)
                pass
            elif token in [13]:
                localctx = FormFlowParser.ConfigOptionsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(FormFlowParser.T__12)
                self.state = 38
                self.match(FormFlowParser.STR)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 39
                    self.match(FormFlowParser.T__13)
                    self.state = 40
                    self.match(FormFlowParser.STR)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [15]:
                localctx = FormFlowParser.ConfigIfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(FormFlowParser.T__14)
                self.state = 47
                self.match(FormFlowParser.ID)
                self.state = 48
                self.match(FormFlowParser.T__15)
                self.state = 49
                self.match(FormFlowParser.STR)
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





