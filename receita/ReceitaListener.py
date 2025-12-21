# Generated from Receita.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ReceitaParser import ReceitaParser
else:
    from ReceitaParser import ReceitaParser

# This class defines a complete listener for a parse tree produced by ReceitaParser.
class ReceitaListener(ParseTreeListener):

    # Enter a parse tree produced by ReceitaParser#receita.
    def enterReceita(self, ctx:ReceitaParser.ReceitaContext):
        pass

    # Exit a parse tree produced by ReceitaParser#receita.
    def exitReceita(self, ctx:ReceitaParser.ReceitaContext):
        pass


    # Enter a parse tree produced by ReceitaParser#Declaracao.
    def enterDeclaracao(self, ctx:ReceitaParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by ReceitaParser#Declaracao.
    def exitDeclaracao(self, ctx:ReceitaParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by ReceitaParser#Add.
    def enterAdd(self, ctx:ReceitaParser.AddContext):
        pass

    # Exit a parse tree produced by ReceitaParser#Add.
    def exitAdd(self, ctx:ReceitaParser.AddContext):
        pass


    # Enter a parse tree produced by ReceitaParser#Misturar.
    def enterMisturar(self, ctx:ReceitaParser.MisturarContext):
        pass

    # Exit a parse tree produced by ReceitaParser#Misturar.
    def exitMisturar(self, ctx:ReceitaParser.MisturarContext):
        pass


    # Enter a parse tree produced by ReceitaParser#Assar.
    def enterAssar(self, ctx:ReceitaParser.AssarContext):
        pass

    # Exit a parse tree produced by ReceitaParser#Assar.
    def exitAssar(self, ctx:ReceitaParser.AssarContext):
        pass



del ReceitaParser