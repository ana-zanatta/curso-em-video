# Modularização em Python - Aula 22

# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(num, formatar=True):
    # A função aumentar() aumenta o valor recebido em 10%

    num_aumentado = num + (num * 0.10)

    if formatar:
        return moeda(num_aumentado)
        
    return num_aumentado


def diminuir(num, formatar=True):
    # A função diminuir() diminui o valor em 10%
    
    valor_subtraido = num - (num * 0.10)

    if formatar:
        return moeda(valor_subtraido)

    return valor_subtraido


def dobro(num, formatar=True):
    # A função dobro() multiplica o valor por 2

    dobro_num = num * 2

    if formatar:
        return moeda(dobro_num)
        

    return dobro_num


def metade(num, formatar=True):
    # A função metade() divide o valor por 2

    metade_num = num / 2

    if formatar:
        return moeda(metade_num)

    return metade_num


# Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

def moeda(num_processado):
    # A função moeda() será utilizada no print pegando o valor já processado pelas outras funções e reprocessando o valor já com o $ e a pontução.

    # Exemplo: 
    
    # num_processado == 1112.399999

    num_formatado = f"R${num_processado:,.2f}"

    # num_formatado == "R$1,112.39"

    num_formatado = num_formatado.replace(",", "X")
    
    # num_formatado == "R$1X112.39"

    num_formatado = num_formatado.replace(".", ",")
    
    # num_formatado == "R$1X112,39"

    num_formatado = num_formatado.replace("X", ".")
    
    # num_formatado == "R$1.112,39"

    # Tudo em uma única linha:
    # num_formatado = f"R${num_processado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    return num_formatado


# Exercício 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
# (Exercício 109 se localiza nas quatro funções.)

# Exercício 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações
# geradas pelas funções que já temos no módulo criado até aqui. (Não feito)

# Exercício 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas
# nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
















