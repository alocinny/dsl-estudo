# Generated from FormFlow.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormFlowParser import FormFlowParser
else:
    from FormFlowParser import FormFlowParser

# This class defines a complete generic visitor for a parse tree produced by FormFlowParser.

class FormFlowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormFlowParser#prog.
    def visitProg(self, ctx:FormFlowParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#formDef.
    def visitFormDef(self, ctx:FormFlowParser.FormDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#question.
    def visitQuestion(self, ctx:FormFlowParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#typeDef.
    def visitTypeDef(self, ctx:FormFlowParser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#MinVal.
    def visitMinVal(self, ctx:FormFlowParser.MinValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#MaxVal.
    def visitMaxVal(self, ctx:FormFlowParser.MaxValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#OptionsVal.
    def visitOptionsVal(self, ctx:FormFlowParser.OptionsValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#Conditional.
    def visitConditional(self, ctx:FormFlowParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormFlowParser#stringList.
    def visitStringList(self, ctx:FormFlowParser.StringListContext):
        return self.visitChildren(ctx)



del FormFlowParser