#import ChatBot
from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer 
bote = Chatbot("Test")

conversa = ["oi","ola","tudo bem?","eu estou bem"]

bote.set_trainer(ListTrainer)
bote.train(conversa)

while True:
	quest = input("Voce: ")
	resposta = bot.get_response(quest)
	print ('Bot: ', resposta)
