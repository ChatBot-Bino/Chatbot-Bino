from rasa_core_sdk import Action


class ActionFaltas(Action):
    def name(self):
        return "action_faltas"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Voce digitou /faltas")
        except ValueError:
            dispatcher.utter_message(ValueError)
