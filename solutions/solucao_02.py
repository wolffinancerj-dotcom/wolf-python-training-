def verificar_senha(senha_digitada):
    senha_correta = "1234"
    return senha_digitada == senha_correta


tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")

    if verificar_senha(senha):
        print("Acesso permitido!")
        break
    else:
        tentativas += 1
        print("Senha incorreta!")

        if tentativas == max_tentativas:
            print("Número máximo de tentativas excedido. Programa encerrado.")