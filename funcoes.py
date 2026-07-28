"""
Fortuna DesSoft - EP2
Jogo de perguntas e respostas em modo texto (terminal).
Tudo em um único arquivo: base de perguntas, as 7 funções obrigatórias,
funções de interface (print/input) e o jogo principal.
"""
 
import random
from perg import quest  # sua base de perguntas, em perg.py
 

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CIANO = "\033[96m"
NEGRITO = "\033[1m"
RESET = "\033[0m"
 
 

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


def cor_do_premio(premio):
    """Retorna uma cor diferente conforme a faixa de prêmio."""
    if premio >= 300000:
        return VERMELHO
    elif premio >= 30000:
        return AMARELO
    elif premio > 0:
        return VERDE
    return CIANO
 
 
def exibe_manual():
    print(f"\n{NEGRITO}{CIANO}{'=' * 55}{RESET}")
    print(f"{NEGRITO}{CIANO}   BEM-VINDO AO FORTUNA DESSOFT!{RESET}")
    print(f"{CIANO}{'=' * 55}{RESET}")
    print("Responda 9 perguntas de múltipla escolha (A, B, C ou D)")
    print("e acumule seu prêmio até chegar a R$ 1.000.000!")
    print()
    print("Em cada pergunta você pode:")
    print("  - Responder digitando A, B, C ou D;")
    print("  - Digitar 'pular' para trocar de pergunta (3 pulos no total);")
    print("  - Digitar 'ajuda' para eliminar respostas erradas (2 ajudas no total,")
    print("    sendo no máximo 1 ajuda por pergunta).")
    print()
    print("Se errar, o jogo acaba e você sai sem nenhum prêmio.")
    print("Após cada acerto, você pode parar e levar o valor já ganho!")
    print(f"{CIANO}{'=' * 55}{RESET}\n")
 
 
def pede_nome():
    nome = input("Qual é o seu nome? ").strip()
    while nome == "":
        nome = input("Nome inválido. Digite seu nome: ").strip()
    return nome
 
 
def exibe_estado(premio_atual, premio_em_jogo, pulos, ajudas):
    cor = cor_do_premio(premio_atual)
    print(f"\n{cor}{NEGRITO}Prêmio garantido: R$ {premio_atual:,}{RESET}".replace(",", "."))
    print(f"{cor}Jogando por: R$ {premio_em_jogo:,}{RESET}".replace(",", "."))
    print(f"Pulos restantes: {pulos} | Ajudas restantes: {ajudas}")
 
 
def pede_opcao(ajuda_disponivel, pulos_restantes):
    """Lê e valida a entrada do jogador: A, B, C, D, pular ou ajuda."""
    while True:
        bruto = input("\nSua resposta (A/B/C/D, 'pular' ou 'ajuda'): ").strip().upper()
 
        if bruto in ["A", "B", "C", "D"]:
            return bruto
 
        if bruto in ["PULAR", "PULA"]:
            if pulos_restantes > 0:
                return "PULAR"
            print(f"{VERMELHO}Você não tem mais pulos disponíveis!{RESET}")
            continue
 
        if bruto == "AJUDA":
            if ajuda_disponivel:
                return "AJUDA"
            print(f"{VERMELHO}Você já usou sua ajuda nesta pergunta (ou não tem mais ajudas)!{RESET}")
            continue
 
        print(f"{VERMELHO}Opção inválida. Digite A, B, C, D, 'pular' ou 'ajuda'.{RESET}")
 
 
def pede_sim_ou_nao(pergunta):
    while True:
        resp = input(pergunta).strip().lower()
        if resp in ["s", "sim"]:
            return True
        if resp in ["n", "nao", "não"]:
            return False
        print(f"{VERMELHO}Digite 's' para sim ou 'n' para não.{RESET}")
 

PREMIOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
PULOS_INICIAIS = 3
AJUDAS_INICIAIS = 2
 
 
def nivel_da_pergunta(indice):
    """As 9 perguntas são divididas em 3 fáceis, 3 médias e 3 difíceis."""
    if indice < 3:
        return "facil"
    elif indice < 6:
        return "medio"
    return "dificil"
 
 
def verifica_base_consistente(base_bruta):
    erros = valida_questoes(base_bruta)
    problemas = [(i, e) for i, e in enumerate(erros) if e]
 
    if problemas:
        print(f"{VERMELHO}Base de perguntas inconsistente! Corrija antes de jogar:{RESET}")
        for indice, erro in problemas:
            print(f"  Questão {indice}: {erro}")
        return False
    return True
 
 
def joga_uma_partida(base):
    nome = pede_nome()
    exibe_manual()
 
    pulos = PULOS_INICIAIS
    ajudas = AJUDAS_INICIAIS
    premio_atual = 0
    questoes_sorteadas = {"facil": [], "medio": [], "dificil": []}
 
    for indice, premio in enumerate(PREMIOS):
        nivel = nivel_da_pergunta(indice)
        respondida = False
 
        while not respondida:
            questao = sorteia_questao_inedita(base, nivel, questoes_sorteadas[nivel])
            ajuda_usada_nesta_questao = False
 
            while True:
                exibe_estado(premio_atual, premio, pulos, ajudas)
                print(questao_para_texto(questao, indice + 1))
 
                opcao = pede_opcao(ajudas > 0 and not ajuda_usada_nesta_questao, pulos)
 
                if opcao == "AJUDA":
                    print(gera_ajuda(questao))
                    ajudas -= 1
                    ajuda_usada_nesta_questao = True
                    continue
 
                if opcao == "PULAR":
                    pulos -= 1
                    print(f"{NEGRITO}Pergunta trocada!{RESET}")
                    break  # sorteia uma nova pergunta inédita do mesmo nível
 
                
                if opcao == questao["correta"]:
                    premio_atual = premio
                    print(f"\n{VERDE}{NEGRITO}Resposta correta! Prêmio atual: R$ {premio_atual}{RESET}")
 
                    if premio_atual == PREMIOS[-1]:
                        print(f"\n{NEGRITO}{VERDE}PARABÉNS, {nome}! Você ganhou R$ {premio_atual}!{RESET}")
                        return
 
                    if not pede_sim_ou_nao("Deseja continuar jogando? (s/n): "):
                        print(f"\n{nome}, você saiu do jogo com R$ {premio_atual}. Até a próxima!")
                        return
 
                    respondida = True
                    break
                else:
                    print(f"\n{VERMELHO}Resposta errada! A opção certa era '{questao['correta']}'.{RESET}")
                    print(f"{VERMELHO}{nome}, você não leva nenhum prêmio. Fim de jogo!{RESET}")
                    return
 
 
def main():
    base_bruta = quest
 
    if not verifica_base_consistente(base_bruta):
        return
 
    base = transforma_base(base_bruta)
 
    jogar_novamente = True
    while jogar_novamente:
        joga_uma_partida(base)
        jogar_novamente = pede_sim_ou_nao("\nDeseja jogar novamente? (s/n): ")
 
    print("\nObrigado por jogar Fortuna DesSoft!")
 
 
if __name__ == "__main__":
    main()
 
