from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[
                {
    
                    'import_path':'chatterbot.logic.BestMatch',
                    'default_response':"Sorry, i dont know what that means",
                    'maximun_similary_threshold':0.90
                    
                }])

List_to_train =[
    "hola",
    "hola",
    "como estas?",
    "excelente",
    "cual es tu comida favorita?",
    "me gustan mucho los tacos",
    "cual es tu deporte favorito?",
    "no me gustan los deportes, pero me gusta el ajedrez",
    'te gusta jugar?',
    "sii",
    "los tacos",
    "a mi tambien",
    "sabes programar?",
    "no, pero preguntame acerca de futbol y si",
    "te gusta el futbol?",
    "si "

] 

chatterotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#esto es para agregar una lista de otros usuario crearon

list_trainer = ListTrainer(bot)
list_trainer.train(List_to_train)
chatterotCorpusTrainer.train('chatterbot.corpus.spanish')

def index(request):
    return render(request, 'blog/index.html')

 
#def specific(request):
 #   list1 = [1,2,3,4,5]
  #  return HttpResponse("list1")

def getResponse(request):
    userMessage =  request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)