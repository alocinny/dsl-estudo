# Generated from Logica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LogicaParser import LogicaParser
else:
    from LogicaParser import LogicaParser

# This class defines a complete listener for a parse tree produced by LogicaParser.
class LogicaListener(ParseTreeListener):

    # Enter a parse tree produced by LogicaParser#Implies.
    def enterImplies(self, ctx:LogicaParser.ImpliesContext):
        pass

    # Exit a parse tree produced by LogicaParser#Implies.
    def exitImplies(self, ctx:LogicaParser.ImpliesContext):
        pass


    # Enter a parse tree produced by LogicaParser#CombinadorNot.
    def enterCombinadorNot(self, ctx:LogicaParser.CombinadorNotContext):
        pass

    # Exit a parse tree produced by LogicaParser#CombinadorNot.
    def exitCombinadorNot(self, ctx:LogicaParser.CombinadorNotContext):
        pass


    # Enter a parse tree produced by LogicaParser#Parens.
    def enterParens(self, ctx:LogicaParser.ParensContext):
        pass

    # Exit a parse tree produced by LogicaParser#Parens.
    def exitParens(self, ctx:LogicaParser.ParensContext):
        pass


    # Enter a parse tree produced by LogicaParser#CombinadorAnd.
    def enterCombinadorAnd(self, ctx:LogicaParser.CombinadorAndContext):
        pass

    # Exit a parse tree produced by LogicaParser#CombinadorAnd.
    def exitCombinadorAnd(self, ctx:LogicaParser.CombinadorAndContext):
        pass


    # Enter a parse tree produced by LogicaParser#Predicado.
    def enterPredicado(self, ctx:LogicaParser.PredicadoContext):
        pass

    # Exit a parse tree produced by LogicaParser#Predicado.
    def exitPredicado(self, ctx:LogicaParser.PredicadoContext):
        pass


    # Enter a parse tree produced by LogicaParser#QuantAll.
    def enterQuantAll(self, ctx:LogicaParser.QuantAllContext):
        pass

    # Exit a parse tree produced by LogicaParser#QuantAll.
    def exitQuantAll(self, ctx:LogicaParser.QuantAllContext):
        pass


    # Enter a parse tree produced by LogicaParser#QuantExist.
    def enterQuantExist(self, ctx:LogicaParser.QuantExistContext):
        pass

    # Exit a parse tree produced by LogicaParser#QuantExist.
    def exitQuantExist(self, ctx:LogicaParser.QuantExistContext):
        pass


    # Enter a parse tree produced by LogicaParser#Var.
    def enterVar(self, ctx:LogicaParser.VarContext):
        pass

    # Exit a parse tree produced by LogicaParser#Var.
    def exitVar(self, ctx:LogicaParser.VarContext):
        pass


    # Enter a parse tree produced by LogicaParser#Const.
    def enterConst(self, ctx:LogicaParser.ConstContext):
        pass

    # Exit a parse tree produced by LogicaParser#Const.
    def exitConst(self, ctx:LogicaParser.ConstContext):
        pass



del LogicaParser