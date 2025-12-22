# <div align="center">Compiladores: Gabaritos & Padrões de Projeto</div>

<div align="center">
  Coleção de implementações de referência para Interpretadores, Análise Semântica e Geração de Código (Máquina de Pilha).
</div>

<br />

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-0d1117?style=flat-square&logo=python&logoColor=39d353&labelColor=0d1117&color=0d1117" alt="Python Badge">
  <img src="https://img.shields.io/badge/ANTLR-4.13-0d1117?style=flat-square&logo=antlr&logoColor=39d353&labelColor=0d1117&color=0d1117" alt="ANTLR Badge">
  <img src="https://img.shields.io/badge/Status-Concluído-0d1117?style=flat-square&logo=checkmark&logoColor=39d353&labelColor=0d1117&color=0d1117" alt="Status Badge">
</div>

---

## 📋 Tabela de Implementações

| Módulo | Descrição Técnica |
| :--- | :--- |
| **Interpretador** | Controle de estado, física de drone e loops de repetição (`while`). |
| **Análise Semântica** |
| **Gerador de Código** | Tradução para Máquina de Pilha (Pilha, Aritmética e Controle de Fluxo/Jumps). |

---

## 1. Interpretadores (Estado e Fluxo)

### Física de Drone e Segurança (Match/Case)
*Foco: Manipulação de variáveis globais e interrupção de fluxo (`return`) em estados críticos.*

```python
    def interpretador(t):
        global bateria, x, y, z

        # [Safety Check] Se bateria acabou, aborta execução imediatamente
        if bateria <= 0 and not isinstance(t, DronePilotParser.ProgramContext):
            print("CRITICAL BATTERY - IGNORING COMMAND")
            return

        match t:
            case DronePilotParser.ProgramContext():
                for c in t.getChildren(): interpretador(c)

            case DronePilotParser.DecolarContext():
                bateria -= 10 
                z = int(t.ALTURA().getText()) # Define altura absoluta
                print(f"Status: (x={x}, y={y}, z={z}) Bat: {bateria}%")

            case DronePilotParser.MoverContext():
                bateria -= 10
                # GOTO = Atribuição direta, não incremento
                x = int(t.X().getText()) 
                y = int(t.Y().getText())
                print(f"Status: (x={x}, y={y}, z={z}) Bat: {bateria}%")

            case DronePilotParser.PousarContext():
                bateria -= 10
                z = 0 # Pousar zera o eixo Z
                print(f"Status: (x={x}, y={y}, z={z}) Bat: {bateria}%")
```
### Loops de Repetição (While)
*Foco: Uso de globals() para mapear strings do parser para variáveis reais do Python.*
```python
    def interpreta_loop(t):
    global player_hp, boss_hp # Variáveis globais de estado

    match t:
        case BossParser.LoopWhileContext():
            nome_var = t.ID().getText()     # Ex: "player_hp"
            limite = int(t.NUM().getText()) # Ex: 0
            acoes = t.acao()                # Lista de nós filhos

            # Mapeia string -> variável real e executa o loop nativo
            while globals()[nome_var] > limite:
                for cmd in acoes:
                    interpreta_loop(cmd)
                # O Python atualiza globals() automaticamente a cada iteração
``` 
## 2. Análise Semântica (O Fiscal)
### Hardware e Conectividade
*Foco: Uso de Set para verificação eficiente e acesso posicional a tokens.*
```python
    tabela = set() # Set para performance O(1)

    def analisa_semantica(t):
        match t:
            case DroneConfigParser.DeclararContext():
                var = t.ID().getText()
                if var in tabela:
                    raise Exception(f"Erro: Componente '{var}' já existe!")
                tabela.add(var)

            case DroneConfigParser.ConectarContext():
                # Acesso posicional: ID(0) é origem, ID(1) é destino
                comp1 = t.ID(0).getText()
                comp2 = t.ID(1).getText()
                
                if comp1 not in tabela or comp2 not in tabela:
                    raise Exception(f"Erro: Componentes não declarados.")
                
                if comp1 == comp2:
                    raise Exception(f"Erro: Curto-circuito! Auto-conexão em '{comp1}'.")
```

### Validação de Funções (Aridade)
*Foco: Tabela de símbolos armazenando metadados (quantidade de parâmetros).*
```python
    # Tabela: { 'nome_funcao': qtd_params }
    tabela_funcoes = {} 

    def analisa_funcao(t):
        match t:
            case LangParser.DefFuncaoContext():
                nome = t.ID().getText()
                qtd_params = len(t.param()) # Conta filhos na declaração
                tabela_funcoes[nome] = qtd_params

            case LangParser.ChamadaContext():
                nome = t.ID().getText()
                qtd_args = len(t.arg()) # Conta argumentos passados
                
                if nome not in tabela_funcoes:
                    raise Exception(f"Erro: Função '{nome}' não existe.")
                
                if qtd_args != tabela_funcoes[nome]:
                    raise Exception(f"Erro Aridade: Esperava {tabela_funcoes[nome]}, recebeu {qtd_args}.")
```

## 3. Geração de Código (Máquina de Pilha)
### Expressões Aritméticas
*Foco: Lógica Pós-Ordem (Operandos -> Operador) e gerenciamento de endereços.*

```
; Código Fonte: altitude = altitude + (offset * 2)
; Mapa: altitude (0), offset (1)

PUSHI 0     ; Endereço alvo (altitude)
LOAD        ; Carrega valor atual de altitude
PUSHI 1     ; Endereço (offset)
LOAD        ; Carrega valor de offset
PUSHI 2     ; Constante 2
MUL         ; Multiplica (offset * 2)
ADD         ; Soma (altitude + resultado)
STORE 0     ; Guarda resultado final em altitude
```

### Controle de Fluxo (IF/ELSE)
*Foco: Uso de Labels e Jumps condicionais (JZ) e incondicionais (JUMP).*
```
; Código Fonte: if x > 10 then y = 1 else y = 0

; 1. Condição
PUSHI 0     ; Endereço x
LOAD
PUSHI 10
GT          ; x > 10? (1=True, 0=False)

; 2. Decisão
JZ L1       ; Se 0 (False), pula para o ELSE (L1)

; 3. Bloco THEN
PUSHI 1
STORE 1     ; y = 1
JUMP L2     ; [IMPORTANTE] Pula o Else e vai para o fim

; 4. Bloco ELSE
LABEL L1    ; Ponto de aterrissagem do JZ
PUSHI 0
STORE 1     ; y = 0

; 5. Fim
LABEL L2    ; Ponto de encontro final
```