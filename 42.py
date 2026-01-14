
# Faça um algoritmo que leia dois valores booleanos (ló gicos) e determine se ambos sã o
# VERDADEIRO ou FALSO.



v1 = input("Digite um numero (1 para VERDADEIRO e 0 para FALSO): ")
v2 = input("Digite um numero (1 para VERDADEIRO e 0 para FALSO): ")


if v1 == "1" and v2 == "1" :
    print("Ambos os valores são verdadeiros")

elif v1 == "0" and v2 == "0" :
    print("Ambos os valores são falsos")

elif v1 != v2:
    print("Ambos valores são diferentes e")

    if v1 == "1" and v2 == "0":
        print("O primeiro valor é verdadeiro e o segundo é falso")
    
    elif v1 == "0" and v2 == "1" :
        print("O primeiro valor é falso e o segundo é verdadeiro")
