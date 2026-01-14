# 48. Faça uma calculadora com as seguintes operaçõ es:
# 1 - Soma      5 - Resto da divisã o (extra)
# 2 - Subtração    6 - Potenciaçã o (extra)
# 3 - Multiplicação    7 - Radiciaçã o (desafio)
# 4 - DIVISÃO
while True:
    print(
        "\n####### CALCULADORA #####\n"
          "1. SOMA             5. RESTO DA DIVISÃO\n"
          "2. SUBTRAÇÃO        6. POTENCIAÇÃO\n"
          "3. MULTIPLICAÇÃO    7. RADICIAÇÃO\n"
          "4. DIVISÃO          8. SAIR \n"
    )
    opcao = input("Digite o número da opção desejada: ")


    if opcao == "1":
        print("\n## SOMA ##\n")
        n1 = int(input(""))
        n2= int(input(""))
        print(f"{(n1) + (n2)} ")

    elif opcao == "2":
        print("\n## SUBTRAÇÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) - (n2)} ")
    elif opcao == "3":
        print("\n## MULTPLICAÇÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) * (n2)} ")

    elif opcao == "4":
        print("\n## DIVISÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) / (n2)} ")

    elif opcao == "5":
        print("\n## RESTO DA DIVISÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) % (n2)} ")

    elif opcao == "6":
        print("\n## POTENCIAÇÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) ** (n2)} ")
    elif opcao == "7":
        print("\n## RADICIAÇÃO ##\n")
        n1 = int(input())
        n2 = int(input())
        print(f"Resultado = {(n1) ** (1/n2)} ")

    elif opcao == "8":
        print("## FECHANDO A CALCULADORA ##")
        break
    else:
        print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE")