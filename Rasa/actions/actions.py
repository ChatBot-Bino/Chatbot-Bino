# import requests
# import json
# from pymongo import MongoClient
# from rasa_sdk import Action


# class ActionTeste(Action):
#   def name(self):
#     return "action_test"

#   def run(self, dispatcher, tracker, domain):
#     telegram_client = MongoClient(port=27017)
#     telegram_db = telegram_client['lino_telegram']

#     return []

#   def save_telegram_user(self, user_data, db_telegram):
#         # Build user structure and save in telegram database
#         db_telegram.users.insert_one(user_data)
#         logging.info('User save in telegram database')
#         return []

#    def build_telegram_user(self, data, sender_id):
#         first_name = ""
#         last_name = ""

#         first_name = data['result']['chat']['first_name']

#         try:
#             last_name = data['result']['chat']['last_name']
#         except KeyError as exception:
#             print("Telegram user has not a last name!")
#             logging.info(exception)

#         notification_list = self.build_notification_list()

#         return {
#             'sender_id': sender_id,
#             'name': first_name + ' ' + last_name,
#             'notification': notification_list
#         }