# 09. Faça um algoritmo para ler: nú mero da conta do cliente, saldo, dé bito e cré dito. Apó s, calcular e
# escrever o saldo atual (saldo atual = saldo - dé bito + cré dito). També m testar se saldo atual for maior
# ou igual a zero escrever a mensagem 'Saldo Positivo', senã o escrever a mensagem 'Saldo Negativo'.



NumeroConta = int(input("Digite o número da sua conta: "))
Saldo = float(input("Digite o Saldo da sua conta: "))
Valor_a_pagar = float(input("Digite Seus débitos á paga: "))
Valor_a_receber = float(input("Digite quanto tem á receber: "))
print("")
Saldo_atual = Saldo - Valor_a_pagar + Valor_a_receber
print(f"R${Saldo_atual:.2f}")


if  Saldo_atual > 0 :
    print(f"Saldo positivo")
elif Saldo_atual < 0 :
    print(f"Seu saldo está negativo")
else:
    print("Saldo zerado")
