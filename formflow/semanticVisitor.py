class SemanticVisitor(FormFlowVisitor):
    def __init__(self):
        self.symbol_table = set() # Tabela de Símbolos simples
        self.errors = []

    def visitQuestion(self, ctx):
        q_id = ctx.ID().getText()
        
        # 1. Verificação de ID Duplicado
        if q_id in self.symbol_table:
            self.errors.append(f"Erro: ID '{q_id}' já definido.")
        else:
            self.symbol_table.add(q_id)

        # 2. Validação de Tipos para restrições
        q_type = ctx.typeDef().start.text # 'text', 'int', etc.
        
        for constraint in ctx.constraints():
            # Se for MinVal ou MaxVal, o tipo deve ser numérico
            if isinstance(constraint, FormFlowParser.MinValContext) or \
               isinstance(constraint, FormFlowParser.MaxValContext):
                if q_type not in ['int', 'float']:
                    self.errors.append(f"Erro em '{q_id}': min/max apenas para int/float.")

        return self.visitChildren(ctx)