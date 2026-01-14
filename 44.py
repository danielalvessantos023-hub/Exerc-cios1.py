# Faça um algoritmo que calcule o IMC (I'ndice de Massa Corporal) de uma pessoa, leia o seu peso e
# sua altura e imprima na tela sua condiçã o de acordo com a tabela abaixo:
# Fó rmula do IMC = peso / (altura) ²
# Tabela Condiçõ es IMC
# -Abaixo de 18,5| Abaixo do peso
# -Entre 18,6 e 24,9| Peso ideal (parabé ns)
# -Entre 25,0 e 29,9| Levemente acima do peso
# -Entre 30,0 e 34,9| Obesidade grau I
# - Entre 35,0 e 39,9| Obesidade grau II (severa)
# - Maior ou igual a 40| Obesidade grau III (mó rbida)


alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
#calculo imc#
imc = peso/(alt**2)
print("")

if imc < 18.5 :
    print(f"Você IMC = {imc:.2f} e está Abaixo do peso")
    
elif imc >= 18.6 and imc <= 24.9 :
    print(f"Você IMC = {imc:.2f} e está Peso ideal (parabéns)")
    
elif imc >= 25 and imc <= 29.9:
    print(f"Você IMC = {imc:.2f} e está levemente acima do peso") 

elif imc >= 30 and imc <=34.9:
    print(f"Você IMC = {imc:.2f} e está Obesidade grau 1")
    
elif imc >= 35 and imc <=39.9:
    print(f"Você IMC = {imc:.2f} e está obesidade grau II")
else: 
    print(f"Você IMC = {imc:.2f} e está obesidade grau III (Mórbida)")

