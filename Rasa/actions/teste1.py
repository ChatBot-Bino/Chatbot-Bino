import requests
import json
from pymongo import MongoClient
from rasa_sdk import Action


class ActionTeste(Action):
  def name(self):

    return "action_test"

  def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Msg enviada por custon action')


 