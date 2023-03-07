string = str(input('qual a palavra: '))

lista_caracteres = list(string)


tamanho_lista = len(lista_caracteres)


for i in range(tamanho_lista // 2):

    indice_inicial = i
    indice_final = tamanho_lista - 1 - i


    lista_caracteres[indice_inicial], lista_caracteres[indice_final] = lista_caracteres[indice_final], lista_caracteres[indice_inicial]


string_invertida = ''.join(lista_caracteres)


print(string_invertida)
