class SemanticVisitor(QuickMathVisitor):
    def __init__(self):
        self.symbols_table = set()
        self.errors = []
    
    def visitStatCmd(self, ctx):
        id = ctx.ID().getText()

        if id not in self.symbols_table:
            self.symbols_table.add(id)
        else:
            self.errors.append("Erro: variavel ja foi declarada")
        
        return self.visitChildren(ctx)
    
    def visitIdExpr(self, ctx):
        var = ctx.ID().getText()

        if id not in self.symbols_table:
            self.errors.append("Erro: variavel nao foi declarada")