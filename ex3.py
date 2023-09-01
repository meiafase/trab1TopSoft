"""

    Exercicio 03 Jogo Termoo.

obterPalavras(txt):
Esta função é responsável por carregar a lista de palavras do arquivo especificado.
Ela lê o arquivo linha por linha, remove espaços em branco extras e converte
todas as palavras para letras minúsculas. Em seguida, retorna uma lista de palavras.

selecionarPalavras(palavras):
Esta função escolhe aleatoriamente uma palavra da lista de palavras fornecida como entrada
usando a biblioteca random. A palavra escolhida será a palavra que o jogador tentará adivinhar.

jogarTermoo():
A função jogarTermoo é a função principal do jogo. Ela orquestra todo o processo de jogo e interage com o jogador.
Primeiro, carrega a lista de palavras do arquivo "lista.txt" usando a função obterPalavras.
Se o arquivo "lista.txt" não for encontrado, ele exibe uma mensagem de erro e encerra o jogo.
Em seguida, escolhe uma palavra aleatória da lista usando a função selecionarPalavras.
Inicializa uma lista vazia chamada letras_corretas para rastrear as letras que o jogador adivinhou corretamente.
Define o número máximo de tentativas como 6
Inicia o contador de tentativas em 0.

Loop Principal:
O jogo entra em um loop que continua até que o jogador adivinhe a palavra corretamente,
atinja o número máximo de tentativas ou decida sair.
A cada iteração do loop, o jogo verifica se o jogador adivinhou corretamente todas as
letras da palavra e, se o fizer, exibe uma mensagem de vitória e encerra o jogo.
Caso contrário, o jogo exibe a palavra oculta, onde letras não adivinhadas são representadas
por "_". O jogador pode então fazer uma tentativa digitando uma única letra.
Se a letra digitada não for válida, o jogo exibe uma
mensagem de erro.
Se a letra já tiver sido tentada antes, o jogo também exibe uma mensagem de erro.
Se a letra digitada for parte da palavra oculta, ela é adicionada à lista letras_corretas.
Se a letra não fizer parte da palavra, o contador de tentativas é incrementado e o jogo exibe o número de tentativas restantes.
O loop continua até que o jogador adivinhe a palavra corretamente, esgote todas as tentativas ou decida sair.

Final do Jogo:
Quando o jogo termina, seja por vitória ou derrota, ele exibe uma mensagem apropriada para o jogador,
informando se eles venceram adivinhando a palavra ou se esgotaram suas tentativas.

"""


import random

def obterPalavras(txt):
#Encontra o arquivo e pega as palavras
    try:
        with open(txt, 'r') as arquivo:
            palavras = arquivo.readlines()
            palavras = [palavra.strip().lower() for palavra in palavras]
            return palavras
    except FileNotFoundError:
        print("!!!!!!! erro ao encontrar o .txt")
        return []

def selecionarPalavra(palavras):
#Seleciona uma palavra aleatoria
    return random.choice(palavras)

def jogarTermoo():
#Funcao que inicia o jogo
    print(" --- TERMOO JOGUINHO! --- ")
    palavras = obterPalavras("lista_palavras.txt")

    if not palavras:
        return

    palavra = selecionarPalavra(palavras)
    letrasCertas = []
    tentativasMaximas = 6
    tentativas = 0

    while tentativas < tentativasMaximas:
        palavraEscondida = ""
        for letra in palavra:
            if letra in letrasCertas:
                palavraEscondida += letra
            else:
                palavraEscondida += "_"

        print(f"Palavra: {palavraEscondida}")
        letraTentativa = input("Digite uma letra: ").lower()

        if len(letraTentativa) != 1 or not letraTentativa.isalpha():
            print("Insira apenas letra válida.")
            continue

        if letraTentativa in letrasCertas:
            print("Você já tentou esta letra.")
            continue

        if letraTentativa in palavra:
            letrasCertas.append(letraTentativa)
            if palavraEscondida == palavra:
                print(f"Parabéns! a palavra é '{palavra}'!")
                break
        else:
            tentativas += 1
            print(f"Letra '{letraTentativa}' não está na palavra. jogadas restantes: {tentativasMaximas - tentativas}")

    if tentativas == tentativasMaximas:
        print(f"Você esgotou suas tentativas. a palavra era '{palavra}'.")

jogarTermoo()