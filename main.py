# print("Hello world")

# produto1 = 5
# produto2 = 500
# produto3 = 50

# print(produto1 + produto2 + produto3)

aluguel = 1000
mercado = 500
carro = 400
amigos = 6

total = aluguel + mercado + carro

carro = carro * 2
total = aluguel + mercado + carro
total_pessoa = total / amigos
# print(total_pessoa)

# print(type(aluguel))
# texto = " Fabricio CARRaro da alura "
# print(texto.upper())
# print(texto.lower())
# print(texto.strip())
# print(texto.replace("  ", " "))
# print(texto.upper().strip().replace("  ", " "))

# nome = input("digite seu nome: ")
# idade = int(input("digite sua idade: "))

# if nome == "carlos":
#     print("seja bem vindo")
# type(idade)
# int(idade)

# print(f"o {nome} tem {idade} de idade")

# if idade >= 18:
#     print (f"{nome} pode entrar na festa, é maior de idade")
# else:
#     print(f"{nome} não pode entrar na festa, é menor de idade")


# media = float(input("Digite a sua média: "))

# if media < 5.0:
#     print("Reprovado!")
# elif media >= 5.0 and media < 7.0:
#     print("Recuperação")
# else:
#     print("Aprovado!")

# INTELIGENCIA ARTIFICIAL

# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()

# #CONFIGURAR CHAVE DA API

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# #CRIA MODELO

# model = genai.GenerativeModel("gemini-2.5-flash")

# #CRIA CHAT

# model.start_chat()

# #INTERAGIR COM O CHAT

# pergunta = input("Digite sua pergunta: ")
# # response = model.generate_content(pergunta)
# # print(response.text)
# # resposta = chat.send_message(pergunta)

# while pergunta.lower() != "fim":
#     response = model.generate_content(pergunta)
#     print(response.text)
#     print("\n")
#     pergunta = input("Digite sua pergunta: ")

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]

for i in lista_de_medias:
    if i > 9:
        print(i)
        break
    else:
        nota = i + 1
        lista_de_medias[lista_de_medias.index(i)] = nota
        print(nota)
