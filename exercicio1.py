sequencia_de_fibonnaci = [0, 1, 1]

range_user = int(input('numero máximo da sequência: '))

for num in range(range_user - 2):
    ultimo_numero = str(sequencia_de_fibonnaci[-1])
    penultimo_numero = str(sequencia_de_fibonnaci[-2])

    soma = int(ultimo_numero) + int(penultimo_numero)

    sequencia_de_fibonnaci.append(soma)

print(sequencia_de_fibonnaci)
