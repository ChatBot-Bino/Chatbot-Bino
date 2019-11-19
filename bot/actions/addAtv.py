from rasa_core_sdk import Action
from pymongo import MongoClient
import requests

class ActionAddAtv(Action):
    def name(self):
        return "action_addAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            
            Materia = tracker.latest_message.get('text')
            dispatcher.utter_message(Materia)

        except ValueError:
            dispatcher.utter_message(ValueError)
