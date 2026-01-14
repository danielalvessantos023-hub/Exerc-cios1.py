# Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é
# mostre se a soma é menor que C.

A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
C = int(input("Digite um valor para C: "))

print("")
if (A + B) < C :
    print(f"A soma de A + B = {A + B} e é menor que C = {C}")
    
elif (A  + B) > C :
    print(f"A soma de A + B = {A + B} e é maior que C = {C}") 
    
else:
    print(f"A soma de A + B = {A + B} e é igual que C = {C}")  