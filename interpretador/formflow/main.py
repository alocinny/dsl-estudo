import sys
from antlr4 import *
from FormFlowLexer import FormFlowLexer
from FormFlowParser import FormFlowParser

respostas = {}

def avalia_config(t):
   match t:
      case FormFlowParser.ConfigMinContext():
         return {'min': float(t.NUM().getText())}
      
      case FormFlowParser.ConfigMaxContext():
         return {'max': float(t.NUM().getText())}
      
      case FormFlowParser.ConfigOptionsContext():
         # Cria lista com os textos das opções
         lista_opts = [token.getText().strip('"') for token in t.STR()]
         return {'options': lista_opts}
      
      case FormFlowParser.ConfigIfContext():
         id_ref = t.ID().getText()
         val_esperado = t.STR().getText().strip('"')
         # Verifica na memória global
         pode_perguntar = str(respostas.get(id_ref)) == val_esperado
         return {'ask_if': pode_perguntar}

def executa(t):
   match t:
      case FormFlowParser.FormularioContext():
         print(f"--- Form: {t.ID().getText()} ---")
         for q in t.question():
            executa(q)
            
      case FormFlowParser.QuestionContext():
         id_pergunta = t.ID().getText()
         texto = t.STR().getText().strip('"')
         tipo = t.tipo().getText()

         regras = {'min': None, 'max': None, 'options': [], 'ask_if': True}

         for c in t.configs():
             r = avalia_config(c)
             regras.update(r) # Atualiza o dict de regras
             
         if not regras['ask_if']:
             return # Pula a pergunta

         while True:
             entrada = input(f"{texto} ")
             try:
                 valor = entrada
                 if tipo == 'int': valor = int(entrada)
                 elif tipo == 'float': valor = float(entrada)
                 
                 # Validações
                 if regras['min'] is not None and valor < regras['min']:
                     print(f"Erro: Mínimo {regras['min']}")
                     continue
                 if regras['max'] is not None and valor > regras['max']:
                     print(f"Erro: Máximo {regras['max']}")
                     continue
                 if tipo == 'choice' and entrada not in regras['options']:
                     print(f"Erro: Opções válidas: {regras['options']}")
                     continue
                     
                 # Salva na memória global
                 respostas[id_pergunta] = valor
                 break
             except ValueError:
                 print(f"Erro: Tipo inválido ({tipo})")

codigo = """
form Triagem {
    question nome: text "Nome?"
    question idade: int "Idade?" min 0 max 120
    question dor: choice "Sente dor?" options "sim", "nao"
    question nivel: int "Nivel (1-10)?" ask_if dor == "sim" min 1 max 10
    end
}
"""

lexer = FormFlowLexer(InputStream(codigo))
parser = FormFlowParser(CommonTokenStream(lexer))
tree = parser.formulario()

executa(tree)

print("\n--- Resultado Final ---")
print(respostas)
