'''
Crie um programa em Python que simule um sistema simples de verificação de senha.
O sistema deve seguir as seguintes regras:

   1. Existe uma senha cadastrada no sistema.

   2. O usuário deve digitar uma senha para tentar acessar o sistema.

   3. O programa deve possuir uma função chamada verificar_senha que recebe:
      - a senha digitada pelo usuário
      - a senha correta do sistema
   
   Essa função deve retornar True se as senhas forem iguais e False caso contrário.

   4. O usuário terá no máximo 3 tentativas para acertar a senha.

   5. Regras de funcionamento:
    - Se o usuário acertar a senha, o programa deve mostrar a mensagem:
          Você entrou!
    - Se errar, o programa deve informar quantas tentativas restantes ainda possui.
    - Se o usuário errar 3 vezes, o sistema deve mostrar:
         Acesso bloqueado.
'''
