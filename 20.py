#
# 20. Faça um procedimento que recebe por parâ metro os valores necessá rios para o cá lculo da fó rmula
# de bhá skara e retorna, també m por parâ metro, as suas raı́zes, caso seja possı́vel calcular.

print("Formula de bhaskara é B² - 4*A*C")
a = int(input("Digite um valor para 'A': ")) 
b = int(input("Digite um valor para 'B': "))
c = int(input("Digite um valor para 'C': "))

delta = (b**2) - (4 * a * c)
print(f"Delta = {delta}")

if delta < 0 and a == 0 :
    print("não exite raízes reais ")
elif delta == 0:
    raiz = (-b - delta**0.5) / (2*a)
    print(f"X = {raiz:.2f}")
                 
else:
    raiz1 = (-b - delta**0.5) / (2 * a)
    raiz2 = (-b + delta**0.5) / (2 * a)
    print(f"X1 = {raiz1:.2f} e X2 {raiz2:.2f}")