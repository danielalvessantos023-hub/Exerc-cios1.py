# 13. Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades
# dos homens serã o sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma
# das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais
# novo com a mulher mais velha


H1 = int(input("Digite a idade do primeiro homem: "))
H2 = int(input("Digite a idade do segundo homem: "))
print('')


M1 = int(input("Digite a idade da primeira mulher: "))
M2 = int(input("Digite a idade da segunda mulher: "))
print("")

if H1 > H2 and M1 > M2:
    soma1 = int(H1) + int(M2)
    print("A soma da idade o homem mais velho com a mulher mais nova é:",soma1,"anos")

if H1 > H2 and M1 < M2:
    soma2 = int(H1) + int(M1)
    print("A soma da idade o homem mais velho com a mulher mais nova é:",soma2,"anos")

if H1 < H2 and M1 > M2:
    soma3 = int(H2) + int(M2)
    print("A soma da idade o homem mais velho com a mulher mais nova é:",soma3,"anos")
    
if H1 < H2 and M1 < M2:
    soma4 = int(H2) + int(M1)
    print("A soma da idade o homem mais velho com a mulher mais nova é:",soma4,"anos")
print("")
#e o produto da idade do homem mais novo com a mulher mais velha#
if H1 > H2 and M1 > M2:
    produto1 = int(H2) * int(M1)
    print("O produto da idade o homem mais novo com a mulher mais valha é:",produto1,"anos")

if H1 > H2 and M1 < M2:
    produto2 = int(H2) * int(M2)
    print("O produto da idade o homem mais novo com a mulher mais velha é:",produto2,"anos")
    

if H1 < H2 and M1 > M2:
    produto3 = int(H1) * int(M1)
    print("O produto da idade o homem mais novo com a mulher mais velha é:",produto3,"anos")

if H1 < H2 and M1 < M2:
    produto4 = int(H1) * int(M2)
    print("O produto da idade o homem mais novo com a mulher mais velha é:",produto4,"anos")

else:
    print("Idades inválidas")

#Método curto:# 


#leia a idade diferente de 2 homens #
# Idade homens#
H1 = int(input("Digite a idade do primeiro homem: "))
H2 = int(input("Digite a idade do segundo homem: "))
#leia a idade diferentre de 2 mulheres#
#Idade mulher#
M1 = int(input("Digite a idade da primeira mulher: "))
M2 = int(input("Digite a idade da segunda mulher: "))
print("")
#calcule a soma da idade do homem mais velho com a mulher mais nova#
if H1 == H2:
    print("Idades inválidas")

elif M1 == M2:
       print("Idades inválidas")
      
else: 
    soma = max (H1, H2) + min (M1, M2)
    produto = min (H1, H2) * max (M1, M2)

    print("A soma da idade o homem mais velho com a mulher mais nova é:",soma,"anos")
    print("")
    print("O produto da idade o homem mais novo com a mulher mais valha é:",produto,"anos")
