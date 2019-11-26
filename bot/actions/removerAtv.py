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

            # TODO: Colocar os slots referentes a essas 2 variaveis.
            TituloParaRemover = ""
            DataParaRemover = ""
            quantidade = 0

            activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']

            for data in activities:
                if(data['TituloDaAtv'] == TituloParaRemover):
                    quantidade += 1

            if quantidade > 1:
                collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                "$pull":{
                    'activities': {
                        'TituloDaAtv': TituloParaRemover,
                        'Data': DataParaRemover
                        }
                    }
                })
            else:
                collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                "$pull":{
                    'activities': {
                        'TituloDaAtv': TituloParaRemover
                        }
                    }
                })

            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
