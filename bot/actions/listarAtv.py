from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionListarAtv(Action):
    def name(self):
        return "action_listarAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            activities = collectionsUsers.find_one({'SenderID': sender_id})
            dispatcher.utter_message("Suas atividades salvas são essas:")

            for dataArray in activities['activities']:
                NomeDaAtv = "Nome: " + dataArray['TituloDaAtv'] + "\n"
                OBS = "OBS: " + dataArray['OBS'] + "\n"
                Text = NomeDaAtv + OBS + "Data: " + dataArray['Data'] + "\n"
                dispatcher.utter_message(Text)

            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
