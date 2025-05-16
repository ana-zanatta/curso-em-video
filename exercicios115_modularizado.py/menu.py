# 115a: Vamos criar um menu em Python, usando modularização.

import funcoes_menu


while True:

    retorno_menuPrincipal = funcoes_menu.menuPrincipal()
            
    if retorno_menuPrincipal == 1:
        funcoes_menu.listar_pessoas()

    elif retorno_menuPrincipal == 2:
        funcoes_menu.cadastrar_pessoa()

    elif retorno_menuPrincipal == 3:
        print("\033[0;31mEncerrando o programa... \033[m")
        break

    else:
        print("\033[0;31mErro! A opção digitada é inválida, tente novamente... \033[m")
    
