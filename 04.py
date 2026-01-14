# 04. Escreva um algoritmo para ler o salá rio mensal atual de um funcioná rio e o percentual de reajuste.
# Calcular e escrever o valor do novo salá rio.



Setembro = float(input("Digite seu salário de Setembro: "))
Outubro = float(input("Digite a porcentagem de reajuste para Outubro: "))
Novembro = float(input("Digite a porcentagem de reajuste para novembro: "))
Dezembro = float(input("Digite a porcentagem de reajuste para Dezembro: "))
print("")

SalOutubro = Setembro * (1+Outubro/100)
print(f"O salário de Outubro será de: R${SalOutubro:.2f}")


SalNovembro = SalOutubro * ( 1 + Novembro/100)
print(f"O salário de Novembro será de: R${SalNovembro:.2f}")


SalDezembro = SalNovembro * ( 1 + Dezembro/100)
print(f"O salário de Dezembro será de: R${SalDezembro:.2f}")
print("")

print(f"O aumento real entre Setembro e Dezembro foi de: R${SalDezembro-Setembro:.2f}")
print(f"O aumento percentual total entre Setembro e Dezembro foi de: {(SalDezembro-Setembro)/Setembro:.2%}")



