import random
import sys
from random import Random

# Criar um único gerador de números aleatórios
gerador = random.Random()


def apresentacao():
    """
    Exibe uma mensagem de boas-vindas ao usuário no sistema Little Calculator
    """
    print('Bem-vindo ao sistema Little Calculator')


def numeros_aleatorios(gerador):
    """
    Gera aleatoriamente os valores de N1 e N2, de 1 a 100, usando o gerador especificado.

    :param gerador: Instância de um gerador de números aleatórios
    :return: N1, N2
    """
    n1 = gerador.randint(1, 100)
    n2 = gerador.randint(1, 100)
    return n1, n2


def dificuldade():
    """
    Essa função deve coletar o nível de dificuldade escolhido pelo usuário, retornar a mesma, e verificar
    se é uma entrada válida, retornando erro caso não
    """
    #   Criando um loop que só será encerrado quando o usuário digitar 1 ou 2
    while True:
        #   Tente até...
        try:
            # Armazena a dificuldade escolhida pelo usuário
            usuario = int(input('Escolha o seu nível de dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): '))
            if 1 == usuario:
                #   Se o usuário escolher a opção 1, retorne a mensagem
                print('Você escolheu o nível fácil e possui 10 tentativas')
                break
            elif 2 == usuario:
                #   Se o usuário escolher a opção 2, retorne a mensagem
                print('Você escolheu o nível médio e possui 10 tentativas')
                break
            elif 3 == usuario:
                #   Se o usuário escolher a opção 3, retorne a mensagem
                print('Você escolheu o nível difícil e possui 10 tentativas')
                break
            else:
                #   Se o usuário escolher qualquer outro valor numérico
                print('Reposta incorreta, selecione apenas 1, 2 ou 3')
        except ValueError:
            #   Se a variável armazenar algum valor que não seja INT
            print('São permitidos apenas números de 1 até 3, tente novamente')
        except KeyboardInterrupt:
            #   Encerramento brusco do programa
            print('\nFinalizando o programa. Encerrando...')
            sys.exit()


def calculos():
    """
    Função que realiza os calculos matemáticos e armazena os valores em uma variável para que possam
    ser utilizados depois
    :return: valor_1, valor_2, soma, subtracao, multiplicacao, divisao
    """
    #   Retorna as duas váriaveis os números aleatórios gerados na função
    valor_1, valor_2 = numeros_aleatorios(gerador)

    # Armazena o valor de soma dos números
    soma = valor_1 + valor_2
    # Armazena o valor de subtracao dos números
    subtracao = valor_1 - valor_2
    # Armazena o valor de multiplicacao dos números
    multiplicacao = valor_1 * valor_2
    # Armazena o valor de divisao dos números
    divisao = valor_1 / valor_2

    return valor_1, valor_2, soma, subtracao, multiplicacao, divisao

def tentativas_usuario():

    corretas = 0
    erradas = 0
    for j in range(1,11):
        acertos, erros = questao()
        corretas += acertos
        erradas += erros
        if j == 10:
            print(f'Você teve {corretas} respostas certas.\n E {erradas} respostas erradas')

def questao():
    """
    Essa linha de código verifica se o calculo feito pelo usuário está correto
    """
    # Obter os valores armazenados nas váriaveis da função calculos
    valor_1, valor_2, soma, subtracao, multiplicacao, divisao = calculos()
    acertos = 0
    erros = 0
    while True:
        try:
            # Armazena a resposta do usuário
            calculo = int(input(f'Faça o cálculo de {valor_1} + {valor_2} : '))
            if calculo == soma:
                #   Se o usuário indicar um valor igual o da variável soma
                print('Você acertou, parabéns!')
                acertos += 1
                break
            else:
                print('Resposta incorreta!')
                erros += 1
                break
        except ValueError:
            print('Esses não são valores numéricos. Tente novamente!')
        except KeyboardInterrupt:
            print('\nPrograma finalizado. Encerrando...')
            sys.exit()
    return acertos, erros

# Chama a função e realiza a apresentação do programa
apresentacao()
dificuldade()
tentativas_usuario()
