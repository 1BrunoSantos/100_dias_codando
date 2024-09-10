"""
A pesquisa binária é um método inteligente para encontrar um número em uma lista ordenada. Ela funciona dividindo a lista ao meio repetidamente até encontrar o número que você procura. É como procurar uma palavra em um dicionário: você não começa pela primeira página, e sim por uma página do meio.

"""

def pesquisa_binaria(lista,item):
    baixo = 0 
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1

        else:
            baixo = meio + 1

    return None

def calcular_max_etapas(tamanho_lista):
    etapas = 0 
    while (2 ** etapas) < tamanho_lista:
        etapas += 1
    return etapas

tamanho_lista_128 = 128
tamanho_lista_256 = 256

print(f"O número máximo de etapas para uma lista de tamanho {tamanho_lista_128} é {calcular_max_etapas(tamanho_lista_128)}")
print(f"O número máximo de etapas para uma lista de tamanho {tamanho_lista_256} é {calcular_max_etapas(tamanho_lista_256)}")




