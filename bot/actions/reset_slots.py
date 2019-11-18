from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionResetMateria(Action):
    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("materia", None),
            SlotSet("horario", None),
            SlotSet("confirmacao", None),
            SlotSet("frequencia_relatorio", None)
        ]
