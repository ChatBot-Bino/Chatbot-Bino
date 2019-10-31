from rasa_core_sdk import Action
from pymongo import MongoClient

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Rasa-network")
        try:
            client = MongoClient("192.168.112.2:27017")
            print(client.list_database_names())
            db = client.telegramDB 
            collectionsUsers = db.user
            collectionsUsers._insert({
                "firstName": "testes",
                "lastName": "Unicode",
                "me mama": "me da uma mamada tripla filha da putaaaa"

            })
            print(client.list_database_names())
        except ValueError:
            dispatcher.utter_message(ValueError)