# 10. Ler 3 valores e escrever o maior deles


valor1 = input("Digite um valor: ")
valor2 = input("Digite um valor: ")
valor3 = input("Digite um valor: ")
MaiorValor = max(valor1, valor2, valor3)
print("")
   
if valor1 > (valor2 and valor3):
    print("O maior valor é:",valor1)

elif valor2 > (valor1 and valor3):
    print("O maior valor é:",valor2)

elif valor3 > (valor1 and valor2):
    print("O maior valor é:",valor3)

else:
    print("Valores inválidos")