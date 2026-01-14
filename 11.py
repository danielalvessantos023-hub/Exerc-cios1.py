#11. Ler 3 valores e escrever a soma dos 2 maiores.#


valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite um valor: "))
valor3 = float(input("Digite um valor: "))
print("")

if valor1 < (valor2 and valor3): 
    soma = (valor2) + (valor3)
    print("A soma dos 2 maiores valore é:",soma)

elif valor2 < (valor1 and valor3):
    soma2 = (valor1) + (valor3)
    print("A soma dos 2 maiores valore é:",soma2)

elif valor3 < (valor2 and valor1): 
    soma3 = (valor1) + (valor2)
    print("A soma dos 2 maiores valore é:",soma3)

else: 
    print("Dados inválidos")