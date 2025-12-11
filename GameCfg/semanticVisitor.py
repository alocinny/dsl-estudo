class SemantiVisitor(GameCfgVisitor):
    def __init__(self):
        self.errors = []
    
    def visitSet(self, ctx):
        id = ctx.ID().getText()

        if id.endswith('vol'):
            if ctx.val().IntVal():

                vol = ctx.val().INT().getText()
                int(vol)
        
                if vol > 100:
                    self.errors.append("Erro: volume não pode ser maior que 100")
            else: 
                self.errors.append("Erro: deve ser um numero inteiro")
        
        return self.visitChildrem(ctx)
