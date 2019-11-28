from rasa_core_sdk import Action
from pymongo import MongoClient
import requests


class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            # Esse bloco de codico serve para se conectar ao MongoDB e usar a collection user que esta os dados.
            # Ele se repete por todas as custon actions.
            tracker = tracker.current_state()
            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            text = "Olá, eu sou o Bino, seu assistente virtual!"
            # A parte daqui para baixo se tem a parte de criar o usuario no banco de dados.
            # Com o nome e o senderId da pessoa.
            if(sender_id == "default"):
                first_name = "Rasa Shell"
                dispatcher.utter_message(text)
            else:
                # remover o token do telegram e botar em uma pasta separada para não ir para o github.
                TELEGRAM_TOKEN = "962521399:AAGyRWTL9kAmjcgFn6mem_DxDyeXcbMRppA"
                data = requests.get(
                    'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(TELEGRAM_TOKEN, sender_id, text)
                ).json()
                first_name = data['result']['chat']['first_name']

            if not collectionsUsers.count({'SenderID': sender_id}):

                user = {
                    'SenderID': sender_id,
                    'first_name': first_name,
                    'classes': [],
                    'activities': [],
                    'VData': None,
                    'VTitulo': None,
                    'VObs': None,
                    'VNewMod': None,
                    'Vmod': None
                }
                collectionsUsers.insert_one(user)

            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
