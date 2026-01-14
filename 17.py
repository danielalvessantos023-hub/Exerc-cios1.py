# 17. Faça uma funçã o que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade
# expressa em dias.

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

print('')
print('')
print(f"A sua idade expressa em dias, na data hoje {data_atual.strftime('%d/%m/%Y')}, é de: {resultado}")
print('')
print('')

