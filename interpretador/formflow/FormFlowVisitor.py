# Generated from FormFlow.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormFlowParser import FormFlowParser
else:
    from FormFlowParser import FormFlowParser

# This class defines a complete generic visitor for a parse tree produced by FormFlowParser.

class FormFlowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormFlowParser#formulario.
    def visitFormulario(self, ctx:FormFlowParser.FormularioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#question.
    def visitQuestion(self, ctx:FormFlowParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#tipo.
    def visitTipo(self, ctx:FormFlowParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#ConfigMin.
    def visitConfigMin(self, ctx:FormFlowParser.ConfigMinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#ConfigMax.
    def visitConfigMax(self, ctx:FormFlowParser.ConfigMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#ConfigOptions.
    def visitConfigOptions(self, ctx:FormFlowParser.ConfigOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#ConfigIf.
    def visitConfigIf(self, ctx:FormFlowParser.ConfigIfContext):
        return self.visitChildren(ctx)



del FormFlowParser