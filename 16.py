# 16. Faça uma funçã o que recebe a mé dia final de um aluno por parâ metro e retorna o seu conceito,
# conforme a tabela abaixo:
# 0,0 a 4,9(D)
# 5,0 a 6,9(C)
# 7,0 a 8,9(B)
# 9,0 a 10,0(A)


notas = []
for i in range (4):
    nota = float(input(f"Digites sua nota do {i + 1}º bimestre:"))
    notas.append(nota)

media = sum(notas)/4
print(f"{media:.2f}")
print('')

if float(media) >= float(0.0) and float(media) <= float(4.9):
    print("D")
    print("Que pena você reprovou!")
    
elif float(media) >= float(5.0) and float(media) <= float(6.9):
    print("C")
    print("Foi por pouco hein!")

elif float(media) >= float(7.0) and float(media) <= float(8.9):
    print("B")
    print("Boa pequeno(a) gafanhoto!")

else:  
    print("A")
    print("Excelente garoto(a) prodígio!")