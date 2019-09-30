import requests
import logging
from pymongo import MongoClient
from rasa_core_sdk import Action
from time import sleep


class ActionStart(Action):
    def name(self):
        return "custom_start"

    def run(self, dispatcher, tracker, domain):

        # Tracker that stores the state of dialogue, to gets the users id
        tracker = tracker.current_state()
        sender_id = tracker['sender_id']

        # Message to send to the user
        text = ('Espera uns segundinhos aí, rapidinho... ')
        sleep(2.75)

        # Get users data to build a user to the database
        data = requests.get(
            'https://api.telegram.org/bot962521399:AAGyRWTL9kAmjcgFn6mem_DxDyeXcbMRppA/sendMessage?chat_id={}&text={}'
            .format(sender_id, text)
        ).json()

        # Check if user data was get succefully
    
        client = MongoClient(port = 27017)
        db = client['bino_telegram']

        # Get all users that are registered and check if
        users_data = list(db.users.find({}, {'sender_id': 1, '_id': 0}))

        users_id = []
        for users in users_data:
            users_id.append(users['sender_id'])

        print(users_id)
        
        new_data = self.build_telegram_user(data, sender_id)
        self.save_telegram_user(new_data, db)


    def build_telegram_user(self, data, sender_id):
        first_name = ""
        last_name = ""

        first_name = data['result']['chat']['first_name']

        try:
            last_name = data['result']['chat']['last_name']
        except KeyError as exception:
            print("Telegram user has not a last name!")
            logging.info(exception)


        return {
            'sender_id': sender_id,
            'name': first_name + ' ' + last_name,
        }

    def save_telegram_user(self, user_data, db_telegram):
        # Build user structure and save in telegram database
        db_telegram.users.insert_one(user_data)
        logging.info('User save in telegram database')
        return []
