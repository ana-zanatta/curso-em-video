# Aula 21: Funções parte 2



# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import datetime

def voto(ano_nasc):

    ano_atual = datetime.now().year

    idade = ano_atual - ano_nasc

    if idade < 18:
        return print(f"Com {idade} anos: VOTO NEGADO. ")
    
    elif 18 < idade < 65:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO. ")
    
    elif idade > 65:
        return print(f"Com {idade} anos: VOTO OPCIONAL. ")
    
    else:
        return print("Valor inválido... Digite novamente.")


voto(int(input("Em que ano você nasceu? ")))"""

# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num, show=True):
    """
"""
    A Função fatorial() calcula o fatorial de um número;
    O parâmetro num é passado pelo input que há dentro da chamada da função;
    O parâmetro opcional show=, que recebe True ou False, determina se será mostrado no terminal a conta realizada pela função para chegar no resultado final
    O return retorna o valor que se define válido para ser mostrado no terminal, que seria o resultado da função fatorial;
    """
"""

    fatorial = 1

    for c in range(num, 0, -1):

        print(c, end="") 

        if show == True:
            if c > 1:
                print(f" x ", end="")
            else:
                print(" = ", end="")  

        fatorial *= c

    return fatorial


print(fatorial(int(input("Digite um número para calcular o fatorial: "))))

# help(fatorial)
# """

# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')

# Programa principal
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip()

# Tratando possíveis entradas vazias

# if gols.isnumeric():
#     gols = int(gols)
# else:
#     gols = 0

gols = int(gols) if gols.isnumeric() else 0

# if nome == '':
#     ficha(gols=gols)
# else:
#     ficha(nome, gols)

ficha(gols=gols) if nome == '' else ficha(nome, gols)
"""

# Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""
def leiaInt(msg):

    ok = False

    valor = 0

    while True:

        n = str(input(msg))

        if n.isnumeric():

            valor = int(n)

            ok = True

        else:
            print("\033[0;31mErro! Digite um número inteiro válido. \033[m")

        if ok:

            break

    return valor
    
# Programa principal

n = leiaInt("Digite um número: ")

print(f"Você acabou de digitar o número {n}. ")

"""

# Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
# Quantidade de notas;
# A menor nota;
# A média da turma;
# A situação (opcional);
"""
def notas(*n, sit=True):
    
#    -> função para analisar notas e situação de vários alunos.
#    :param n: Uma ou mais notas dos alunos (aceita várias);
#    :param sit: Valor opcional, indicado se deve ou não adicionar a situação;
#    :return: Dicionário com várias informações sobre a situação das notas.


    r = dict()

    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
   
    if sit == True:

        if r["media"] >= 7:
            print("A situação é BOA. ")

        elif 7 > r["media"] > 5:
            print("A situação é RAZOÀVEL. ")

        else:
            print("A situação é RUIM. ")
    
    return r
   

# Programa principal:

resposta = notas(2.5, 5, 6, 9)
print(resposta)
"""

# Exercício 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

"""
c = (
    "\033[m",         # 0 - sem cor
    "\033[0;30;41m",  # 1 - vermelho
    "\033[0;30;42m",  # 2 - verde
    "\033[0;30;43m",  # 3 - amarelo
    "\033[0;30;44m",  # 4 - azul
    "\033[0;30;45m",  # 5 - roxo
    "\033[7;30m"      # 6 - branco invertido
)

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end="")
    print("~" * tamanho)
    print(f"  {msg}")
    print("~" * tamanho)
    print(c[0], end="")

# Programa principal:
comando = ""

while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = input("Função ou Biblioteca: ").strip()
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
"""