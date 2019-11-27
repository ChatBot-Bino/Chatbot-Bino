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

            Data2Rm = tracker['latest_message']['text']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VData': Data2Rm}})
            dispatcher.utter_message("Ok")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
