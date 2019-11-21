from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionChecarUsoGerenciadorFaltas(Action):
    def name(self):
        return "action_checar_uso_gerenciador_faltas"

    def run(self, dispatcher, tracker, domain):
        
        last_intent = tracker.latest_message['intent'].get('name')

        if (last_intent == None):
            return [SlotSet("gerenciador_faltas_status", tracker.get_slot("gerenciador_faltas_status"))]

        elif (last_intent == "negar"):
            return [SlotSet("gerenciador_faltas_status", "primeira_vez")]

        elif (last_intent == "afirmar"):
            return [SlotSet("gerenciador_faltas_status", "uso_confirmado")]
        
        else:
            return [SlotSet("gerenciador_faltas_status", tracker.get_slot("gerenciador_faltas_status"))]


class ActionSetUsoConfirmado(Action):
    def name(self):
        return "action_set_uso_confirmado"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("gerenciador_faltas_status", "uso_confirmado")
        ]