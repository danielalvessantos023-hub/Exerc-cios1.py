# Faça um algoritmo que leia trê s valores que representam os trê s lados de um triâ ngulo e verifique
# se sã o vá lidos, determine se o triâ ngulo é : equilá tero, isó sceles ou escaleno.

lado_a = int(input("Digite um valor para o lado A: "))
lado_b = int(input("Digite um valor para o lado B: "))
lado_c = int(input("Digite um valor para o lado C: "))

if lado_a + lado_b == lado_c or lado_c + lado_b == lado_a or lado_a + lado_c == lado_b:
    print("Valores inválidos tente novamente ")

elif lado_b != lado_a and lado_a != lado_c:
    print("Triangulo escaleno")

elif lado_b == lado_a and lado_b != lado_c or lado_a == lado_c and lado_a != lado_b : 
    print("Triagulo isósceles")

else: 
    print("Triangulo equilátero")