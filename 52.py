# Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada

n = int(input("Digite um numero: "))

print('')
print(f"Tabuada do {n}")
print('')

for i in range (1, 11):
   resultado = n * i
   print(f"{n} X {i} = {resultado}")
