#
# Faça um algoritmo que efetue o cá lculo do salá rio lı́quido de um professor. As informaçõ es
# fornecidas serã o: valor da hora aula, nú mero de aulas lecionadas no mê s e percentual de desconto do
# INSS. Imprima na tela o salá rio lı́quido final.


valor_hora_aula = float(input("Digite o valor da sua hora aula: "))
numero_de_aula_mes = float(input("Digite quantas aula você lecionou no mes: "))
desconto_inss = [7.5, 9, 12, 14]
salbruto = valor_hora_aula * numero_de_aula_mes
print("")
print(f"Seu salário bruto = R${salbruto}")


if salbruto <= 1518:
    print(f"Desconto insss = R${salbruto * (desconto_inss[0]/100):.2f}")
    print(f"Seu líquido = R${salbruto * (1-desconto_inss[0]/100):.2f}")

elif salbruto > 1518 and salbruto <= 2793.88:
    print(f"Desconto insss = R${salbruto * (desconto_inss[1]/100):.2f}")
    print(f"Seu líquido é R${salbruto * (1 - desconto_inss[1]/100):.2f}")

elif salbruto > 1793.88 and salbruto <= 4190.83 :
    print(f"Desconto insss = R${salbruto * (desconto_inss[2]/100):.2f}")
    print(f"Seu líquido = R${salbruto * (1 - desconto_inss[2]/100):.2f}")
    
else: 
    print(f"Desconto insss = R${salbruto * (desconto_inss[3]/100):.2f}")
    print(f"Seu líquido = R${salbruto * (1 -desconto_inss[3]/100):.2f}")