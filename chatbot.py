from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('DEInfo Bot')

conversa = ['oi', 'Olá', 'tudo bem?', 'tudo ótimo', 'você gosta de programar?',
'Ainda não sei, mas tenho vontade de aprender C++ e Python',"se for escolher gosta de qual primeiro?",
"Gostaria de primeiro aprender C++.","qual o seu nome?","Meu nome é DEInfo bot.","deus existe?","Acho que não.",
"chatbots vão para o inferno?","Existe inferno?","o que é você?", "Sou um chatbot, um programa de computador",
"qual a sua idade?","Não tenho idade.","você gosta de ler?","Sim, bastante!", "que tipo de livro você gosta?",
"Livros de ficção científica.","qual seu autor favorito?", "Tenho vários, mas acho que Asimov é o meu favorito."]


convLink = ["Você sabe o que é um dataset?", "Dataset é simplesmente um banco de dados.","Para que serve um dataset?",
            "Pesquisadores usam os datasets para buscar informações, responder perguntas...", "Onde para baixar datasets?",
            "O Yahoo é um bom lugar", "Diga outro site para baixar dataset", "O site do Banco Mundial"]

trainer = ListTrainer(bot)

trainer.train(conversa)
trainer.train(convLink)

pergunta=''
print("Olá, sou o DEInfo Bot, para sair da conversa digite 'sair' sem as aspas.")
while True:
    try:
        pergunta = input("Usuário: ")
        if pergunta == "sair":
            break
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
            print('DEInfo Bot: ', resposta)
        else:
            print('DEInfo Bot: Ainda não sei responder esta pergunta')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break