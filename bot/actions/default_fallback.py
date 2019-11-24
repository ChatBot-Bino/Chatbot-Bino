from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction

class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        
        return [FollowupAction("utter_default")]