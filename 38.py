# Faça um algoritmo que calcule a quantidade de litros de combustı́vel gastos em uma viagem,
# sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuá rio o tempo que será gasto na
# viagem a sua velocidade mé dia, distâ ncia percorrida e a quantidade de litros utilizados para fazer a
# viagem.


consumo_lt = 12 #km#
tempo = float(input("Digite quanto tempo durou sua viagem: "))
velocidade = float(input("Digite a velocidade média: "))

distancia = tempo * velocidade 
consumo = distancia / consumo_lt

print(f"Seu consuomo médio = {consumo:.2f} litros")
