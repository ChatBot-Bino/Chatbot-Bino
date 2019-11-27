from rasa_core_sdk import Action
from pymongo import MongoClient
import re

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

            Mod2save = tracker['latest_message']['text']

            dispatcher.utter_message("Ok")
            if(re.match(r"[atvATVatividadeATIVIDADE]+", Mod2save)):
                Mod2save = "TituloDaAtv"
                dispatcher.utter_message("Agora me manda o novo nome da atividade.")
            elif(re.match(r"[obsOBSobservacaoobservação]+", Mod2save)):
                Mod2save = "OBS"
                dispatcher.utter_message("Agora me manda a nova observação.")
            elif(re.match(r"[dataDataATA]+", Mod2save)):
                Mod2save = "Data"
                dispatcher.utter_message("Agora me manda a nova data")

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'Vmod': Mod2save}})

            
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
