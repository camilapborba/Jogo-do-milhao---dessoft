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

import random
def sorteia_questao(dic,string):
    

    for nivel,questoes in dic.items():
        if nivel == string:
            return random.choice(questoes)


def sorteia_questao_inedita(dic, nivel, questoes_sorteadas):
    questao = sorteia_questao(dic, nivel)

    for questao_sorteada in questoes_sorteadas:
        if questao == questao_sorteada:
            return sorteia_questao_inedita(dic, nivel, questoes_sorteadas)

    questoes_sorteadas.append(questao)

    return questao

def questao_para_texto(dic,id):


    pergunta = dic["titulo"]
    
    opcaoA = dic["opcoes"]["A"]
    opcaoB = dic["opcoes"]["B"]
    opcaoC = dic["opcoes"]["C"]
    opcaoD = dic["opcoes"]["D"]

    final = f"----------------------------------------\nQUESTAO {id}\n\n{pergunta}\n\nRESPOSTAS:\nA: {opcaoA}\nB: {opcaoB}\nC: {opcaoC}\nD: {opcaoD}\n"

    return final

import random
def gera_ajuda(dic):
    incorretas = []
    novo = []

    certo = dic["correta"]

    for opcao in dic["opcoes"]:
        if opcao != certo:
            incorretas.append(opcao)
    
    dicas = random.randint(1,2)
    
    if dicas == 1:
        dica = random.choice(incorretas)
        
        opcaoA = dic["opcoes"][dica]
        final =f"DICA:\nOpções certamente erradas: {opcaoA}"

    
    elif dicas == 2:
        dica1 = random.choice(incorretas)
        
        for opcao in dic["opcoes"]:
            if opcao != dica1 and opcao!= certo:
                novo.append(opcao)
        
        dica2 = random.choice(novo)

        dica1 = dic["opcoes"][dica1]
        dica2 = dic["opcoes"][dica2]
        
        final = f'DICA:\nOpções certamente erradas: {dica1} | {dica2}'


    return final



