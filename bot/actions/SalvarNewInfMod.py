from rasa_core_sdk import Action
from pymongo import MongoClient


class ActionSalvarNewInfMod(Action):
    def name(self):
        return "action_salvarNewInfoMod"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker = tracker.current_state()

            sender_id = tracker['sender_id']
            client = MongoClient("mongo:27017")
            db = client.telegramdb
            collectionsUsers = db.user

            NewInfo = tracker['latest_message']['text']

            collectionsUsers.update_one({'SenderID': sender_id}, {'$set': {'VNewMod': NewInfo}})

            # Pegando do DB todos os dados que a pessoa quer mudar.
            TituloDaMod = collectionsUsers.find_one({'SenderID': sender_id})['VTitulo']
            DataDaMod = collectionsUsers.find_one({'SenderID': sender_id})['VData']
            Mod2Change = collectionsUsers.find_one({'SenderID': sender_id})['Vmod']
            NewMod = NewInfo

            valido = False
            # If com o objetivo de checar se a opção de campo do usuario foi escolhida entre Nome, OBS e Data.
            if Mod2Change != "Inválido":
                activities = collectionsUsers.find_one({'SenderID': sender_id})['activities'] # Pegando o array de atividades do usuario
                for data in activities:
                    if(data['TituloDaAtv'] == TituloDaMod and data['Data'] == DataDaMod):
                        valido = True

                        dispatcher.utter_message("Achei e ja mudei para você.")
                        dispatcher.utter_message("Agora ela está assim:")

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

                        # Imprimindo a atividade nova 
                        collectionsUsers.update_one({'SenderID': sender_id}, {'$addToSet': {'activities': NewAtv}})
                        NomeDaAtv = "Nome: " + NewAtv['TituloDaAtv'] + "\n"
                        OBS = "OBS: " + NewAtv['OBS'] + "\n"
                        Text = NomeDaAtv + OBS + "Data: " + NewAtv['Data'] + "\n"
                        dispatcher.utter_message(Text)
                        StopIteration

            if not valido:
                dispatcher.utter_message("Não achei uma atividade com:")
                NomeDaAtv = "Nome: " + TituloDaMod + "\n"
                Text = NomeDaAtv + "Data: " + DataDaMod + "\n"
                dispatcher.utter_message(Text)

            client.close
        except ValueError:
            dispatcher.utter_message(ValueError)
