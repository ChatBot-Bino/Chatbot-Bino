from rasa_core_sdk import Action
from pymongo import MongoClient
import re


class ActionAddDate(Action):
    def name(self):
        return "action_adicionarData"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            NewData = tracker['latest_message']['text']
            # Regex de Data
            if(re.fullmatch(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$", NewData)):

                activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']
                # Pegando o titulo que a pessoa colocou 
                # para botar no lugar que a data dessa atividade deve ir.
                TituloAnterior = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo'] 

                for Data in activities:
                    if(Data['TituloDaAtv'] == TituloAnterior):
                        # Salvando a atividade temporariamente
                        activities = Data

                        # Tirando a atividade que foi adicionada para poder colocar uma nova no lugar
                        collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                            "$pull": {
                                'activities': {
                                    'TituloDaAtv': TituloAnterior
                                }
                            }
                        })
                        activities['Data'] = NewData
                        collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VData': NewData}})
                        collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': activities}}) # Colocando a nova atividade
                        StopIteration
            else:
                dispatcher.utter_message("Data inserida não aceita.\nSalvando como nenhuma data salva")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
