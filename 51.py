#Faça um algoritmo que imprima na tela a tabuada de 1 até 10
for numero in range(1, 11):
    print(f"\nTabuada do {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")