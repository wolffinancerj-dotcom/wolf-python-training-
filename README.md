# Wolf Finance – Python Training 🐺

Este repositório foi criado para que os membros da **Wolf Finance** pratiquem Python enquanto aprendem a usar **Git e GitHub em projetos colaborativos**.

O objetivo é que todos aprendam o fluxo real utilizado em projetos de tecnologia e dados:

* versionamento de código com Git
* trabalho com branches
* commits organizados
* envio de Pull Requests (PR)
* revisão de código

Essas habilidades são essenciais em qualquer projeto profissional.

 

# Estrutura do Repositório

```
wolf-python-training
│
├── exercises/
│   └── src/
│        └── petr4.csv
│        └── btc.csv
│   └── exercise_01.py
|
├── member/
│   └── exercise_01_matheus.py
|
├── solutions/
│   └── solution_01.py
└── README.md
```

**exercises/**
Contém os exercícios que devem ser resolvidos.

**solutions/**
Cada membro deve enviar sua solução nesta pasta.

 

# Fluxo de Contribuição

Todos os membros devem seguir este fluxo.

 

# 1. Fazer Fork do Repositório

Clique em **Fork** no canto superior direito da página do repositório.

Isso criará uma cópia do repositório na sua conta do GitHub.

 

# 2. Clonar o Repositório

No seu computador, rode:

```
git clone https://github.com/SEU-USUARIO/wolf-python-training.git
```

Entre na pasta do projeto:

```
cd wolf-python-training
```

 

# 3. Criar uma Branch

Nunca trabalhe diretamente na branch **main**.

Crie uma branch com seu nome:

```
git checkout -b solution-seu-nome
```

Exemplo:

```
git checkout -b solution-matheus
```

 

# 4. Resolver o Exercício

Abra o notebook localizado em:

```
exercises/exercise_01.py
```

Resolva o exercício e salve sua solução na pasta:

```
solutions/
```

Exemplo:

```
solutions/exercise_01_matheus.py
```

 

# 5. Fazer Commit das Alterações

```
git add .
git commit -m "solution exercise 01 - seu nome"
```

 

# 6. Enviar para o GitHub

```
git push origin solution-seu-nome-da-sua-branch
```

 

# 7. Criar Pull Request

No GitHub aparecerá o botão:

**Compare & Pull Request**

Clique nele para criar o Pull Request.

Use o seguinte formato:

**Título**

```
Solution Exercise 01 - Seu Nome
```

**Descrição**

```
Nome: Seu nome
Exercício: Exercise 01
Descrição: Implementação da solução proposta
```

 

# Revisão de Código

O líder do projeto irá revisar o Pull Request.

Possíveis resultados:

✔ aprovado → o código é integrado ao repositório
✏ pedido de alterações → você deve ajustar o código e atualizar o PR

 

# Regras Importantes

* Não editar arquivos diretamente na **main**
* Sempre trabalhar em uma **branch**
* Cada membro deve enviar **sua própria solução**
* Todo envio deve ser feito via **Pull Request**

 

# Objetivo do Projeto

Além de aprender Python, este projeto tem como objetivo ensinar práticas utilizadas em projetos reais de tecnologia e dados:

* colaboração em equipe
* versionamento de código
* revisão de código
* organização de projetos

Essas práticas são usadas diariamente em empresas de tecnologia, bancos e fundos quantitativos.

 

🐺 **Wolf Finance**
Liga de Investimentos – CEFET/RJ
