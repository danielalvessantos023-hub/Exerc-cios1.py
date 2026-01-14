#
# Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá
# somar os dois valores, caso contrá rio devera multiplicar A por B. Ao final de qualquer um dos cá lculos
# deve-se atribuir o resultado a uma variá vel C e imprimir seu valor na tela.


a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
C = []
if a == b : 
    c = a + b 
    C.append(c)
    print(f"A é igual a B, Então soma = {C[0]}")

elif  a != b :
    c = a *b 
    C.append(c)
    print(f"A é diferente de B, Então multiplicação = {C[0]}")