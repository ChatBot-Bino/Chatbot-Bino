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

            tracker = tracker.current_state()
            sender_id = tracker['sender_id']
            
            if not collectionsUsers.count({'SenderID': sender_id}):
                first_name = None
                last_name = None
                user = {
                    'SenderID': sender_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'classes': {},
                    'exams': {},
                    'activities': {}
                }
                collectionsUsers.insert_one(user)
            


        except ValueError:
            dispatcher.utter_message(ValueError)
