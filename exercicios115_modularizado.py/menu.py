# 115a: Vamos criar um menu em Python, usando modularização.

# Função que irá mostrar as opções e liberar o input para o usuário digitar qual opção ele quer (retorna o código da opção):

def menuPrincipal():

    # Print da mensagem "Menu Principal":

    msg = "MENU PRINCIPAL"
    tamanho = len(msg) + 20

    print("-" * tamanho)
    print(f"          {msg}")
    print("-" * tamanho)

    # Print das opções:

    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar pessoas")
    print("3 - Sair do sistema")

    print("-" * tamanho)

    # usuário digitará a opção no input abaixo:

    while True:

        try:
            opcao = input("Sua opção: ")

            opcao = int(opcao)

            if opcao in [1, 2, 3]:
                return opcao
            
            else:
                raise ValueError

        except (ValueError, TypeError):

            print("\033[0;31mErro! A opção digitada é inválida, tente novamente... \033[m")

            continue


retorno_menuPrincipal = menuPrincipal()

print(retorno_menuPrincipal) # Apenas para visualizar que está retornando o código escolhido pelo usuário


