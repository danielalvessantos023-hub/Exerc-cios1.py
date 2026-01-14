# 22. Faça uma funçã o que recebe, por parâ metro, um valor inteiro e positivo e retorna o nú mero de
# divisores desse valor.

valor = int(input("Digite um número inteiro positivo: "))
print("")
contador = 0
for i in range(1,(valor) + 1):
    if valor % i == 0 :
        contador += 1
print(f"O número {valor} tem {contador} divisores")