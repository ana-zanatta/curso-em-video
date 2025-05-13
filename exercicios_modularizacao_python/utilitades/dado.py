def leia_dinheiro():

    valor = input("Digite um valor: ").replace(".", "")

    if valor.count(",") > 1:
        print(f'Erro! Esse valor não é válido. ')
        return 0

    for caracter in valor:
        if not caracter.isdigit() and caracter != ",":
            print(f'Erro! "{valor}" não é um número. ')
            return 0
        
    valor = valor.replace(",", ".")

    return float(valor)
