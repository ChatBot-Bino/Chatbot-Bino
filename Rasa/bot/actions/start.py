from rasa_core_sdk import Action
from pymongo import MongoClient

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            client = MongoClient("172.17.0.2:27017")
            print(client.list_database_names())
            db = client.telegramdb
            collectionsUsers = db.user
            collectionsUsers._insert({
                "firstName": "testes",
                "lastName": "Unicode"
            })
            print(client.list_database_names())
        except ValueError:
            dispatcher.utter_message(ValueError)