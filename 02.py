# 01. Escreva um algoritmo para ler as dimensõ es de um retâ ngulo (base e altura), calcular e escrever a
# á rea do retâ ngulo.
#



dias_por_ano = 365
dias_por_mes = 30
#leia idade em anos#
anos=int(input("Digite sua idade em anos: "))
#meses vividos neste ano#
meses=int(input("Digite quantos meses você já viveu este ano: "))
#dias vividos neste ano#
dias=int(input("Digite quantos dias você já viveu neste mes: "))
#escreva a idade expressa em dias#
idade_em_dias= (anos*dias_por_ano)+(meses*dias_por_mes)+dias
print("")
print("Sua idade expressa em dias é de:",idade_em_dias,"dias")