from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionAddAtv(Action):
    def name(self):
        return "action_adicionar"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            

        except ValueError:
            dispatcher.utter_message(ValueError)
