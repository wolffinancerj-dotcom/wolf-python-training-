import os

class Cliente:
    
    def __init__(self,nome,saldo):
        self.nm = nome
        self.saldo = saldo

    def getName(self):
      return self.nm
    
    def getSaldo(self):
      return self.saldo


# -------------------------------------------------------------------------------------

os.system('cls')
listaDeClientes = []
ctrl1 = True

print("-------------- Bem vindo ao sistema de cadastro de cliente! --------------")

while(ctrl1):
  

  nome = input(f"\nInsira o Nome do {len(listaDeClientes)+1}° cliente:\n")
  saldo = float(input(f"\nInsira o saldo de {nome}:\n"))

  listaDeClientes.append(Cliente(nome,saldo))

  ctrl2 = True
  while(ctrl2): 
    continuarLoop = input("Você deseja continuar cadastrando novos clientes? [s/n]\n")
    if(continuarLoop=='s'):
      ctrl2 = False
      os.system('cls')
    elif(continuarLoop=='n'):
      ctrl1=False
      ctrl2=False
      os.system('cls')
    else:
      print("Insira uma resposta válida!\n\n------------------------------\n\n")

#--------------------------------------------------------------------------------------------

print("""LISTA DE CLIENTES - BANCO NACIONAL\n--------------------------\n   NOME    |    SALDO CONTA
--------------------------""")
for i in listaDeClientes:
  print(f"{i.getName()}  |  {i.getSaldo()}")

      

