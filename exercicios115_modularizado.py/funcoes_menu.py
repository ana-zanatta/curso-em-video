
pessoas_gerais = []

def cadastrar_pessoa():

    while True:

        # Dados de cadastro:

        cadastros_pessoas = {
            "nome": "",
            "cpf": "",
           
        }

        # Input solicitando os dados da escola.
        
        cadastros_pessoas["nome"] = input("Nome da pessoa: ")

        cadastros_pessoas["cpf"] = input("CPF: ")

        parar_cadastro = input("Deseja parar de cadastrar? [Sim/Não]: ").strip().upper()

        pessoas_gerais.append(cadastros_pessoas)
            
        if parar_cadastro == "SIM":
            break

# Função para ver as pessoas cadastradas:

def listar_pessoas():
    for indice, pessoa in enumerate(pessoas_gerais):
        print(indice, pessoa)





def menuPrincipal():

        # Print da mensagem "Menu Principal":

    while True:
        
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

        

