# Generated from Robo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RoboParser import RoboParser
else:
    from RoboParser import RoboParser

# This class defines a complete generic visitor for a parse tree produced by RoboParser.

class RoboVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RoboParser#program.
    def visitProgram(self, ctx:RoboParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#Move.
    def visitMove(self, ctx:RoboParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#Repete.
    def visitRepete(self, ctx:RoboParser.RepeteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#Turn.
    def visitTurn(self, ctx:RoboParser.TurnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#Back.
    def visitBack(self, ctx:RoboParser.BackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#avancar.
    def visitAvancar(self, ctx:RoboParser.AvancarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#repetir.
    def visitRepetir(self, ctx:RoboParser.RepetirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#girar.
    def visitGirar(self, ctx:RoboParser.GirarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#dir.
    def visitDir(self, ctx:RoboParser.DirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboParser#voltar.
    def visitVoltar(self, ctx:RoboParser.VoltarContext):
        return self.visitChildren(ctx)



del RoboParser