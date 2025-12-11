class CodegenVisitor(GameCfgVisitor):
    def __init__(self):
        self.code = []
    
    def visitConfig(self, ctx):
        name = ctx.ID().getText()

        self.code.append("data = {}")

        self.visitChildren(ctx)

        return "\n".join(self.code)
    
    def visitSection(self, ctx):
        name = ctx.ID().getText()

        self.code.append(f"# Section {name}")
        self.code.append(f'data["{name}"] = {{}}')

        self.current_sec = name
        
        self.visitChildren(ctx)

        self.current_sec = None
    
    def visitSet(self, ctx):
        id = ctx.ID().getText()
        val = ctx.val().getText()

        sec = self.current_sec
        self.code.append(f'data["{sec}"]["{id}"] = {val}')