import requests
import logging
from pymongo import MongoClient
from time import sleep
from rasa_core_sdk import Action
from constantes import (TELEGRAM_TOKEN, TELEGRAM_DB)

class StartComand(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
        
            db = MongoClient("mongodb://mongo:27017")
            TelegramDB = db.TelegramDB

            user_data = {
                'name': 'First Name',
                'last_name': 'last_name',
                'materias': {
                    'materia1': 'nome_da_primeira',
                    'materia2': 'nome_da_segunda',
                    'materia3': 'nome_da_terceira'
                }
            }
            result = TelegramDB.insert_one(user_data)
            print('One user: {0}'.format(result.inserted_id))

            # if sender_id in users_id:
            #     # User found in the database
            #     for message in messages:
            #         dispatcher.utter_message(message)
            #     return []
            # else:
            #      if messenger is "Telegram":
            #         new_data = self.build_telegram_user(data, sender_id)
            #         self.save_telegram_user(new_data, db)

        except Exception as exc:
            dispatcher.utter_message(exc)