# 19. Faça um procedimento que recebe a idade de um nadador por parâ metro e retorna, també m por
# parâ metro, a categoria desse nadador de acordo com a tabela abaixo:
# -5 a 7 anosInfantil A
# -8 a 10 anosInfantil B
# -11-13 anosJuvenil A
# -14-17 anosJuvenil B
# -Maiores de 18 anos Adulto
from datetime import datetime
from dateutil.relativedelta import relativedelta

ano_atual = datetime.today().year
data_nasc = []
while True:
    ano = int(input("Digite o ano em que vc nasceu com 4 digitos: "))
    if len(str(ano)) != 4:
        print("Dados inválidos, tente novamente")
    elif ano > ano_atual:
        print("Ainda não chegamos ai, tente novamente")
    else:
        break


while True:
    mes = int(input("Digite o mes em que você nasceu com 2 digitos: "))
    if len(str(mes)) != 2 :
        print("Dados inválidos, tente novamente: ")
    elif mes > 12 :
        print("O ano so tem 12 meses, tente novamente ")
    else:
        break


while True: 
    dia = int(input("Digite o dia em você nasceu com 2 digitos: "))
    if len(str(dia)) < 2 or len(str(dia)) > 2:
        print("Dados inválidos, tente novamente ")
    elif dia > 31 :
        print("Seu mes tem mais dias do que os outros, tente novamente ")
    else:
        break
print("")
data_nasc.append (ano)
data_nasc.append (mes)
data_nasc.append (dia)

data_atual= datetime.today().date()
nasc = datetime(data_nasc[0], data_nasc[1], data_nasc[2])
idade = relativedelta(data_atual, nasc).years 

if idade < 5 :
    print("Você não tem idade sulficiente para nadar ")
elif idade >= 5  and idade <= 7:
    print(f"Você tem {idade} anos e se encaixa na categoria Infantil A ")
elif idade >=8 and idade <= 10 :
    print(f"Você tem {idade} anos e se encaixa na categoria Infantil B ")
elif idade >=11 and idade <= 13:
    print(f"Você tem {idade} anos e se encaixa na categoria Juvenil A ")
elif idade >13 and idade <= 17:
    print(f"Você tem {idade} anos e se encaixa na categoria Junevil B ")
else:
    print(f"Você tem {idade} anos e se encaixa na categoria Adulto ")

