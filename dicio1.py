# https://academiahopper.com.br/dicionarios-em-python/

comando = "continue"
contatos = {}

while comando != "sair": 
  comando = input("Digite o comando: (novo, pes, sair):")

if comando == "novo":
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    contatos[nome] = {
      "nome": nome,
      "telefone": telefone,
      "email": email
    }

if comando == "pes":
	nome = input("Nome: ").lower()
    if nome in contato:
    	contato = contatos[nome]
    	print(contato)
    else:
    	print("Não encontrado")
