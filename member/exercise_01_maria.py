# Quando fiz, pensei que era pra iniciar a lista vazia e o usuário preenche, 
# Então fiz assim para ficar diferente, não sei se pode 
nomes = [] 
saldos = []

notDone = True

print("Entradas:")
print('---')
while notDone:
    nome = input("Insira o nome: ")
    nomes.append(nome)

    saldo = float(input("Insira o saldo: ").replace(',', '.'))
    saldos.append(saldo)

    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar == 'N':
        notDone = False

print("\n\nSaída/Impressão:")
print('---')
print("LISTA DE CLIENTES - BANCO NACIONAL\n")
print('--------------------------')
print("   NOME    |    SALDO CONTA   ")
print('--------------------------')
for i in range(len(nomes)):
    print(f"{nomes[i]} | R${saldos[i]:.2f}")