import sys
import math
from antlr4 import *
from RoboLexer import RoboLexer
from RoboParser import RoboParser

class RoboInterpreter:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.angle = 90.0 #90 graus, norte no círculo trigonométrico

	# a função visit é o cérebro. Ela recebe um pedaço (tree) e decide o que vai fazer com ele
	def visit(self, tree):
		match tree:
			# caso 1: raiz do programa
			case RoboParser.ProgramContext():
				for child in tree.getChildren():
					# o programa tem vários filhos (comandos). visitamos um por um na ordem
					self.visit(child)
				return (self.x, self.y)
			# caso 2: comando de movimento (na gramática tá a label #Move)
			case RoboParser.MoveContext():
				# a gramática dele tem comando: avancar #Move
				# o 'tree' é o nó #Move. O filho dele é a regra avançar.
				# precisa descer esse nível pra pegar o número
				ctx_avancar = tree.avancar()
				# pega o contexto do token INT e converte para inteiro
				dist = int(ctx_avancar.INT().getText())

				# matemática: decompõe o vetor em X e Y
				rad = math.radians(self.angle)
				self.x += dist * math.cos(rad)
				self.y += math.sin(rad)
			# caso 3: Comando de voltar (label #Back)
			case RoboParser.BackContext():
				ctx_voltar = tree.voltar() # desce para a regra de voltar
				dist = int(ctx_voltar.INT().getText())
				rad = math.radians(self.angle)
				# mesma lógica mas subtrai pq anda pra trás
				self.x -= dist * math.cos(rad)
				self.y -= dist * math.sin(rad)
			# caso 4: comando de girar  (label #Turn)
			case RoboParser.TurnContext():
				ctx_girar = tree.girar() # desce para a regra girar
				graus = int(ctx_girar.INT().getText())
				# a palavra dir é reservada no python, o antlr muda para 'dir_()'
				lado = ctx_girar.dir_().getText()

				if lado == 'ESQUERDA':
					self.angle += graus # soma graus (sentido anti-horario)
				else:
					self.angle -= graus # subtrai graus (sentido horário)
			# caso 5: o loop (label #Repete)
			case RoboParser.RepeteContext():
				ctx_repita = tree.repetir() # desce para a regra repetir

				repeticoes = int(ctx_repita.INT().getText())

				lista_comandos_internos = ctx_repita.comando()

				for _ in range(repeticoes):
					for cmd  in lista_comandos_internos:
						self.visit(cmd)
			# caso padrão pra nós que não importam
			case _:
				pass

# teste do código

codigo = """
AVANCE 10
REPITA 2
	GIRE 45 GRAUS A ESQUERDA
	AVANCE 10
FIM-REPITA
GIRE 45 GRAUS A DIREITA
VOLTE 10
"""

lexer = RoboLexer(InputStream(codigo))
parser = RoboParser(CommonTokenStream(lexer))
tree = parser.program()
visitor = RoboInterpreter()
pos = visitor.visit(tree)

print(f"posição final: ({pos[0]:.2}, {pos[1]:.2})")
