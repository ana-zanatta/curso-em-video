# Aula 23: Tratamento de erros e exceções

# Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):

    while True:
         
        try:
            n = int(input(msg))

        except (ValueError, TypeError):

            print("\033[0;31mErro! Digite um número inteiro válido. \033[m")
            continue

        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interrompida pelo usuário! \033[m")
            return 0

        else:
           return n


# Programa principal

n = leiaInt("Digite um número inteiro: ")

print(f"Você acabou de digitar o número {n}. ")


def leiaFloat(msg):

    while True:
         
        try:
            n = float(input(msg))

        except (ValueError, TypeError):

            print("\033[0;31mErro! Digite um número real válido. \033[m")
            continue

        else:
           return n

    
# Programa principal

n = leiaFloat("Digite um número real: ")

print(f"Você acabou de digitar o número {n}. ")"""


# Exercício 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import requests

response = requests.get(url="https://google.com")
print(response.text)
"""


"""
import urllib

import urllib.request

try: 
    site = urllib.request.urlopen("https://google.com")

except urllib.error.URLError:
    print("O site está indisponível no momento! ")

else:
    print("O site foi acessado com sucesso! ")
"""

# Exercício 115: Vamos criar um menu em Python, usando modularização.
# (Exercício resolvido nos arquivos dentro do módulo exercicios115_modularizado.py)