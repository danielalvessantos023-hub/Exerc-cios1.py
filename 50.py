# Sara tem 1,50m e cresce 2 centı́metros por ano, enquanto Francisco tem 1,10m e cresce 3
# centı́metros por ano. Faça um algoritmo que calcule e imprima na tela em quantos anos serã o
# necessá rios para que Francisco seja maior que Sara.
altura_sara = 1.50
altura_francisco = 1.10

crescimento_sara = 0.02
crescimento_francisco = 0.03

anos = 0

while altura_francisco <= altura_sara:
    altura_sara += crescimento_sara
    altura_francisco += crescimento_francisco
    anos += 1

print(f"Serão necessários {anos} anos para Francisco ser maior que Sara.")