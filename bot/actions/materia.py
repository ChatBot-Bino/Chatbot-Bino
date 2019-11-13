# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet


# class ActionMateria(Action):
#     def name(self):
#         return "action_materia"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):

#         materia = tracker.get_slot('materia')

#         try:
#             dispatcher.utter_message("Você está fazendo {}?".format(materia))
#         except ValueError:
#             dispatcher.utter_message(ValueError)
#         return [SlotSet("materia", materia)]
