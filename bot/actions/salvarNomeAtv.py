from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionSalvarNomeAtv(Action):
    def name(self):
        return "action_salvarNomeAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            Titulo2Save = tracker['latest_message']['text']

            Name = collectionsUsers.find_one({'SenderID': sender_id})['first_name']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VTitulo': Titulo2Save}})
            dispatcher.utter_message("Ok")
            dispatcher.utter_message(Name + ", agora me manda a data dessa atividade.")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
