# 24. Faça uma funçã o que leia um nú mero nã o determinado de valores positivos e retorna a mé dia
# aritmé tica dos mesmos.

numero = []
while True:
    valor = int(input("Digite um valor positivo (Digite 0 para parar) "))
    numero.append(valor)

    if valor <= 0 :
        break


total = (sum(numero[:-1])) / len(numero[:-1])


print(f" Média aritmética dos valores digitados  = {total:.2f}")
