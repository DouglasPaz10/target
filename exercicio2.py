import json

arq = open('dados.json')

arq_interpretado = json.load(arq)

comparacao = []

arq_interpretado = [dict for dict in arq_interpretado if int(dict['valor']) != 0]

for dict in arq_interpretado:
    comparacao.append(dict['valor'])

minimo = min(comparacao)
maximo = max(comparacao)

for dict in arq_interpretado:
    if dict['valor'] == minimo:
        print('mês de menor valor: ', dict)

    if dict['valor'] == maximo:
        print('mês de maior valor: ', dict)


media_mensal = sum(comparacao)/ len(comparacao)
print('esta é a média mensal: ', media_mensal)


acima_da_media = []
for valor in comparacao:


    if valor > media_mensal:
        acima_da_media.append(valor)



print('numero de meses em que o faturamento foi maior que a média mensal: ', len(acima_da_media))
