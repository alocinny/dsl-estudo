# Generated from Logica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LogicaParser import LogicaParser
else:
    from LogicaParser import LogicaParser

# This class defines a complete generic visitor for a parse tree produced by LogicaParser.

class LogicaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LogicaParser#Implies.
    def visitImplies(self, ctx:LogicaParser.ImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#CombinadorNot.
    def visitCombinadorNot(self, ctx:LogicaParser.CombinadorNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#Parens.
    def visitParens(self, ctx:LogicaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#CombinadorAnd.
    def visitCombinadorAnd(self, ctx:LogicaParser.CombinadorAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#Predicado.
    def visitPredicado(self, ctx:LogicaParser.PredicadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#QuantAll.
    def visitQuantAll(self, ctx:LogicaParser.QuantAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#QuantExist.
    def visitQuantExist(self, ctx:LogicaParser.QuantExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#Var.
    def visitVar(self, ctx:LogicaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#Const.
    def visitConst(self, ctx:LogicaParser.ConstContext):
        return self.visitChildren(ctx)



del LogicaParser