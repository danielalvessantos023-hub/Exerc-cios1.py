
#Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela
# o quociente e o resto da divisã o inteira entre eles.\


i = int(input("Digite um valor para 'A' (dividendo): "))
A = i

while True:
    B = int(input("Digite um valor para 'B' (divisor): "))
    if B == 0 : 
        print("Divisão por 0 não é permitida, digite outro valor")
    else:
        break

print(f"A divido por B = {A/B}")
print(f"Divisão inteira de A por B = {A//B} com resto {A%B}")