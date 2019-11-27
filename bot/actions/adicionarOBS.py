from rasa_core_sdk import Action
from pymongo import MongoClient
import re

class ActionAddOBS(Action):
    def name(self):
        return "action_adicionarOBS"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            NewOBS = tracker['latest_message']['text']
            if(re.fullmatch(r"[nNaãAÃoOp]+", NewOBS)):
                activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']
                TituloAnterior = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo']
                DataAnterior = collectionsUsers.find_one({'SenderID': sender_id})['VData']

                for OBS in activities:
                    if(OBS['TituloDaAtv'] == TituloAnterior and OBS['Data'] == DataAnterior):
                        activities = OBS
                        collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                            "$pull": {
                                'activities': {
                                    'TituloDaAtv': TituloAnterior,
                                    'Data': DataAnterior
                                }
                            }
                        })
                        activities['OBS'] = 'Nenhum obs salvo.'
                        collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': activities}})
                        StopIteration
            else:
                activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']
                TituloAnterior = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo']
                DataAnterior = collectionsUsers.find_one({'SenderID': sender_id})['VData']

                for OBS in activities:
                    if(OBS['TituloDaAtv'] == TituloAnterior and OBS['Data'] == DataAnterior):
                        activities = OBS
                        collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                            "$pull": {
                                'activities': {
                                    'TituloDaAtv': TituloAnterior,
                                    'Data': DataAnterior
                                }
                            }
                        })
                        activities['OBS'] = NewOBS
                        collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': activities}})
                        StopIteration
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
