#Uma fruteira está vendendo frutas com a seguinte tabela de preços:Morango - Até 5 Kg,R$ 2,50
# por Kg - Acima de 5 Kg,R$ 2,20 por Kg Maçã - Até 5 Kg,R$ 1,80 por Kg - Acima de 5 Kg,R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10
# % sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva
# o valor a ser pago pelo cliente.maça_ate_5kg = 1.8

maça_acima_5kg = 1.5
morango_ate_5kg = 2.5
morango_acima_5kg = 2.2
desconto = 10

produto = input("Digite o produto comprado: ")
quantidade = float(input("Digita o peso do produto: "))
print("")

if produto == "maça" and quantidade <= 5 :
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${quantidade * maça_ate_5kg:.2f}")

elif produto == "maça" and quantidade > 5 and quantidade < 8:
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${quantidade * maça_acima_5kg:.2f}")

elif produto == "maça" and quantidade > 8:
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${(quantidade * maça_acima_5kg) / (1 + desconto/100):.2f}")
    
elif produto == "morango " and quantidade <= 5 :    
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${quantidade * morango_ate_5kg:.2f}")

elif produto == "morango" and quantidade > 5 and quantidade <= 8 :
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${quantidade * morango_acima_5kg:.2f}")
    
elif produto == "morango" and quantidade > 8:
    print(f"Produto: {produto}  Peso: {quantidade}  Preço: R${(quantidade * morango_acima_5kg) / (1 + desconto/100):.2f}")

    


 

