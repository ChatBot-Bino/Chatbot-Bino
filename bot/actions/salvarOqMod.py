from rasa_core_sdk import Action
from pymongo import MongoClient
import re


class ActionSalvarOqMod(Action):
    def name(self):
        return "action_salvarOqMod"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()
            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            Mod2save = tracker['latest_message']['text']

            dispatcher.utter_message("Ok")
            # Bloco de regex para poder descobrir qual campo o usuario quer mudar.
            if(re.fullmatch(r"\b(\w*NOME\w*)\b|\b\b(\w*nome\w*)\b|\b\b(\w*Nome\w*)\b|\b", Mod2save)):
                Mod2save = "TituloDaAtv"
                dispatcher.utter_message("Agora me manda o novo nome da atividade.")
            elif(re.fullmatch(r"[obsOBSobservacaoobservação]+", Mod2save)):
                Mod2save = "OBS"
                dispatcher.utter_message("Agora me manda a nova observação.")
            elif(re.fullmatch(r"[dataDataATA]+", Mod2save)):
                Mod2save = "Data"
                dispatcher.utter_message("Agora me manda a nova data")
            else:
                Mod2save = "Inválido"
                dispatcher.utter_message("O tipo que você digitou não existe.")
                dispatcher.utter_message("Escreva algo coisa para continuar")

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'Vmod': Mod2save}})

            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
