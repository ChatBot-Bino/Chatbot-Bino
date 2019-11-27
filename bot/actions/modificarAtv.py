from rasa_core_sdk import Action
from pymongo import MongoClient
import re

class ActionModAtv(Action):
    def name(self):
        return "action_modAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user
            TituloDaMod = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo']
            DataDaMod = collectionsUsers.find_one({'SenderID': sender_id})['VData']
            Mod2Change = collectionsUsers.find_one({'SenderID': sender_id})['Vmod']
            NewMod = collectionsUsers.find_one({'SenderID': sender_id})['VNewMod']

            activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']

            for data in activities:
                if(data['TituloDaAtv'] == TituloDaMod and data['Data'] == DataDaMod):
                    NewAtv = data
                    collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                        "$pull": {
                            'activities': {
                                'TituloDaAtv': TituloDaMod,
                                'Data': DataDaMod
                            }
                        }
                    })
                    NewAtv[Mod2Change] = NewMod
                    collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': NewAtv}})
                    StopIteration
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
