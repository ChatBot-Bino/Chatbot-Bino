from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionSalvarNewInfMod(Action):
    def name(self):
        return "action_salvarNewInfoMod"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            NewInfo = tracker['latest_message']['text']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VNewMod': NewInfo}})
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
