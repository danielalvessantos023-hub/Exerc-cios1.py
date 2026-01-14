#Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos,
# meses e dias essa pessoa ja viveu. Leve em consideraçã o o ano com 365 dias e o mê s com 30 dias.
# (Ex: 5 anos, 2 meses e 15 dias de vida)
from datetime import date
data_nasc = []

dia = int(input("Digite o dia em que você nasceu: "))
mes = int(input("Digite o mes em que você nasceu: "))
ano = int(input("Digite o ano em que você nasceu: "))
data_nasc.append(dia)
data_nasc.append(mes)
data_nasc.append(ano)

#transformando lista em data#
data_na = date(data_nasc[2], data_nasc[1], data_nasc[0])
#data atual#
data_atual = date.today()
#calculo#
resultado = (data_atual - data_na).days

em_anos = resultado // 365
em_mes = (resultado % 365)% 31
em_dias = em_anos % 365

print(em_anos, em_mes, em_dias)