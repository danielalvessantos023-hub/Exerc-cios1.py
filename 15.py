# 15. Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido


valores = []

for i in range (100):
    valor= int(input(f"Digite o {i + 1}º valor:"))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

print(f"O maior valor é: {maior}")
print(f"o menor valor é: {menor}")
