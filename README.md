# Jogo-do-milhao---dessoft
#exercicio - Camila Borba

ortuna DesSoft

Jogo de perguntas e respostas no estilo "Show do Milhão", feito em Python puro para rodar no terminal (sem dependências externas).

Exercício Programa - Design de Software.

Como jogar

Requer apenas Python 3.8+ (nenhuma biblioteca externa é necessária).

bash
git clone <endereco-do-seu-repositorio>
cd fortuna_dessoft
python3 fortuna.py
Regras do jogo
O jogador informa seu nome.
O jogo exibe um pequeno manual (quantos pulos e ajudas ele tem).
A cada rodada, uma pergunta inédita é sorteada, com 4 alternativas (A, B, C, D).
O jogador escolhe entre:
A, B, C ou D, para responder a pergunta;
ajuda, que elimina 1 ou 2 alternativas sabidamente erradas;
pula, que sorteia outra pergunta do mesmo nível;
parar, que encerra o jogo e garante o prêmio já conquistado.
Acertando, o prêmio sobe conforme a tabela abaixo. Errando, o jogador perde tudo e o jogo acaba.
Numero	Premio (R$)	Nivel
1	1.000	Facil
2	5.000	Facil
3	10.000	Facil
4	30.000	Medio
5	50.000	Medio
6	100.000	Medio
7	300.000	Dificil
8	500.000	Dificil
9	1.000.000	Dificil

O jogo termina quando o jogador atinge R$ 1.000.000, erra uma pergunta, ou opta por parar (a cada acerto ele pode escolher continuar ou sair com o prêmio atual).

Pulos e ajudas
O jogador começa com 3 pulos e 2 ajudas (válidos para o jogo todo, não por pergunta).
Não é possível pedir ajuda mais de uma vez na mesma pergunta (o jogo valida e avisa).
Sem pulos ou ajudas disponíveis, o jogo avisa e repete a pergunta atual (ou pede outra opção).
Entradas inválidas (diferentes de A, B, C, D, ajuda, pula ou parar) são rejeitadas com uma mensagem de erro, e o jogo pede a resposta novamente sem consumir tentativas.
Exemplo de execução
Ok JOÃO, você tem direito a pular 3 vezes e 2 ajudas!
As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!

O jogo já vai começar! Lá vem a primeira questão!

____________________________________________________________

QUESTÃO 1

Qual o resultado da operação 57 + 32?

RESPOSTAS:
A: -19
B: 85
C: 89
D: 99

Qual sua resposta?! C

Você acertou! Seu prêmio atual é de R$ 10000.00
HEY! Você passou para o nível MEDIO!
Estrutura do projeto
Arquivo	Responsabilidade
base_perguntas.py	Base bruta de perguntas e respostas (facil, medio e dificil).
funcoes_jogo.py	As 7 funções obrigatórias do EP2 e as regras de validação/sorteio.
interface.py	Impressão em tela (com cores ANSI), leitura e validação de entradas.
fortuna.py	Loop principal do jogo (ponto de entrada: python3 fortuna.py).
Funções obrigatórias

Todas implementadas e testadas em funcoes_jogo.py, e efetivamente usadas por fortuna.py:

transforma_base(base_bruta): converte a base bruta (lista de tuplas) em uma lista de dicionários no formato usado pelo jogo.
valida_questao(questao): verifica se uma questão está consistente (campos obrigatórios, 4 alternativas, resposta correta válida etc).
valida_lista_questoes(lista_questoes): verifica se toda a base é consistente e sem perguntas repetidas.
sorteia_questao(lista_questoes): sorteia uma questão aleatória da lista.
sorteia_questao_inedita(lista_questoes, questoes_ja_usadas): sorteia uma questão que ainda não foi usada na partida.
questao_para_string(questao): formata a pergunta e as 4 alternativas como texto para exibição.
gera_ajuda(questao): sorteia 1 ou 2 alternativas sabidamente erradas para dar como dica.
Recursos extras
Cores no terminal: verde para prêmios menores, amarelo para prêmios médios e magenta para os prêmios mais altos; vermelho para erros e avisos e azul para mudança de nível.
Validação completa de entradas do usuário em todos os pontos do jogo (resposta da pergunta, continuar ou parar, nome).
Novo jogo sem reiniciar o programa: ao final de cada partida, o jogo pergunta se o jogador quer jogar novamente.
Base de perguntas ampliada (21 perguntas, 7 por nível), fácil de adicionar mais linhas em BASE_BRUTA, em base_perguntas.py.
Testes manuais realizados
Vitória alcançando R$ 1.000.000.
Derrota ao errar uma pergunta (perde tudo).
Uso de pula até esgotar os 3 pulos disponíveis.
Uso de ajuda e bloqueio ao tentar usá-la 2 vezes na mesma pergunta.
Entrada de opção inválida (por exemplo F, ganhar) sendo rejeitada corretamente.
Parar o jogo no meio, saindo com o prêmio acumulado até ali.
Autor

Desenvolvido individualmente como Exercício Programa da disciplina de Design de Software.