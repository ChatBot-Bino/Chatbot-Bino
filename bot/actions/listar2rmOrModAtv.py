from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionListar2rmOrModAtv(Action):
    def name(self):
        return "action_listar2rmOrModAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            activities = collectionsUsers.find_one({'SenderID': sender_id})
            Name = activities['first_name']
            lastIntent = tracker['latest_message']['intent']['name']
   
            for dataArray in activities['activities']:
                NomeDaAtv = "Nome: " + dataArray['TituloDaAtv'] + "\n"
                OBS = "OBS: " + dataArray['OBS'] + "\n"
                Text = NomeDaAtv + OBS + "Data: " + dataArray['Data'] + "\n"
                dispatcher.utter_message(Text)

            dispatcher.utter_message("Ok.")

            if(lastIntent == "remover_atividade"):
                dispatcher.utter_message(Name + ", agora me manda o nome da atividade que você quer retirar?")

            elif(lastIntent == "modificar_atividade"):
                dispatcher.utter_message(Name + ", agora me manda o nome da atividade que você quer modificar.")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
