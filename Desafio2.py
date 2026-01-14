'''Crie uma classe Aluno para um sistema escolar:

Atributos: nome, matricula, notas (lista de notas)
Métodos:
_init_ que recebe nome e matrícula, notas começa vazia
adicionar_nota(nota) - adiciona uma nota (0-10)
calcular_media() - retorna a média das notas
situacao() - retorna "Aprovado" se média ≥ 7, senão "Reprovado"
melhor_nota() - retorna a maior nota'''

class aluno:
    def __init__(self, nome: str , matricula: int , notas:list[float]):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas


    def nota(self):
    
        valor1 = float(input("Digite a nota do 1º Bimestre: "))
        if valor1 < 0 or valor1 > 10 :
            print(f"ERROR: Nota deve estar entre 0 e 10 ")
            return False
        valor2 = float(input("Digite a nota do 2º Bimestre: "))
        if valor2 < 0 or valor2 > 10 :
            print(f"ERROR: Nota deve estar entre 0 e 10 ")
            return False
        valor3 = float(input("Digite a nota do 3º Bimestre: "))
        if valor3 < 0 or valor3 > 10 :
            print(f"ERROR: Nota deve estar entre 0 e 10 ")
            return False
        valor4 = float(input("Digite a nota do 4º Bimestre: "))
        if valor4 < 0 or valor4 > 10 :
            print(f"ERROR: Nota deve estar entre 0 e 10 ")
            return False
        print('')


        self.notas.append(valor1)
        self.notas.append(valor2)
        self.notas.append(valor3)
        self.notas.append(valor4)

    def calculo(self):
        media = sum(self.notas) / len(self.notas)
        print(f"Nota 1º bimestre: {self.notas[0]}\n"
              f"Nota 1º bimestre: {self.notas[1]}\n"
              f"Nota 1º bimestre: {self.notas[2]}\n"
              f"Nota 1º bimestre: {self.notas[3]}\n"
              f"\n"
              f"Maior nota : {max(self.notas)}\n"
              f"Média no ano: {media}")
        if media >= 7 :
            print(f"Média = {media} Você está aprovado")
            return True
        else:
            print(f"Média = {media} Você foi reprovado")
            return False

def main():
    a = aluno(nome = input("Digite o nome do aluno(a): "),
              matricula= int(input("Digte o número da matricula: ")),
              notas = [])
    a.nota()
    a.calculo()


if __name__ == "__main__":
       main()