# Generated from Logica.g4 by ANTLR 4.13.1
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
        4,1,12,49,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,1,
        0,1,0,1,0,1,0,3,0,32,8,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,40,8,0,10,0,
        12,0,43,9,0,1,1,1,1,3,1,47,8,1,1,1,0,1,0,2,0,2,0,0,54,0,31,1,0,0,
        0,2,46,1,0,0,0,4,5,6,0,-1,0,5,6,5,1,0,0,6,7,5,9,0,0,7,8,5,2,0,0,
        8,32,3,0,0,7,9,10,5,3,0,0,10,11,5,9,0,0,11,12,5,2,0,0,12,32,3,0,
        0,6,13,14,5,5,0,0,14,32,3,0,0,4,15,16,5,11,0,0,16,17,5,7,0,0,17,
        22,3,2,1,0,18,19,5,2,0,0,19,21,3,2,1,0,20,18,1,0,0,0,21,24,1,0,0,
        0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,
        5,8,0,0,26,32,1,0,0,0,27,28,5,7,0,0,28,29,3,0,0,0,29,30,5,8,0,0,
        30,32,1,0,0,0,31,4,1,0,0,0,31,9,1,0,0,0,31,13,1,0,0,0,31,15,1,0,
        0,0,31,27,1,0,0,0,32,41,1,0,0,0,33,34,10,5,0,0,34,35,5,4,0,0,35,
        40,3,0,0,6,36,37,10,3,0,0,37,38,5,6,0,0,38,40,3,0,0,4,39,33,1,0,
        0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,
        1,0,0,0,43,41,1,0,0,0,44,47,5,9,0,0,45,47,5,10,0,0,46,44,1,0,0,0,
        46,45,1,0,0,0,47,3,1,0,0,0,5,22,31,39,41,46
    ]

class LogicaParser ( Parser ):

    grammarFileName = "Logica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'all'", "','", "'some'", "'->'", "'not'", 
                     "'and'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "CONST", "PRED", "WS" ]

    RULE_formula = 0
    RULE_exp = 1

    ruleNames =  [ "formula", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    VAR=9
    CONST=10
    PRED=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ImpliesContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicaParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplies" ):
                listener.enterImplies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplies" ):
                listener.exitImplies(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplies" ):
                return visitor.visitImplies(self)
            else:
                return visitor.visitChildren(self)


    class CombinadorNotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LogicaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombinadorNot" ):
                listener.enterCombinadorNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombinadorNot" ):
                listener.exitCombinadorNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombinadorNot" ):
                return visitor.visitCombinadorNot(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LogicaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class CombinadorAndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicaParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombinadorAnd" ):
                listener.enterCombinadorAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombinadorAnd" ):
                listener.exitCombinadorAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombinadorAnd" ):
                return visitor.visitCombinadorAnd(self)
            else:
                return visitor.visitChildren(self)


    class PredicadoContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self):
            return self.getToken(LogicaParser.PRED, 0)
        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LogicaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicado" ):
                listener.enterPredicado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicado" ):
                listener.exitPredicado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicado" ):
                return visitor.visitPredicado(self)
            else:
                return visitor.visitChildren(self)


    class QuantAllContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LogicaParser.VAR, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantAll" ):
                listener.enterQuantAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantAll" ):
                listener.exitQuantAll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantAll" ):
                return visitor.visitQuantAll(self)
            else:
                return visitor.visitChildren(self)


    class QuantExistContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LogicaParser.VAR, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantExist" ):
                listener.enterQuantExist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantExist" ):
                listener.exitQuantExist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantExist" ):
                return visitor.visitQuantExist(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogicaParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = LogicaParser.QuantAllContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(LogicaParser.T__0)
                self.state = 6
                self.match(LogicaParser.VAR)
                self.state = 7
                self.match(LogicaParser.T__1)
                self.state = 8
                self.formula(7)
                pass
            elif token in [3]:
                localctx = LogicaParser.QuantExistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LogicaParser.T__2)
                self.state = 10
                self.match(LogicaParser.VAR)
                self.state = 11
                self.match(LogicaParser.T__1)
                self.state = 12
                self.formula(6)
                pass
            elif token in [5]:
                localctx = LogicaParser.CombinadorNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LogicaParser.T__4)
                self.state = 14
                self.formula(4)
                pass
            elif token in [11]:
                localctx = LogicaParser.PredicadoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(LogicaParser.PRED)
                self.state = 16
                self.match(LogicaParser.T__6)
                self.state = 17
                self.exp()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 18
                    self.match(LogicaParser.T__1)
                    self.state = 19
                    self.exp()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(LogicaParser.T__7)
                pass
            elif token in [7]:
                localctx = LogicaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(LogicaParser.T__6)
                self.state = 28
                self.formula(0)
                self.state = 29
                self.match(LogicaParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = LogicaParser.ImpliesContext(self, LogicaParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 33
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 34
                        self.match(LogicaParser.T__3)
                        self.state = 35
                        self.formula(6)
                        pass

                    elif la_ == 2:
                        localctx = LogicaParser.CombinadorAndContext(self, LogicaParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(LogicaParser.T__5)
                        self.state = 38
                        self.formula(4)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LogicaParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ConstContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONST(self):
            return self.getToken(LogicaParser.CONST, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)



    def exp(self):

        localctx = LogicaParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = LogicaParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(LogicaParser.VAR)
                pass
            elif token in [10]:
                localctx = LogicaParser.ConstContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(LogicaParser.CONST)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




