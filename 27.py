# 27. Escreva um algoritmo que leia o nú mero de litros vendidos e o tipo de combustı́vel, calcule e
# imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço
# do litro do á lcool é R$ 2,90.


litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (G para gasolina / A para álcool): ").strip().upper()

if tipo == "G":
    valor = litros * 3.30
    print(f"Valor a pagar: R$ {valor:.2f}")

elif tipo == "A":
    valor = litros * 2.90
    print(f"Valor a pagar: R$ {valor:.2f}")

else:
    print("Tipo de combustível inválido.")
