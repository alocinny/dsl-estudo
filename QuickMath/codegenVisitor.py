class CodegenVisitor(QuickMathVisitor):
    def __init__(self):
        self.code = []
    
    def visitProgram(self, ctx):
        name = ctx.ID().getText()
        self.code.append(f"def {name}():")

        self.visitChildren(ctx)

        return "\n".join(self.code)
    
    def visitStatCmd(self, ctx):
        var = ctx.ID().getText()
        num = ctx.INT().getText()

        self.code.append(f" {var} = {num}")

    def visitShowCmd(self, ctx):
        expr = ctx.expr().getText()

        self.code.append(f" print({expr})")
