class CodeGenVisitor(FlyPlanVisitor):
    def __init__(self):
        self.code = []
    
    def visitMission(self, ctx):
        name = ctx.ID().getText()
        
        self.code.append(f"class Mission{name}:")
        self.code.append(f" def run(self, drone):")
        
        self.visitChildren(ctx)

        return "\n".join(self.code)
    
    def visitConfig(self, ctx):
        val = ctx.FLOAT().getText()

        self.code.append(f"     drone.set_speed({val})")

    def visitGoto(self, ctx):
        name = ctx.goto().ID().getText()

        self.visitChildren(ctx)
    
    def visitorPosInst(self, ctx):
        ints = ctx.INT().getText()

        x, y, z = inst[0].getText(), inst[1].getText(), inst[2].getText()

        self.code.append(f"     drone.move_to(x={x}, y={y}, z={z})") 
    
    def visitActionInst(self, ctx):
        acao = ctx.action().getText()

        if acao == "takeoff":
            self.code.append(f"     drone.takeoff()")
        elif acao == "land":
            self.code.append(f"     drone.land()")
        
        #act = ctx.action().cildren[1].getText()
        #self.code.append(f"     drone.{act}()")
    
    def visitHoverInst(self, ctx):
        sec = ctx.hover().INT().getText()
        self.code.append(f"     drone.hover(seconds={sec})")
