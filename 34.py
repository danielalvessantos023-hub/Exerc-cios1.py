# Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura
# correspondente em grau Celsius. Imprima na tela as duas temperaturas. Fó rmula: C = (5 * ( F-32) / 9)


fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (5 * (fahrenheit - 32)) / 9

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura em Celsius: {celsius:.2f} °C")