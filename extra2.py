# Conversão de Número para Romano (até 3999)
# Objetivo: Converter um número inteiro em algarismos romanos.
# 3500//1000=3
# Lógica envolvida:
# •	Subtração sequencial usando valores padrão (1000, 900, 500, 400…).
# •	Uso de repetição com while ou for.
# •	Ordem importa (ex: 4 = IV, não IIII).

def romano (n):
    
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos= ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL','X', 'IX', 'V', 'IV', 'I']
    

    if n <= 0 or n >= 4000 :
        return "Valor fora do intervalo suportado "
    
    resultado = ""
    i = 0
    
    while n > 0:
        if n >= valores[i]:
            resultado += simbolos[i] 
            n -= valores [i]
        else:
            i += 1
    
    return resultado
def main ():
    try:
        n = int(input("digite um valor: "))
        r  = romano (n)
        print (f"O numero {n} em algarismo romano é: {r}")
    except ValueError:
       print("")
if __name__ == "__main__":
    main()