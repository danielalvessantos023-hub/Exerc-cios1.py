# 18. Faça uma funçã o que verifique se um valor é perfeito ou nã o. Um valor é dito perfeito quando ele é
# igual a soma dos seus divisores exceto ele pró prio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que sã o seus
# divisores). A funçã o deve retornar um valor booleano.


n = int(input("Digite um número: "))
def perfeito(n):
    if n <= 1:
        return False
soma_div = 0
for i in range (1, n):
     if n % i == 0:
        soma_div += i
       
if soma_div == n :
    print(f"{n} É uma número perfeito")
else:
    print(f"{n} Não é um número perfeito")
print(f"a soma dos divisores de {n} é igual a {soma_div}")

