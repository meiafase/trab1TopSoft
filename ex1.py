"""

    Exercicio 01 Jogo da Velha 4x4.

Cada jogador (X e O) faz uma jogada por vez, alternando entre eles.

O jogador atual escolhe uma linha e uma coluna onde deseja colocar sua peça.

O código verifica se a posição escolhida está vazia. Se estiver, o jogador atual coloca sua peça nessa posição.
Se não estiver vazia, o jogador é solicitado a escolher outra posição.

Após cada jogada, o código verifica se o jogador atual venceu. Isso é feito verificando se há quatro de suas peças em
linha horizontal, vertical ou diagonal. Se o jogador vencer, o jogo termina e a vitória é anunciada.

O jogo continua até que um jogador vença ou o tabuleiro esteja completamente preenchido (empate).

"""

def mostrarTabuleiro(tabuleiro):
    #mostra o tabuleiro 4x4.
    
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 9)

def criarTabuleiro():
    #Cria um tabuleiro vazio 4x4 como uma lista de listas.
    
    tabuleiro = [[' ' for _ in range(4)] for _ in range(4)]
    return tabuleiro

def verificarVitoria(tabuleiro, jogador):
    #Verifica se um jogador venceu o jogo.
    
    for linha in tabuleiro:
        if all(simbolo == jogador for simbolo in linha):
            return True

    for coluna in range(4):
        if all(tabuleiro[i][coluna] == jogador for i in range(4)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False


def fazerJogada(tabuleiro, jogador, linha, coluna):
    #Realiza a jogada de um jogador em uma posição específica do tabuleiro.
    
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Posição ja escolhida. Tente novamente.")
        return False

def jogoVelha():
    #Função principal para jogar o jogo.

    tabuleiro = criarTabuleiro()
    jogadorDaVez = 'X'
    vecedor = None
    jogadas = 0

    while True:
        mostrarTabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogadorDaVez}")

        linha = int(input("Digite o número da linha (0 a 3): "))
        coluna = int(input("Digite o número da coluna (0 a 3): "))

        if linha < 0 or linha > 3 or coluna < 0 or coluna > 3:
            print("Posição inválida. Tente novamente.")
            continue

        if fazerJogada(tabuleiro, jogadorDaVez, linha, coluna):
            jogadas += 1
            if jogadas >= 8:
                vecedor = jogadorDaVez if verificarVitoria(tabuleiro, jogadorDaVez) else None

            if vecedor or jogadas == 16:
                break

            jogadorDaVez = 'O' if jogadorDaVez == 'X' else 'X'

    mostrarTabuleiro(tabuleiro)

    if vecedor:
        print(f"O jogador {vecedor} venceu!")
    else:
        print("O jogo empatou!")

jogoVelha()