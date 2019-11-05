from rasa_core_sdk import Action
from pymongo import MongoClient

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Insert test.")
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user
            collectionsUsers._insert({
                "firstName": "testes",
                "lastName": "Unicode"
            })  
            # rdispatcher.utter_message(client.list_database_names())
            dispatcher.utter_message("Att")
            # dispatcher.utter_message(client)
        except ValueError:
            dispatcher.utter_message(ValueError)