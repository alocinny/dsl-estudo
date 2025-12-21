# Generated from Robo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RoboParser import RoboParser
else:
    from RoboParser import RoboParser

# This class defines a complete listener for a parse tree produced by RoboParser.
class RoboListener(ParseTreeListener):

    # Enter a parse tree produced by RoboParser#program.
    def enterProgram(self, ctx:RoboParser.ProgramContext):
        pass

    # Exit a parse tree produced by RoboParser#program.
    def exitProgram(self, ctx:RoboParser.ProgramContext):
        pass


    # Enter a parse tree produced by RoboParser#Move.
    def enterMove(self, ctx:RoboParser.MoveContext):
        pass

    # Exit a parse tree produced by RoboParser#Move.
    def exitMove(self, ctx:RoboParser.MoveContext):
        pass


    # Enter a parse tree produced by RoboParser#Repete.
    def enterRepete(self, ctx:RoboParser.RepeteContext):
        pass

    # Exit a parse tree produced by RoboParser#Repete.
    def exitRepete(self, ctx:RoboParser.RepeteContext):
        pass


    # Enter a parse tree produced by RoboParser#Turn.
    def enterTurn(self, ctx:RoboParser.TurnContext):
        pass

    # Exit a parse tree produced by RoboParser#Turn.
    def exitTurn(self, ctx:RoboParser.TurnContext):
        pass


    # Enter a parse tree produced by RoboParser#Back.
    def enterBack(self, ctx:RoboParser.BackContext):
        pass

    # Exit a parse tree produced by RoboParser#Back.
    def exitBack(self, ctx:RoboParser.BackContext):
        pass


    # Enter a parse tree produced by RoboParser#avancar.
    def enterAvancar(self, ctx:RoboParser.AvancarContext):
        pass

    # Exit a parse tree produced by RoboParser#avancar.
    def exitAvancar(self, ctx:RoboParser.AvancarContext):
        pass


    # Enter a parse tree produced by RoboParser#repetir.
    def enterRepetir(self, ctx:RoboParser.RepetirContext):
        pass

    # Exit a parse tree produced by RoboParser#repetir.
    def exitRepetir(self, ctx:RoboParser.RepetirContext):
        pass


    # Enter a parse tree produced by RoboParser#girar.
    def enterGirar(self, ctx:RoboParser.GirarContext):
        pass

    # Exit a parse tree produced by RoboParser#girar.
    def exitGirar(self, ctx:RoboParser.GirarContext):
        pass


    # Enter a parse tree produced by RoboParser#dir.
    def enterDir(self, ctx:RoboParser.DirContext):
        pass

    # Exit a parse tree produced by RoboParser#dir.
    def exitDir(self, ctx:RoboParser.DirContext):
        pass


    # Enter a parse tree produced by RoboParser#voltar.
    def enterVoltar(self, ctx:RoboParser.VoltarContext):
        pass

    # Exit a parse tree produced by RoboParser#voltar.
    def exitVoltar(self, ctx:RoboParser.VoltarContext):
        pass



del RoboParser