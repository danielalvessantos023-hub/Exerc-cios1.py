# aça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se
# ela é maior ou menor de idade

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) 


if idade >= 18 : 
    print(f"{nome} Você é Maior de idade" )
else: 
    print(f"{nome} Você é Menor de idade ")