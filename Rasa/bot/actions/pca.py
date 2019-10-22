
from rasa_core_sdk import Action


class ActionTest(Action):
    def name(self):
        return "action_pca"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("FUNCIONOUUUUUU")
        except ValueError:
            dispatcher.utter_message(ValueError)