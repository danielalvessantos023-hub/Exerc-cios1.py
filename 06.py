#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês'
# mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele'
# efetuadas. Escrever um algoritmo que leia o nú mero de carros por ele vendidos, o valor total'
#  de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva '
# o salário final do vendedor.#

Numero_de_carros = int(input("Digite quantos carros você vendeu: "))
Valor_total_vendas = float(input("Digite o valor total de vendas: "))
Salário_fixo = float(input("Digite o valor dos eu salário:"))
Porcentagem_p_carro = float(input("Digite a Porcentagem de comoissão por carro: "))
Porcentagem_total_vendas = 5

comissão_total = (Porcentagem_p_carro * Numero_de_carros) + ((1 - Porcentagem_total_vendas/100)* Valor_total_vendas)
print("")
print(f"Seu salário final será de: R${Salário_fixo + comissão_total:.2f}")