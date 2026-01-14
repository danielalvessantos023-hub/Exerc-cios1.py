# #(Crie uma classe Contato para uma agenda:
#
# #Atributos: nome, telefone, email
# Métodos:
# _init_ para inicializar
# alterar_telefone(novo_telefone)
# alterar_email(novo_email)
# exibir() que mostra todos os dados formatados
# _str_ que retorna apenas nome e telefone#



class Contato:
    def __init__(self):
        self.agenda = []

    def adicionar (self, nome: str, telefone , email: str):
        contato =   {
            "Nome": nome,
            "Telefone": telefone,
            "E-mail":email
        }

        self.agenda.append(contato)
        print("\n #### CONTATO ARMAZENADO COM SUCESSO ####\n ")

    def cadastro (self):
            while True:
                print("######### CADASTRO CONTATO ############")
                nome = input("Nome: ")
                telefone = int(input("Telefone: "))
                email = input("E-mail: ")

                self.adicionar(nome, telefone, email)

                while True:
                    continuar = input("\nDeseja adicionar outro contato? (S/N): ").strip().lower()

                    if continuar == "s":
                        break  # sai do loop interno e volta ao cadastro#

                    elif continuar == "n":
                        return  # encerra o método completamente #

                    else:
                        print("Opção inválida. Digite apenas S ou N.")
                        continue

    def listar_contatos(self):
        if not self.agenda:
            print("\n #### NENHUM CONTATO REGISTRADO ######")

        else:
            for contato in self.agenda:
                print(f"\nNome: {contato['Nome']}\n"
                      f"Telefone: {contato['Telefone']}\n"
                      f"E-mail: {contato['E-mail']}\n")



    def alterar_contato(self,):
        print("######### ALTERA CONTATO ############\n"
              "########## LISTA DE CONTATOS ########")

        if not self.agenda:
            print("\n #### NENHUM CONTATO REGISTRADO ######\n"
                    " ######## RETORNANDO AO MENU #########")
            return
        for i, contato in enumerate(self.agenda, start=1):
            print(f"{i} - {contato['Nome']}")

        indice = int(input("\nEscolha a opção  do contato que deseja alterar neste contato: ")) - 1
        if indice < 0 or indice > len(self.agenda):
            print("Contato inválido")
            return
        print("1 - Nome")
        print("2 - Telefone")
        print("3 - Email")

        campo = input("\nO que deseja alterar? ")

        if campo == "1":
            print(f"Antigo nome = {self.agenda[indice]['Nome']}")
            novo = input("Novo Nome: ")
            self.agenda[indice]['Nome'] = novo
            print(f"Novo Nome armazenado: {novo}")
        elif campo == "2":
            print(f"Antigo Telefone = {self.agenda[indice]['Telefone']}")
            novo = input("Novo Telefone: ")
            self.agenda[indice]['Telefone'] = novo
            print(f"Novo Telefone armazenado: {novo}")


        elif campo == "3":
            print(f"Antigo E-mail = {self.agenda[indice]['E-mail']}")
            novo = input("Novo E-mail: ")
            self.agenda[indice]['E-mail'] = novo
            print(f"Novo E-mail armazenado: {novo}")



    def menu (self):
        while True:
            print("\n #########################\n"
                    " ########## MENU #########\n"
                    " #########################\n"
                  "\n1. Adicionar contato \n"
                  "2. Alterar contato \n"
                  "3. consultar agenda \n"
                  "4. Sair ")

            opcao = input("\nDigite o número da opção desejada: ")

            if opcao == "1" :
                self.cadastro()

            elif opcao == "2":
                self.alterar_contato()

            elif opcao == "3" :
                self.listar_contatos()

            elif opcao == "4" :
                while True:
                    sair = input("Deseja sair do programa ? (S/N): ").strip().lower()
                    if sair == "s":
                        print("\nSaindo so programa\n")
                        return

                    elif sair == "n" :
                        print("\nRetornando\n")
                        break

                    else:
                        print("\n OPÇÃO INVÁLIDA \n")
                        continue

            else:
                print("########### OPÇÃO INVÁLIDA ############\n"
                      "########### TENTE NOVAMENTE ###########")
                continue



def main():
    agenda = Contato()
    agenda.menu()
if __name__ == "__main__":
    main()

