# Funções em Python

# ___________________________


# Exercício 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área
# do terreno.
"""
def area(largura, comprimento):

    print("CONTROLE DE TERRENOS")
    print(F"{20*"-="}")
    
    resultado = largura * comprimento

    print(f"A área de um terreno de {largura}x{comprimento} é de {resultado}m².")



 
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

area(comprimento=comprimento, largura=largura)"""

# __________________________

# 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’) Saída: ***** Olá, Mundo! ***** (De acordo com o tamanho da frase)

# Jeito Guanabara:
"""
def escreva(msg):
    tam = len(msg) + 4
    print("*" * tam)
    print(f"  {msg}")
    print("*" * tam)


escreva("oioioioi")

"""

# Ideia junto com GPT:
"""
def escreva(msg):


    largura = len(msg) + 4

    print("*" * largura)
    print(msg.center(largura))
    print("*" * largura)


msg = input("Escreva uma mensagem: ")
escreva(msg)"""

# __________________________

# Exercício 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três
# contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

"""
from time import sleep

def contador(inicio, fim, passo):

    if passo < 0:
        passo*= -1

    if passo == 0:
        passo = 1

    print(f"Conte de {inicio} até {fim} pulando de {passo} em {passo}: ")

    if inicio < fim:

        cont = inicio 

        while cont <= fim:

            print(f"{cont}", end=" ", flush=True)

            sleep(0.5)

            cont += passo

        print("Fim")

    else:

        cont = inicio

        while cont >= fim:

            print(f"{cont}", end=" ", flush=True)

            sleep(0.5)

            cont -= passo

        print("Fim")


contador(1, 10, 1)
contador(10, 0, 1)

# Contagem persalizada:

print("Informe sua contagem personalizada: ")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contador(i, f, p)
"""

# ________________________________

# Exercício 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros de valores inteiros. Seu programa tem que analisar todos
# os valores e dizer qual deles é o maior.

"""
def maior(minha_lista):
       
    num_maior = minha_lista[0]

    for n in minha_lista:
        if n > num_maior:
            num_maior = n

    return num_maior


numeros = [10, 5, 8, 90, 34]
# numeros = [5, 6]
# numeros = [10, 5, 45, 1]
# numeros = [10]

maior_numero = maior(numeros) # Variável que recebe a função que acha o maior número

print(f"O maior número encontrado na lista {numeros} é o {maior_numero}. ")
"""

# ________________________

# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

"""
from random import randint 

def sorteia():

    sorteados = [] # Ou lista = [randint(1, 10) for _ in range(5)]

    for _ in range(5):

        num_lista = randint(1, 10)

        sorteados.append(num_lista)

    return sorteados


def somaPar(lista_num):

    num_par = 0

    for n in lista_num:

        if n % 2 == 0:
            num_par += n

    somados = num_par

    print(f"Os números pares da lista quando somados resultam em {somados}")


retorno = sorteia()

print(f"Os números sorteados foram {retorno}")

somaPar(retorno)
"""

# Jeito Guanabara:
"""
from random import randint

from time import sleep

def sorteia(lista):

    print("Sorteando 5 valores da lista: ", end="")

    for cont in range(5):

        n = randint(1, 10)

        lista.append(n)

        print(f"{n} ", end="", flush=True)

        sleep(0.5)

    print("Pronto!")

def somaPar(lista):

    soma = 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor

    print(f"O resultado da soma dos números pares da lista {lista} fica {soma}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
"""

# _______________________
