'''Crie uma classe Produto para uma loja:

Atributos: nome, preco, quantidade_estoque
Métodos:
_init_ para inicializar
comprar(quantidade) que reduz o estoque se houver suficiente
repor(quantidade) que aumenta o estoque
valor_total_estoque() que calcula preço × quantidade
_str_ para mostrar: "Produto: NOME (R$ PREÇO)"'''


class Produto:
    def __init__(self, nome: str = "Feijão" , preco: float = 6.5, estoque: int = 0, ):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.valor_repo = self.preco * 0.7


    def venda (self, quantidade: int):
        if quantidade <= 0:
            print("ERROR: Quatidade menor ou igual a 0 não é permitido! ")
            return False

        if quantidade > self.estoque :
            print("Estoque insuficiente.")
            print(f"Estoque disponível: {self.estoque}")
            return False

        self.estoque -= quantidade
        valor_total = quantidade * self.preco

        print(f"Venda realizada com sucesso:\n "
              f"Quantidade: {quantidade} \n "
              f"Valor unitário : {self.preco} \n "
              f"Valor total : {valor_total} \n "
              f"Estoque restante : {self.estoque}")
        return True

    def repor (self, quantidade: int):
        if quantidade <= 0 :
            print(f"ERROR: Nenhuma quantidade adicionada !")
            return False

        estoque_anterior = self.estoque
        self.estoque += quantidade
        Valor_compra = quantidade * self.preco
        print(f"REPOSIÇÃO REALIZADA COM SUCESSO:\n"
              f"Quantidade comprada = {quantidade}\n "
              f"Valor gasto = {Valor_compra}\n"
              f"Estoque anterior = {estoque_anterior}\n"
              f"Novo estoque = {self.estoque}")
        return  True

    def verificar_estoque(self):
        print(f"STATUS ATUAL DO ESTOQUE:\n"
                f"Produto: {self.nome}\n"
                f"Quantidade em estoque: {self.estoque}\n"
                f"Preço unitário: {self.preco}\n"
                f"Valor total do estoque: {self.estoque * self.preco} "
                )

    def menu(self):
        while True:
            print(
                "\nMENU:\n"
                "1. Realizar venda\n"
                "2. Repor estoque\n"
                "3. Ver estoque\n"
                "4. Sair"
            )

            opcao = input("Escolha uma opção (1-4): ").strip()

            if opcao == '1':
                qtd = int(input("Quantidade de saída: "))
                self.venda(qtd)

            elif opcao == '2':
                qtd = int(input("Quantidade de entrada: "))
                self.repor(qtd)

            elif opcao == '3':
                self.verificar_estoque()

            elif opcao == '4':
                print("Sistema encerrado.")
                break

            else:
                print("OPÇÃO INVÁLIDA")

def main():
    p = Produto('Feijão', 6.5, 0  )
    p.menu()
if __name__=="__main__":
    main()


