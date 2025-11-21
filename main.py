# print("Hello world")

# produto1 = 5
# produto2 = 500
# produto3 = 50

# print(produto1 + produto2 + produto3)

# aluguel = 1000
# mercado = 500
# carro = 400
# amigos = 6

# total = aluguel + mercado + carro

# carro = carro * 2
# total = aluguel + mercado + carro
# total_pessoa = total / amigos
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
# response = model.generate_content(pergunta)
# print(response.text)
# resposta = chat.send_message(pergunta)

# while pergunta.lower() != "fim":
#     response = model.generate_content(pergunta)
#     print(response.text)
#     print("\n")
#     pergunta = input("Digite sua pergunta: ")

# lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
# lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]

# lista_de_medias[0] #PRIMEIRO ELEMENTO
# lista_de_medias[len(lista_de_medias) - 1] #ULTIMO ELEMENTO
# lista_de_medias[- 1] #ULTIMO ELEMENTO
# lista_de_medias[- 2] #PENULTIMO ELEMENTO

# lista_de_medias[1:] #SEGUNDO ELEMENTO ATÉ O FINAL
# lista_de_medias[1:3] #SEGUNDO ELEMENTO ATÉ O SEGUNDO - A SEGUNDA INFORMAÇÃO NÃO ENTRA
# lista_de_medias[:3] #PRIMEIRO ELEMENTO ATÉ O ELEMENTO 2 - A SEGUNDA INFORMAÇÃO NÃO ENTRA

# tamanho_da_lista = len(lista_de_medias)

# for i in lista_de_medias:
#     if i > 9:
#         lista_de_medias[lista_de_medias.index(i)] = 10.0
#         break
#     else:
#         nota = i + 1
#         lista_de_medias[lista_de_medias.index(i)] = nota

# print(lista_de_medias)

# lista_de_nomes.append("Carlos Maciel") #INCLUI APENAS 1 VALOR COM O APPEND
# lista_de_nomes.extend(["Joao Branco", "Antonio Carlos"]) #INCLUI QUANTOS VALORES FOREM NECESSÁRIOS - PRECISA ESTAR ENTRE COLCHETES
# print(lista_de_nomes)

# lista_de_nomes.remove("Joao Branco") #REMOVE COM BASE NO VALOR - O PRIMEIRO QUE ENCONTRAR
# print(lista_de_nomes)

# lista_de_nomes.pop(2) #REMOVE COM BASE NO INDICE
# print(lista_de_nomes)


#DICIONARIOS

# dicionario_nome_media = {"Maria Silva":8.9, 
#                          "João Santos":7.5, 
#                          "Ana Oliveira":4.2, 
#                          "Pedro Costa":1.4, 
#                          "Juliana Pereira":9.5
#                         }

# dicionario_nome_media["Maria Silva"] #BUSCA O VALOR CONFORME O DADO PASSADO
# dicionario_nome_media.get("Maria Silva") #OUTRA FORMA DE BUSCAR VALOR
# dicionario_nome_media.pop("Maria Silva") #REMOVE O VALOR DO VALOR PASSADO

# dicionario_nome_media.itens() #MOSTRA TODAS AS CHAVES COM SEUS VALORES
# dicionario_nome_media.keys() #MOSTRA APENAS AS CHAVES
# dicionario_nome_media.values() #MOSTRA APENAS OS VALORES


#DESAFIO DICIONARIO
#nome e media como chaves
#uma lista de dicionarios

# dicionario_desafio = [
#     {"nome": "Carlos Maciel", "media": 8.9},
#     {"nome": "Joao Paulo", "media": 5.0},
#     {"nome": "Ana Pereira", "media": 7.2},
# ]

# print(dicionario_desafio[0]) #TRAZ TODAS AS INFORMAÇÕES DO INDICE
# print(dicionario_desafio[0]["nome"]) #TRAZ APENAS O VALOR DA CHAVE NOME, NO INDICE SOLICITADO


# nomes = ['Maria', 'João', 'Ana', 'Pedro', 'Juliana']

# print(nomes[-1])  # Exibe 'Juliana'
# print(nomes[-2])  # Exibe 'Pedro'

# # Exemplo de slicing com índice negativo
# ultimos_tres = nomes[-3:]
# print(ultimos_tres)  # Exibe ['Ana', 'Pedro', 'Juliana']


#LOOPs - FORMAS PARA UTILIZAR

# dicionario_desafio = [
#     {"nome": "Carlos Maciel", "media": 8.9},
#     {"nome": "Joao Paulo", "media": 5.0},
#     {"nome": "Ana Pereira", "media": 7.2},
# ]

# n = 0

# while n < len(dicionario_desafio):
#     print(dicionario_desafio[n])

#     n += 1


# for i in dicionario_desafio:
#     print(i)


# for n in range(5): de 1 a 5
#     print(n)


# for n in range(2,7): de 2 a 6
#     print(n)


# for n in range(2, 7, 2): de 2 a 6 pulando de 2 em 2
#     print(n)


# pessoa = {
#     "nome": "Carlos Maciel",
#     "idade": 30,
#     "altura": 1.79,
# }

# for chave, valor in pessoa.items():
#     print(f"a chave {chave} possui o valo de {valor}")


# for n in range(11):
#     if n % 2 == 0:
#         print(n)


#FUNÇÕES

# texto1 = "Carlos aUGUsto maCIel"
# texto2 = "  carlos AugUsto maCIel"
# texto3 = "carlos    aUGUsto maCIel"
# texto4 = "Carlos aUGUsto    maCIEL"

# def ajusta_texto(texto):
#     texto_novo = texto.upper()
#     lista = texto_novo.split()
#     nome_pronto = " ".join(lista)
#     return nome_pronto

# def ajusta_texto(texto):
#     print(" ".join(texto.upper().split()))

# ajusta_texto(texto1)

# import random

# salas_de_aula = ["Sala 1", "Sala 2", "Sala 3", "Sala 4", "Sala 5"]

# def aloca_alunos_salas(nome_aluno, lista_sala):
#     sala_aluno = random.choice(lista_sala)
#     nome_aluno = ajusta_texto(nome_aluno)

#     dicionario_aluno = {
#         "nome:": nome_aluno,
#         "sala": sala_aluno,
#     }
#     print(dicionario_aluno)

# aloca_alunos_salas(texto1, salas_de_aula)


import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

#CONFIGURAR CHAVE DA API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#CRIA MODELO
model = genai.GenerativeModel("gemini-2.5-flash")

#CRIA CHAT
model.start_chat()

# #INTERAGIR COM O CHAT
corpos_emails = [
    """Prezados Senhores,
    Espero que esta mensagem os encontre bem.
    Encaminho em anexo o relatório mensal referente às atividades desenvolvidas no período de outubro. O documento contempla os principais indicadores de desempenho, metas atingidas, pendências em aberto e sugestões de melhoria para os próximos ciclos.
    Solicito, por gentileza, que realizem a leitura atenta do material e, caso haja dúvidas ou considerações, estou à disposição para esclarecimentos ou reuniões complementares.
    Agradeço pela atenção e colaboração de sempre.
    Atenciosamente,
    [Seu Nome]""",

    """Prezada equipe,
    Cumprimentando cordialmente, venho por meio deste confirmar a realização da reunião de alinhamento estratégico, previamente agendada para sexta-feira, dia 15 de novembro, às 14h, na sala de conferências do 3º andar.
    A pauta principal será a revisão dos objetivos trimestrais, análise dos resultados obtidos até o momento e definição de ações prioritárias para o próximo período. Solicito que todos tragam seus respectivos relatórios atualizados e estejam preparados para contribuir com sugestões e observações pertinentes.
    Contamos com a presença de todos para garantir um encontro produtivo.
    Cordialmente,
    [Seu Nome]""",

    """Prezado(a) [Nome do Entrevistador],
    Gostaria de expressar minha sincera gratidão pela oportunidade de participar da entrevista realizada no dia 10 de novembro, referente à vaga de [Nome da Vaga] em sua respeitável empresa.
    Foi uma experiência enriquecedora poder conhecer mais sobre os valores, projetos e desafios da organização, bem como compartilhar um pouco da minha trajetória profissional e das competências que acredito poder agregar à equipe.
    Reitero meu interesse pela posição e coloco-me à disposição para quaisquer etapas adicionais do processo seletivo.
    Agradeço novamente pela atenção e gentileza com que fui recebido(a).
    Atenciosamente,
    [Seu Nome]""",

    """Prezados,
    Espero que estejam bem.
    Venho por meio deste solicitar a emissão da segunda via do boleto referente ao mês de outubro, vinculado ao contrato nº [Número do Contrato]. Por algum motivo, não recebi o documento dentro do prazo habitual e, para evitar qualquer transtorno, gostaria de regularizar a pendência o quanto antes.
    Caso necessário, posso fornecer novamente os dados cadastrais ou qualquer outra informação que facilite o processo.
    Agradeço antecipadamente pela atenção e aguardo retorno com o boleto atualizado.
    Cordialmente,
    [Seu Nome]""",
]

def resume_email(corpos_emails):
    lista_resumos = []

    for i, email in enumerate (corpos_emails):
        pergunta = (f"Resuma o email em no maximo 20 palavras", email)
        response = model.generate_content(pergunta)
        lista_resumos.append((f"E-mail {i+1}: {response.text}"))
        print((f"E-mail {i+1}: {response.text}"))

    return lista_resumos        

resumos = resume_email(corpos_emails)

# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# #CONFIGURAR CHAVE DA API
# client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

# pergunta = "o que é ml?"

# completion = client_groq.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[
#         {
#             "role": "user",
#             "content": pergunta
#         }
#     ],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     reasoning_effort="medium",
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")

with open("lista-resumos.txt", "a", encoding="utf-8") as arquivos:
    for elemento in resumos:
        arquivos.write(elemento + "\n")

arquivo_lido = []

with open("lista-resumos.txt", "a", encoding="utf-8") as arquivo:
    for linha in arquivo:
        arquivo_lido.append(linha + "\n")
