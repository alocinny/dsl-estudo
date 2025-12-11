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
        4,1,20,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,5,1,5,1,5,5,5,55,8,5,
        10,5,12,5,58,9,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,7,10,59,0,12,1,0,
        0,0,2,14,1,0,0,0,4,26,1,0,0,0,6,36,1,0,0,0,8,49,1,0,0,0,10,51,1,
        0,0,0,12,13,3,2,1,0,13,1,1,0,0,0,14,15,5,1,0,0,15,16,5,17,0,0,16,
        20,5,2,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,
        0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,3,0,0,24,25,
        5,4,0,0,25,3,1,0,0,0,26,27,5,5,0,0,27,28,5,17,0,0,28,29,5,6,0,0,
        29,33,3,6,3,0,30,32,3,8,4,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,
        0,0,0,33,34,1,0,0,0,34,5,1,0,0,0,35,33,1,0,0,0,36,37,7,0,0,0,37,
        38,5,18,0,0,38,7,1,0,0,0,39,40,5,11,0,0,40,50,5,19,0,0,41,42,5,12,
        0,0,42,50,5,19,0,0,43,44,5,13,0,0,44,50,3,10,5,0,45,46,5,14,0,0,
        46,47,5,17,0,0,47,48,5,15,0,0,48,50,5,18,0,0,49,39,1,0,0,0,49,41,
        1,0,0,0,49,43,1,0,0,0,49,45,1,0,0,0,50,9,1,0,0,0,51,56,5,18,0,0,
        52,53,5,16,0,0,53,55,5,18,0,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,11,1,0,0,0,58,56,1,0,0,0,4,20,33,49,56
    ]

class FormFlowParser ( Parser ):

    grammarFileName = "FormFlow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'form'", "'{'", "'end'", "'}'", "'question'", 
                     "':'", "'text'", "'int'", "'float'", "'choice'", "'min'", 
                     "'max'", "'options'", "'ask_if'", "'=='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_formDef = 1
    RULE_question = 2
    RULE_typeDef = 3
    RULE_constraints = 4
    RULE_stringList = 5

    ruleNames =  [ "prog", "formDef", "question", "typeDef", "constraints", 
                   "stringList" ]

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
    STRING=18
    NUMBER=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formDef(self):
            return self.getTypedRuleContext(FormFlowParser.FormDefContext,0)


        def getRuleIndex(self):
            return FormFlowParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = FormFlowParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.formDef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormDefContext(ParserRuleContext):
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
            return FormFlowParser.RULE_formDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormDef" ):
                listener.enterFormDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormDef" ):
                listener.exitFormDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormDef" ):
                return visitor.visitFormDef(self)
            else:
                return visitor.visitChildren(self)




    def formDef(self):

        localctx = FormFlowParser.FormDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(FormFlowParser.T__0)
            self.state = 15
            self.match(FormFlowParser.ID)
            self.state = 16
            self.match(FormFlowParser.T__1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 17
                self.question()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(FormFlowParser.T__2)
            self.state = 24
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

        def typeDef(self):
            return self.getTypedRuleContext(FormFlowParser.TypeDefContext,0)


        def constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormFlowParser.ConstraintsContext)
            else:
                return self.getTypedRuleContext(FormFlowParser.ConstraintsContext,i)


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
        self.enterRule(localctx, 4, self.RULE_question)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(FormFlowParser.T__4)
            self.state = 27
            self.match(FormFlowParser.ID)
            self.state = 28
            self.match(FormFlowParser.T__5)
            self.state = 29
            self.typeDef()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                self.state = 30
                self.constraints()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormFlowParser.STRING, 0)

        def getRuleIndex(self):
            return FormFlowParser.RULE_typeDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDef" ):
                listener.enterTypeDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDef" ):
                listener.exitTypeDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDef" ):
                return visitor.visitTypeDef(self)
            else:
                return visitor.visitChildren(self)




    def typeDef(self):

        localctx = FormFlowParser.TypeDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typeDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            self.match(FormFlowParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormFlowParser.RULE_constraints

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConditionalContext(ConstraintsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConstraintsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FormFlowParser.ID, 0)
        def STRING(self):
            return self.getToken(FormFlowParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)


    class OptionsValContext(ConstraintsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConstraintsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stringList(self):
            return self.getTypedRuleContext(FormFlowParser.StringListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionsVal" ):
                listener.enterOptionsVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionsVal" ):
                listener.exitOptionsVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionsVal" ):
                return visitor.visitOptionsVal(self)
            else:
                return visitor.visitChildren(self)


    class MaxValContext(ConstraintsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConstraintsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FormFlowParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxVal" ):
                listener.enterMaxVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxVal" ):
                listener.exitMaxVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxVal" ):
                return visitor.visitMaxVal(self)
            else:
                return visitor.visitChildren(self)


    class MinValContext(ConstraintsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormFlowParser.ConstraintsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FormFlowParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinVal" ):
                listener.enterMinVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinVal" ):
                listener.exitMinVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinVal" ):
                return visitor.visitMinVal(self)
            else:
                return visitor.visitChildren(self)



    def constraints(self):

        localctx = FormFlowParser.ConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constraints)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = FormFlowParser.MinValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(FormFlowParser.T__10)
                self.state = 40
                self.match(FormFlowParser.NUMBER)
                pass
            elif token in [12]:
                localctx = FormFlowParser.MaxValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(FormFlowParser.T__11)
                self.state = 42
                self.match(FormFlowParser.NUMBER)
                pass
            elif token in [13]:
                localctx = FormFlowParser.OptionsValContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(FormFlowParser.T__12)
                self.state = 44
                self.stringList()
                pass
            elif token in [14]:
                localctx = FormFlowParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(FormFlowParser.T__13)
                self.state = 46
                self.match(FormFlowParser.ID)
                self.state = 47
                self.match(FormFlowParser.T__14)
                self.state = 48
                self.match(FormFlowParser.STRING)
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


    class StringListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(FormFlowParser.STRING)
            else:
                return self.getToken(FormFlowParser.STRING, i)

        def getRuleIndex(self):
            return FormFlowParser.RULE_stringList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringList" ):
                listener.enterStringList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringList" ):
                listener.exitStringList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringList" ):
                return visitor.visitStringList(self)
            else:
                return visitor.visitChildren(self)




    def stringList(self):

        localctx = FormFlowParser.StringListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stringList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(FormFlowParser.STRING)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 52
                self.match(FormFlowParser.T__15)
                self.state = 53
                self.match(FormFlowParser.STRING)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





