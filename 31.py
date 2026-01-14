#Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

reajuste = 5

valor = int(input("Digite um valor: "))
print("")
valor_reajustado = valor * (1 + reajuste/100)
print(f"Valor reajustado é igual a {valor_reajustado:.2f}")
 