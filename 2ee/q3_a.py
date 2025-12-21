var_livre = []
var_declar = []
var_ambigua = []

def analisa(t, escopo = []):
	case LogicaParser.QuantAllContext | LogicParser.QuantxistContext():
		var = t.VAR().getText
		if var in escopo:
			var_ambigua.append(var)
		else:
			var_declar.append(var)
		analisa(t.formula(), escopo + [var])

	case LogicParser.ImpliesContext() | LogicParser.CombinadorOrContext() | LogicParser.CombinadorAndContext():
		analisa_logica(t.formula(0), escopo)
		analisa_logica(t.formula(1), escopo)
	case LogicParser.PredicadoContext():
		for exp in t.exp():
			analisa(exp, escopo)
	case LogicParser.VarContext():
		var = t.VAR().getText()
		if nome not in escopo:
			var_livre.append(var)
	case LogicParser.ParensContext():
		analisa(t.formula(), escopo)
		
