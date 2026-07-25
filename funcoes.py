def transforma_base(questoes):
    base = {}

    i = 0
    while i < len(questoes):
        questao = questoes[i]
        nivel = questao["nivel"]

        if nivel not in base:
            base[nivel] = []

        base[nivel].append(questao)

        i += 1

    return base

def valida_questao(questao):
    erros = {}

    if "titulo" not in questao:
        erros["titulo"] = "nao_encontrado"

    if "nivel" not in questao:
        erros["nivel"] = "nao_encontrado"

    if "opcoes" not in questao:
        erros["opcoes"] = "nao_encontrado"

    if "correta" not in questao:
        erros["correta"] = "nao_encontrado"

    if len(questao) != 4:
        erros["outro"] = "numero_chaves_invalido"

    if "titulo" in questao:
        if questao["titulo"].strip() == "":
            erros["titulo"] = "vazio"

    if "nivel" in questao:
        if questao["nivel"] not in ["facil", "medio", "dificil"]:
            erros["nivel"] = "valor_errado"

    if "opcoes" in questao:
        if len(questao["opcoes"]) != 4:
            erros["opcoes"] = "tamanho_invalido"

        elif set(questao["opcoes"].keys()) != {"A", "B", "C", "D"}:
            erros["opcoes"] = "chave_invalida_ou_nao_encontrada"

        else:
            vazias = {}

            for letra, resposta in questao["opcoes"].items():
                if resposta.strip() == "":
                    vazias[letra] = "vazia"

            if len(vazias) > 0:
                erros["opcoes"] = vazias

    if "correta" in questao:
        if questao["correta"] not in ["A", "B", "C", "D"]:
            erros["correta"] = "valor_errado"

    return erros

def valida_questoes(lista):
    resultado = []
    for ex in lista:
        erros = valida_questao(ex)
        resultado.append(erros)
    return resultado
