def otimiza(t):
    match t:
        # --- O FOCO DA QUESTÃO (Quantificador) ---
        case LogicParser.QuantAllContext():
            var = t.VAR().getText()
            # 1. Otimiza o filho primeiro (recursão)
            corpo_str = otimiza(t.formula())
            
            # 2. Verifica se a variável é útil
            # Se 'x' aparece no texto do corpo, mantemos o 'all x'
            if var in corpo_str:
                return f"all {var}, {corpo_str}"
            else:
                # OTIMIZAÇÃO: Jogamos o 'all' fora e retornamos só o corpo
                return corpo_str

        # --- NOVIDADE: IMPLIES ---
        case LogicParser.ImpliesContext():
            esq = otimiza(t.formula(0))
            dir = otimiza(t.formula(1))
            return f"{esq} -> {dir}"

        # --- OUTROS (Repassa) ---
        case LogicParser.AndContext():
            return f"{otimiza(t.formula(0))} and {otimiza(t.formula(1))}"
            
        case LogicParser.PredicadoContext():
            return t.getText()
            
        case _:
            return t.getText()
