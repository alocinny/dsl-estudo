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
## Referência de Estudos

Documentação consolidada com os gabaritos de implementação e padrões utilizados na disciplina.

<table width="100%">
  <tr>
    <td width="100%" align="center">
      <a href="./RESUMO_GABARITOS.md">
        <img src="https://img.shields.io/badge/Acessar_Resumo_Técnico-➔-0d1117?style=for-the-badge&logo=readthedocs&logoColor=39d353&labelColor=0d1117&color=39d353" alt="Ver Gabaritos">
      </a>
    </td>
  </tr>
</table>

<div align="center"> 
  <sub>Built with 💀 by alocinny</sub></p> 
  <p><i>Engenharia da Computação - UPE</i></p> 
</div>


