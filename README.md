<div align="center">
  <h2> DSLs & Compilers Study</h2>
  <p>
    Repositório pessoal para estudos de <b>Compiladores</b>, <b>Interpretadores</b> e criação de <br/>
    <b>Linguagens de Domínio Específico (DSLs)</b>.
  </p>

  <img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=39d353" />
  <img src="https://img.shields.io/badge/ANTLR4-0d1117?style=flat-square&logo=antlr&logoColor=39d353" />
  <img src="https://img.shields.io/badge/Compilers-0d1117?style=flat-square&logo=compilerexplorer&logoColor=39d353" />
  <img src="https://img.shields.io/badge/Engenharia_Computação-0d1117?style=flat-square&logo=robotframework&logoColor=39d353" />
</div>
<br/>

## Projetos & DSLs

Aqui estão as linguagens e experimentos desenvolvidos, focando em análise léxica, sintática e semântica (Visitors).

| Projeto | Descrição & Conceitos | Status |
| :--- | :--- | :--- |
| **🚁 FlyPlan** | **DSL de Drones**. Define missões autônomas com waypoints (x,y,z) e comandos (takeoff, land, hover). Gera código Python para controle real. | ✅ Concluído |
| **📝 FormFlow** | **Formulários Interativos**. Sistema de perguntas com tipagem forte, validações (`min`, `max`) e ramificação condicional (`ask_if`). | ✅ Concluído |
| **⚙️ GameCfg** | **Configuração Hierárquica**. DSL para definir configurações de jogos (Vídeo, Áudio) com validação semântica de valores. | ✅ Concluído |
| **🧮 QuickMath** | **Math Interpreter**. Linguagem simples para declaração de variáveis e cálculo de expressões matemáticas. | ✅ Concluído |
| **🧠 Interpretador** | Estudos fundamentais sobre construção de interpretadores puros (sem geração de código). | 🚧 Em Andamento |


## Tecnologias & Ferramentas

* **Linguagem Host:** Python 3.x
* **Gerador de Parser:** ANTLR4 (Another Tool for Language Recognition)
* **Metodologia:** Visitor Pattern para caminhamento na árvore sintática (AST).

## Como Executar

A maioria dos projetos segue o padrão de gerar os arquivos do ANTLR e executar o visitor principal.

### Pré-requisitos
```bash
pip install antlr4-python3-runtime
```
### Gerando o Lexer/Parser
Para qualquer uma das DSLs (ex: FormFlow), entre na pasta e rode:

```bash
antlr4 -Dlanguage=Python3 -visitor <nome_arquivo>.g4
```
### Rodando o interpretador/gerador
```bash
python main.py
# ou
python codegenVisitor.py
```
<div align="center"> <p>Desenvolvido por <a href="https://www.google.com/search?q=https://github.com/alocinny"><b>Benny</b></a> 🐍</p> <p><i>Engenharia da Computação - UPE</i></p> </div>
