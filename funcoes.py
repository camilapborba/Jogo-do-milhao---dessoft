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