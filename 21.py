# 21. Faça um procedimento que lê 50 valores inteiros e retorna o maior e o menor deles.

numeros = []
for i in range(50):
    n = int(input(f"Digite um número inteiro {i + 1}: ")) 
    numeros.append(n)
menor = min(numeros)
maior = max(numeros)
print(f"O menor valor digitado foi {menor} e o maior foi {maior}")