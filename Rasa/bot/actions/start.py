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
            tracker = tracker.current_state()
            sender_id = tracker['sender_id']

            text = ('Espera uns segundinhos aí, rapidinho... ')
            sleep(2.75)

            data = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
                .format(TELEGRAM_TOKEN, sender_id, text)
            ).json()

            client = MongoClient(TELEGRAM_DB)
            db = client['telegram_db']

            users_data = list(db.users.find({}, {'sender_id': 1, '_id': 0}))

            users_id = []
            for users in users_data:
                users_id.append(users['sender_id'])

            print(users_data)

            # if sender_id in users_id:
            #     # User found in the database
            #     for message in messages:
            #         dispatcher.utter_message(message)
            #     return []
            # else:
            #      if messenger is "Telegram":
            #         new_data = self.build_telegram_user(data, sender_id)
            #         self.save_telegram_user(new_data, db)

        except ValueError:
            dispatcher.utter_message(ValueError)