# Generated from Receita.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ReceitaParser import ReceitaParser
else:
    from ReceitaParser import ReceitaParser

# This class defines a complete generic visitor for a parse tree produced by ReceitaParser.

class ReceitaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ReceitaParser#receita.
    def visitReceita(self, ctx:ReceitaParser.ReceitaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#Declaracao.
    def visitDeclaracao(self, ctx:ReceitaParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#Add.
    def visitAdd(self, ctx:ReceitaParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#Misturar.
    def visitMisturar(self, ctx:ReceitaParser.MisturarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#Assar.
    def visitAssar(self, ctx:ReceitaParser.AssarContext):
        return self.visitChildren(ctx)



del ReceitaParser