# Faça um algoritmo que leia o valor do salá rio mı́nimo e o valor do salá rio de um usuá rio, calcule
# quantos salá rios mı́nimos esse usuá rio ganha e imprima na tela o resultado. (Base para o Salá rio
# mı́nimo R$ 1.293,20).

salário_min = 1239.2
salário_usuário = float(input("Digite o valor do seu salário: "))

qts_mins = (salário_usuário / salário_min)

print (f"Você recebe {qts_mins:.2f} salários minimos ")
