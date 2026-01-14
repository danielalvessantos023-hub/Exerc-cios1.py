#14. Faça um algoritmo para ler um nú mero que é um có digo de usuá rio. Caso este có digo seja diferente
# de um có digo armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a
# mensagem ‘Usuá rio invá lido!’. Caso o Có digo seja correto, deve ser lido outro valor que é a senha. Se
# esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a
# senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’


user = 1234
password = 9999

while True:
    usuario = int(input("Digite seu usário com 4 dgitos: "))
    if user != usuario:
       print("Usuário inválido, tente novamente")
    else:
        break
while True:
    import getpass
    senha = int(getpass.getpass("Digite sua senha com 4 digitos: "))
    if password != senha :
        print("Senha inválida")
    else:
        print("Acesso liberado")
        break