# 05. O custo de um carro novo ao consumidor é a soma do custo de fá brica com a porcentagem do
# distribuidor e dos impostos (aplicados ao custo de fá brica). Supondo que o percentual do distribuidor
# seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fá brica de um carro,
# calcular e escrever o custo final ao consumidor.


Valor_de_produção = float(input("Digite o custo de fábrica do veículo: "))
Impostos = 45
Distribuidor = 28 

print("")
print(f"O valor final do veículo será de: R${Valor_de_produção * (1+Impostos/100) *(1+ Distribuidor/100):.2f}")