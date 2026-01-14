# Faça um algoritmo para receber um nú mero qualquer e imprimir na tela se o nú mero é par ou
# ı́mpar, positivo ou negativo.

numero = int(input("Digite um valor: "))
print("")

if numero > 0 and numero %2==0 :
    print("O numero {numero} é Par e Positivo")
    
elif numero > 0 and numero %2 != 0 :
    print("O numero {numero} é Ímpar e Positivo")

elif numero < 0 and numero %2 == 0 : 
    print("O numero {numero} é Par e Negativo")
    
elif numero < 0 and numero %2 != 0 :
    print("O numero {numero} é Ímpar e Negativo")
    
else: 
    print("O numero {numero} é = 0")