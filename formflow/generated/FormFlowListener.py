# Generated from FormFlow.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormFlowParser import FormFlowParser
else:
    from FormFlowParser import FormFlowParser

# This class defines a complete listener for a parse tree produced by FormFlowParser.
class FormFlowListener(ParseTreeListener):

    # Enter a parse tree produced by FormFlowParser#prog.
    def enterProg(self, ctx:FormFlowParser.ProgContext):
        pass

    # Exit a parse tree produced by FormFlowParser#prog.
    def exitProg(self, ctx:FormFlowParser.ProgContext):
        pass


    # Enter a parse tree produced by FormFlowParser#formDef.
    def enterFormDef(self, ctx:FormFlowParser.FormDefContext):
        pass

    # Exit a parse tree produced by FormFlowParser#formDef.
    def exitFormDef(self, ctx:FormFlowParser.FormDefContext):
        pass


    # Enter a parse tree produced by FormFlowParser#question.
    def enterQuestion(self, ctx:FormFlowParser.QuestionContext):
        pass

    # Exit a parse tree produced by FormFlowParser#question.
    def exitQuestion(self, ctx:FormFlowParser.QuestionContext):
        pass


    # Enter a parse tree produced by FormFlowParser#typeDef.
    def enterTypeDef(self, ctx:FormFlowParser.TypeDefContext):
        pass

    # Exit a parse tree produced by FormFlowParser#typeDef.
    def exitTypeDef(self, ctx:FormFlowParser.TypeDefContext):
        pass


    # Enter a parse tree produced by FormFlowParser#MinVal.
    def enterMinVal(self, ctx:FormFlowParser.MinValContext):
        pass

    # Exit a parse tree produced by FormFlowParser#MinVal.
    def exitMinVal(self, ctx:FormFlowParser.MinValContext):
        pass


    # Enter a parse tree produced by FormFlowParser#MaxVal.
    def enterMaxVal(self, ctx:FormFlowParser.MaxValContext):
        pass

    # Exit a parse tree produced by FormFlowParser#MaxVal.
    def exitMaxVal(self, ctx:FormFlowParser.MaxValContext):
        pass


    # Enter a parse tree produced by FormFlowParser#OptionsVal.
    def enterOptionsVal(self, ctx:FormFlowParser.OptionsValContext):
        pass

    # Exit a parse tree produced by FormFlowParser#OptionsVal.
    def exitOptionsVal(self, ctx:FormFlowParser.OptionsValContext):
        pass


    # Enter a parse tree produced by FormFlowParser#Conditional.
    def enterConditional(self, ctx:FormFlowParser.ConditionalContext):
        pass

    # Exit a parse tree produced by FormFlowParser#Conditional.
    def exitConditional(self, ctx:FormFlowParser.ConditionalContext):
        pass


    # Enter a parse tree produced by FormFlowParser#stringList.
    def enterStringList(self, ctx:FormFlowParser.StringListContext):
        pass

    # Exit a parse tree produced by FormFlowParser#stringList.
    def exitStringList(self, ctx:FormFlowParser.StringListContext):
        pass



del FormFlowParser