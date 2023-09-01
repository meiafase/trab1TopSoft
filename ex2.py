"""

    Exercicio 02 Jogo da Velha NxN.

Função criarTabuleiro:
Esta função cria um tabuleiro vazio com o número especificado de linhas e colunas.
Ele usa uma lista de listas (matriz) para representar o tabuleiro, onde cada elemento
representa uma célula do tabuleiro. O tabuleiro começa vazio, com todos os elementos
preenchidos com espaços em branco.

Função imprimirTabuleiro:

Esta função recebe o tabuleiro como entrada e imprime-o no console. Ela utiliza loops
para percorrer o tabuleiro e imprimir as células e as linhas que separam as linhas e
colunas.

Função verificarVitoria:

Esta função verifica se um jogador ganhou o jogo. Ela recebe o tabuleiro, o jogador
atual, a linha e a coluna da última jogada como entrada.
A função verifica a linha, a coluna, a diagonal principal e a diagonal secundária a
partir da posição da última jogada para ver se todas as células contêm o símbolo do
jogador atual.
Se qualquer uma dessas verificações for verdadeira, a função retorna True, indicando
que o jogador venceu. Caso contrário, retorna False.

Função jogoVelha:

Esta função é a principal do jogo. Ela começa pedindo ao jogador que escolha o número de linhas e colunas para criar o tabuleiro.
Em seguida, inicializa o tabuleiro com a função criarTabuleiro, define o jogador atual como 'X' e o número de jogadas como 0.
O jogo entra em um loop principal onde os jogadores alternam fazendo suas jogadas. O loop continua até que haja um vencedor ou empate.
Em cada iteração do loop, o tabuleiro é impresso, e o jogador atual é solicitado a fazer uma jogada. A jogada é validada para garantir
que esteja dentro dos limites do tabuleiro e que a célula escolhida esteja vazia.
Após cada jogada, o código verifica se o jogador atual venceu usando a função verificarVitoria. Se houver um vencedor, o jogo é
encerrado e o vencedor é anunciado.
Se não houver um vencedor e o número de jogadas atingir o máximo (linhas * colunas), o jogo termina em empate.
Caso contrário, o jogador atual é alternado para o próximo, e o loop continua.

"""


def criarTabuleiro(linhas, colunas):
#Cria o tabuleiro
    tabuleiro = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
#Mostra o tabuleiro
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * (4 * len(linha) - 1))

def verificarVitoria(tabuleiro, jogador, linha, coluna):
#Verifica se tem algum vencedor da rodada
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    
    # Verificar a linha
    if all(tabuleiro[linha][i] == jogador for i in range(colunas)):
        return True
    
    # Verificar a coluna
    if all(tabuleiro[i][coluna] == jogador for i in range(linhas)):
        return True
    
    # Verificar a diagonal principal
    if linha == coluna and all(tabuleiro[i][i] == jogador for i in range(min(linhas, colunas))):
        return True
    
    # Verificar a diagonal secundária
    if linha + coluna == linhas - 1 and all(tabuleiro[i][colunas - 1 - i] == jogador for i in range(min(linhas, colunas))):
        return True
    
    return False

def jogoVelha():
#Funcao que inicia o jogo
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    
    tabuleiro = criarTabuleiro(linhas, colunas)
    jogadorDaVez = 'X'
    jogadas = 0
    
    while True:
        imprimirTabuleiro(tabuleiro)
        print(f'Jogador {jogadorDaVez}, é a sua vez!')
        linha = int(input("Digite o número da linha (1 a {0}): ".format(linhas)))
        coluna = int(input("Digite o número da coluna (1 a {0}): ".format(colunas)))
        
        if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas or tabuleiro[linha][coluna] != ' ':
            print("Jogada inválida. Tente novamente.")
            continue
        
        tabuleiro[linha][coluna] = jogadorDaVez
        jogadas += 1
        
        if verificarVitoria(tabuleiro, jogadorDaVez, linha, coluna):
            imprimirTabuleiro(tabuleiro)
            print(f"O jogador {jogadorDaVez} venceu!")
            break
        
        if jogadas == linhas * colunas:
            imprimirTabuleiro(tabuleiro)
            print("Empate!")
            break
        
        jogadorDaVez = 'O' if jogadorDaVez == 'X' else 'X'

jogoVelha()