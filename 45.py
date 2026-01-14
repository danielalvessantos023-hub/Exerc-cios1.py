# . Faça um algoritmo que leia trê s notas obtidas por um aluno, e imprima na tela a mé dia das notas.

not1 = float(input("Digite uma nota: "))
not2 = float(input("Digite uma nota: "))
not3 = float(input("Digite uma nota: "))
lisnot = []
lisnot.append(not1), lisnot.append(not2), lisnot.append(not3)

media = sum(lisnot)/len(lisnot)
print(f"Média = {media:.2f}")