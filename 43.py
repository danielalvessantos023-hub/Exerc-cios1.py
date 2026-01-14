# aça um algoritmo que leia trê s valores inteiros diferentes e imprima na tela os valores em ordem
# decrescente.

var1 = int(input("Digite um valor: "))
var2 = int(input("Digite um valor: "))
var3 = int(input("Digite um valor: "))
list = []
sorted(list, key=int, reverse=True)
list.append (int(var1)), list.append(int(var2)), list.append(int(var3))

print(f"Lista em ordem decrescente = {list}")