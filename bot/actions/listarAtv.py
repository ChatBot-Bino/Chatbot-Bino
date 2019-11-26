from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionAddAtv(Action):
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
                OBS = NomeDaAtv + "OBS: " + dataArray['OBS'] + "\n"
                DataAtv = OBS + "Data: " + dataArray['Data'] + "\n"
                dispatcher.utter_message(DataAtv)

            
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
