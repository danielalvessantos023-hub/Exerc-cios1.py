# Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme
# a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser
# pago. Utilize os có digos da tabela de condiçõ es de pagamento para efetuar o cá lculo adequado.
# Tabela de Có digo de Condiçõ es de Pagamento
# 1 - A` Vista em Dinheiro ou Pix, recebe 15% de desconto
# 2 - A` Vista no cartã o de cré dito, recebe 10% de desconto
# 3 - Parcelado no cartã o em duas vezes, preço normal do produto sem juros
# 4 - Parcelado no cartã o em trê s vezes ou mais, preço normal do produto mais juros de 10%


valor = float(input("Digite o valor do produto: "))
print("")

print ("Escolha a forma de pagamento: ")
print ("1 - A Vista em Dinheiro ou Pix, recebe 15% de desconto")
print ("2 - A Vista no cartão de crédito, recebe 10% de desconto" )
print ("3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros" )
print ("4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%")
print("")



while True:
    opcão = int(input("Digite uma opção de pagamentos: "))
    print("")
    if opcão == 1 :
        preço_final = valor * 0.85
        print(f"Preço final do produto: R${preço_final:.2f}")
        break
    
    elif opcão == 2:
        preço_final = valor * 0.9           
        print(f"Preço final do produto: R${preço_final:.2f}")
        break
    
    elif opcão == 3:
        preço_final = valor 
        print(f"Preço final do produto: R${preço_final:.2f}")
        break
    
    elif opcão == 4:
        preço_final = valor * 1.1
        print(f"Preço final do produto: R${preço_final:.2f}")
        break

    else:
        print("Dados inválidos, escolha outra opcão de pagamento")
        print("")
     
    