from rasa_core_sdk import Action
from pymongo import MongoClient

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user
        except ValueError:
            dispatcher.utter_message(ValueError)