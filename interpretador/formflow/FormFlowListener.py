# Generated from FormFlow.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormFlowParser import FormFlowParser
else:
    from FormFlowParser import FormFlowParser

# This class defines a complete listener for a parse tree produced by FormFlowParser.
class FormFlowListener(ParseTreeListener):

    # Enter a parse tree produced by FormFlowParser#formulario.
    def enterFormulario(self, ctx:FormFlowParser.FormularioContext):
        pass

    # Exit a parse tree produced by FormFlowParser#formulario.
    def exitFormulario(self, ctx:FormFlowParser.FormularioContext):
        pass


    # Enter a parse tree produced by FormFlowParser#question.
    def enterQuestion(self, ctx:FormFlowParser.QuestionContext):
        pass

    # Exit a parse tree produced by FormFlowParser#question.
    def exitQuestion(self, ctx:FormFlowParser.QuestionContext):
        pass


    # Enter a parse tree produced by FormFlowParser#tipo.
    def enterTipo(self, ctx:FormFlowParser.TipoContext):
        pass

    # Exit a parse tree produced by FormFlowParser#tipo.
    def exitTipo(self, ctx:FormFlowParser.TipoContext):
        pass


    # Enter a parse tree produced by FormFlowParser#ConfigMin.
    def enterConfigMin(self, ctx:FormFlowParser.ConfigMinContext):
        pass

    # Exit a parse tree produced by FormFlowParser#ConfigMin.
    def exitConfigMin(self, ctx:FormFlowParser.ConfigMinContext):
        pass


    # Enter a parse tree produced by FormFlowParser#ConfigMax.
    def enterConfigMax(self, ctx:FormFlowParser.ConfigMaxContext):
        pass

    # Exit a parse tree produced by FormFlowParser#ConfigMax.
    def exitConfigMax(self, ctx:FormFlowParser.ConfigMaxContext):
        pass


    # Enter a parse tree produced by FormFlowParser#ConfigOptions.
    def enterConfigOptions(self, ctx:FormFlowParser.ConfigOptionsContext):
        pass

    # Exit a parse tree produced by FormFlowParser#ConfigOptions.
    def exitConfigOptions(self, ctx:FormFlowParser.ConfigOptionsContext):
        pass


    # Enter a parse tree produced by FormFlowParser#ConfigIf.
    def enterConfigIf(self, ctx:FormFlowParser.ConfigIfContext):
        pass

    # Exit a parse tree produced by FormFlowParser#ConfigIf.
    def exitConfigIf(self, ctx:FormFlowParser.ConfigIfContext):
        pass



del FormFlowParser