from antlr4 import *
from ReceitaLexer import ReceitaLexer
from ReceitaParser import ReceitaParser

declarados = [] # lista de ingredientes válidos
misturado = False
assado = False

def analisa(t):
	global misturado, assado #pq vai precisar alterar essas tags

	match t:
		# caso 1:
		case ReceitaParser.ReceitaContext():
			for filho in t.inst():
				analisa(filho)
		# caso 2:
		case ReceitaParser.DeclaracaoContext():
			nome = t.ID().getText()
			if nome in declarados:
				raise Exception(f"erro: '{nome}' já foi declarado")
			declarados.append(nome)
		# caso 3:
		case ReceitaParser.AddContext():
			nome = t.ID().getText()
			if nome not in declarados:
				raise Exception(f"erro: '{nome}' nao foi declarado")
			declarados.append(nome)
		# caso 4
		case ReceitaParser.MisturarContext():
			if assado:
				raise Exception("erro: não pode misturar depois de assado")
			misturado = True
		# caso 5
		case ReceitaParser.AssarContext():
			if not misturado:
				raise Exception("erro: precisa misturar antes de assar")
			assado = True


cod1= """
Ingrediente Ovos
Ingrediente Farinha
Adicione 3 de Ovos
Adicione 200 de  Farinha
Assar por 30 minutos
"""

cod2 = """
Ingrediente Ovos
Adicione 3 de Ovos
Misturar por 5 minutos
Assar por 30 minutos
"""

try:
	lexer = ReceitaLexer(InputStream(cod1
	))
	parser = ReceitaParser(CommonTokenStream(lexer))
	tree = parser.receita()

	# Reseta memória para o teste
	declarados = [] 
	misturado = False
	assado = False

	print("--- Analisando... ---")
	analisa(tree)
	print("Sucesso! A receita é válida.")

except Exception as e:
	print(e)
