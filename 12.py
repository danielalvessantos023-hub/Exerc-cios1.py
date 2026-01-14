# 12. Ler dois valores e imprimir uma das trê s mensagens a seguir:
# ‘Nú meros iguais’,
# caso os nú meros sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’,
# caso o segundo seja maior que o primeiro.



valor1 = input("Digite um valor: ")
valor2 = input("Digite um valor: ")
print("")

if valor1 > valor2:  
    print("O primeiro número é maior!")


elif valor1 < valor2:  
    print("O segundo número é maior!")

else:  
    print("Números iguais!")
