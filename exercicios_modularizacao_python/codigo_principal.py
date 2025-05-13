# Neste arquivo será incluído o código principal, que irá operar as funções aumentar(), diminuir(), dobro() e metade() do arquivo moeda.py

import utilitades.moeda as moeda

from utilitades.dado import leia_dinheiro

valor = leia_dinheiro()

print(f"O valor recebido aumentado em 10% fica {(moeda.aumentar(valor, formatar=False))}")

print(f"O valor digitado menos 10% resulta em {(moeda.diminuir(valor, formatar=True))}")

print(f"Se dobrarmos o valor digitado resulta em {(moeda.dobro(valor, formatar=False))}")

print(f"E se dividirmos o valor recebido pela metado fica {(moeda.metade(valor, formatar=True))}")