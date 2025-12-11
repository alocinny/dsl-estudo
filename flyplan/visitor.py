class SemanticVisitor(FlyPlanVisitor):
    def __init__(self):
        # define lista de erros
        self.erros = []
    
    def visitConfig(self, ctx):
        
        speed_txt = ctx.FLOAT().getText()
        speed = float(speed_txt)

        if speed > 25.0:
            self.errors.append("Erro: velocidade máxima foi ultrapassada")
        
        return self.visitChildren(ctx)

    def visitDefMission(self, ctx):
        all_comands = ctx.command()

        gotos = [cmd for cmd in all_comands if cmd.goto()]

        if not gotos:
            return self.visitChildren(ctx)

        for g in gotos[:-1]:
            instructions = g.goto().instruction()

            for instr in instructions:
                if inst.action() and inst.action().LAND():
                    self.errors.append("erro: land encontrado no meio da missão")
    
        return self.visitChildren(ctx)