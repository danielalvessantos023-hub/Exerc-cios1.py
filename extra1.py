# Verificador de Número Primo
# Objetivo: Determinar se um número inteiro positivo é primo.
# Lógica envolvida:
# •	Verificar divisibilidade de 2 até √n.
# •	Tratar casos especiais (0,1, 2, números negativos).
# •	Contar divisores — se apenas 1 e ele mesmo ⇒ primo.

n = int(input("digite um numero : "))

def primo (n):
    if n == 2 or n == 3:
        return True

    elif n <= 1:
        return False
    
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    cond = 3
    while cond < n**0.5 :
        cond += 2
    if n % cond == 0:
        return False
    else: 
        return True

  
if primo(n):
    print(f"O número {n} é um número primo")
else:
    print(F"O número {n} não é um número primo")   
    
            
  