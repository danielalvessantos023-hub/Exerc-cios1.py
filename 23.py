#23. Faça uma funçã o que receba um valor inteiro e positivo e calcula o seu fatorial.\


valor = int(input("Digite um número inteiro positivo: "))
print("")
fatorial = 1
for i in range(2,(valor) + 1):
    if valor / i:
        fatorial *= i
print(f"O número {valor} tem {fatorial}!")