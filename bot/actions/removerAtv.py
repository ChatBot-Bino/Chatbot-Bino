from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionRmAtv(Action):
    def name(self):
        return "action_removerAtv"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            Titulo2rm = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo']
            Data2rm = collectionsUsers.find_one({'SenderID': sender_id})['VData']

            activities = collectionsUsers.find_one({'SenderID': sender_id})['activities']

            AtividadeRemovida = False

            for data in activities:
                if(data['TituloDaAtv'] == Titulo2rm and data['Data'] == Data2rm):
                    collectionsUsers.find_one_and_update({'SenderID': sender_id}, {
                        "$pull": {
                            'activities': {
                                'TituloDaAtv': Titulo2rm,
                                'Data': Data2rm
                            }
                        }
                    })
                    AtividadeRemovida = True
                    StopIteration

            Name = collectionsUsers.find_one({'SenderID': sender_id})['first_name']

            if not AtividadeRemovida:
                Name = collectionsUsers.find_one({'SenderID': sender_id})['first_name']
                dispatcher.utter_message(Name + ", não achei essa atividade nas suas atividades salvas.")
            else:
                dispatcher.utter_message(Name + ", pronto atividade removida.")
            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
