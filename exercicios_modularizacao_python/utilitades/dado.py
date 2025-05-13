def leia_dinheiro():

    valor = input("Digite um valor: ").replace(".", "")

    if valor.count(",") > 1:
        print(f'Erro! Esse valor não é válido. ')
        return 0

    for caracter in valor:
        if not caracter.isdigit() and caracter != ",":
            print(f'Erro! "{valor}" não é um número. ')
            return 0
        

    # se não for deve acusar um erro de acordo com o que foi digitado, ex: "a" não é um valor válido ou "" não é um valor válido (com split para caso
    # digitarem com espaço)
    
    valor = valor.replace(",", ".")

    return float(valor)
