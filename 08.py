# 08. A jornada de trabalho semanal de um funcioná rio é de 40 horas. O funcioná rio que trabalhar mais
# de 40 horas receberá hora extra, cujo cá lculo é o valor da hora regular com um acré scimo de 50%.
# Escreva um algoritmo que leia o nú mero de horas trabalhadas em um mê s, o salá rio por hora e escreva
# o salá rio total do funcioná rio, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
# (considere que o mê s possua 4 semanas exatas).




HorasSemana = 40
HorasMes = 160
HorasExtras = 50
HorasTrabalhadas = float(input("Digite quantas horas trabalhou: "))
ValorHora = float(input("Dgite o valor da sua hora: "))
print("")
if HorasTrabalhadas > HorasMes:
    ValorExtra =(HorasTrabalhadas - HorasMes) * ValorHora * (HorasExtras/100)
    print (f"Você recebrá: R${ValorExtra:.2f} de horas extras")
    print(f"Seu sálario este mes será: R${ValorExtra + (HorasTrabalhadas * ValorHora):.2f}")
else:
    print(f"Seu salário será: R${HorasTrabalhadas * ValorHora:.2f}")
    