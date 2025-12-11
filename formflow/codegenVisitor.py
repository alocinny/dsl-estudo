class CodeGenVisitor(FormFlowVisitor):
    def __init__(self):
        self.code = []
        self.indent = ""

    def visitFormDef(self, ctx):
        self.code.append("def main():")
        self.code.append("    answers = {}")
        
        self.indent = "    " # Define indentação base
        self.visitChildren(ctx) # Visita as questões
        
        # Código final de impressão
        self.code.append(f"{self.indent}print(answers)")

        return "\n".join(self.code)

    def visitQuestion(self, ctx):
        q_id = ctx.ID().getText()
        q_text = ctx.typeDef().STRING().getText()
        q_type = ctx.typeDef().start.text # int, text, choice...
        
        extra_args = ""
        is_conditional = False
        condition_str = ""

        # Processa restrições (min, max, options, ask_if)
        for c in ctx.constraints():
            if c.MinVal(): 
                extra_args += f", min_value={c.NUMBER().getText()}"
            elif c.OptionsVal():
                opts = [t.getText() for t in c.stringList().STRING()]
                extra_args += f", options={opts}"
            elif c.Conditional():
                # Tratamento do 'ask_if'
                target_id = c.ID().getText()
                val = c.STRING().getText()
                is_conditional = True
                condition_str = f'if answers.get("{target_id}") == {val}:'

        # Geração do código da questão
        method_map = {'text': 'ask_text', 'int': 'ask_int', 
                      'float': 'ask_float', 'choice': 'ask_choice'}
        
        func_call = f'answers["{q_id}"] = {method_map[q_type]}({q_text}{extra_args})'

        # Escreve no buffer de código
        self.code.append(f"{self.indent}# Question {q_id}")
        
        if is_conditional:
            self.code.append(f"{self.indent}{condition_str}")
            self.code.append(f"{self.indent}    {func_call}") # Indenta +1 nível
        else:
            self.code.append(f"{self.indent}{func_call}")