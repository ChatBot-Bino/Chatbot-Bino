from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionConfigurarRelatorio(Action):
    def name(self):
        return "action_configurar_relatorio"

    def run(self, dispatcher, tracker, domain):

        frequencia = None

        intent = tracker.latest_message['intent'].get('name')

        if (intent == "frequencia_relatorio_dia"):
            frequencia = "dia"

        elif (intent == "frequencia_relatorio_semana"):
            frequencia = "semana"

        elif (intent == "frequencia_relatorio_mes"):
            frequencia = "mes"

        return [SlotSet("frequencia_relatorio", frequencia)]
