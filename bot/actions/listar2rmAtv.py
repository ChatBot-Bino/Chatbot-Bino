from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionListar2rmAtv(Action):
    def name(self):
        return "action_listar2rmAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            activities = collectionsUsers.find_one({'SenderID': sender_id})
            Name = activities['first_name']
            dispatcher.utter_message(Name + ", qual das suas atividades salvas você quer retirar?")

            for dataArray in activities['activities']:
                NomeDaAtv = "Nome: " + dataArray['TituloDaAtv'] + "\n"
                OBS = "OBS: " + dataArray['OBS'] + "\n"
                Text = NomeDaAtv + OBS + "Data: " + dataArray['Data'] + "\n"
                dispatcher.utter_message(Text)
            dispatcher.utter_message("Ok")
            dispatcher.utter_message(Name + ", agora me manda o nome da atividade.")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
