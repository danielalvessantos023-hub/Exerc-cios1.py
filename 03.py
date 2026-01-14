# 03. Escreva um algoritmo para ler o nú mero total de eleitores de um municı́pio, o nú mero de votos
# brancos, nulos e vá lidos. Calcular e escrever o percentual que cada um representa em relaçã o ao total
# de eleitores.
#




#leia o número de votos em blanco#
VotosBlancos=int(input("Digite o número de votos em blanco: "))
#leia o número de votos nulos#
VotosNulos=int(input("Digite o númer de votos nulos: "))
#leia o número de votos válidos#
VotosVálidos=int(input("Digite o nḿero de votos válidos: "))
print("")
#Total de eleitores#
TotalEleitores=VotosBlancos+VotosNulos+VotosVálidos
print("O número total de votos foi de:",TotalEleitores,"votos")
print("")
#percentual de votos em blanco#
print(f"O percentual de votos em blanco foi de:{VotosBlancos/TotalEleitores:.2%}")
print("")
#percentual de votos nulos#
print(f"O percentual de votos nulos foi de: {VotosNulos/TotalEleitores:.2%}")
print("")
#percentual de votos válidos#
print(f"O percentual de votos válidos foi de: {VotosVálidos/TotalEleitores:.2%}")