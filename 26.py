# 26. Um posto está vendendo combustı́veis com a seguinte tabela de descontos:
# A' lcool:
# - até 20 litros,desconto de 3% por litro
# - acima de 20 litros,desconto de 4% por litro
# Gasolina:
# - até 20 litros, desconto de 6% por litro
# - acima de 20 litros, desconto de 5% por litro
#

gaso = 3.3
alcool = 2.9
alcool_ate_20 = 3
alcool_mais_20 = 4
gasolina_ate_20 = 6
gasolina_mais_20 = 5

quantidade = float(input("Digite a quantidade de combustível: "))
combustivel = input("digite qual combustível foi abastecido: ")

while True: 
    if combustivel == "gasolina" and quantidade <= 20 :
        print(f"preço sem desconto: R${quantidade*gaso:.2f}")
        print(f"preço com desconto: R${(quantidade*gaso) / (1 +  gasolina_ate_20/100):.2f}")
    elif combustivel == "gasolina" and quantidade > 20: 
        print(f"preço sem desconto: R${quantidade*gaso:.2f}")
        print(f"preço com desconto: R${(quantidade*gaso) / (1 +  gasolina_mais_20/100):.2f}")
    elif combustivel == "alcool" and quantidade <= 20 :
        print(f"preço sem desconto: R${quantidade*alcool:.2f}")
        print(f"preço com desconto: R${(quantidade*alcool) / (1 +  alcool_ate_20/100):.2f}")
    elif combustivel == "alcool" and quantidade > 20 :
        print(f"preço dem desconto: R$ {(quantidade * alcool)}")
        print(f"preço com desconto: R${(quantidade*alcool) / (1 +  alcool_mais_20/100):.2f}")
        
    break
    
    