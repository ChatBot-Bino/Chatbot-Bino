from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionAddAtv(Action):
    def name(self):
        return "action_adicionar"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            Atividade = tracker['latest_message']['text']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VTitulo': Atividade}})
            newAtv = {
                "TituloDaAtv": Atividade,
                'Data': "Nenhuma Salva",
                'OBS': "Nenhum OBS"
            }

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VData': "Nenhuma Salva"}})
            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'Vmod': None}})
            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VNewMod': None}})
            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VObs': "Nenhum OBS"}})
            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VTitulo': Atividade}})

            collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': newAtv}})
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
