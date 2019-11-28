from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionSalvarNomeAtv2rm(Action):
    def name(self):
        return "action_salvarNomeAtv2rm"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user
            # Essa custon action serve para poder salvar no Banco de Dados o nome de atividade que a pessoa quer remover.
            Titulo2Save = tracker['latest_message']['text']

            Name = collectionsUsers.find_one({'SenderID': sender_id})['first_name']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VTitulo': Titulo2Save}})
            dispatcher.utter_message("Ok")
            dispatcher.utter_message(Name + ", agora me manda a data dessa atividade. No formato DD/MM/YYYY")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
