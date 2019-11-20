from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionChecarPrimeiraVez(Action):
    def name(self):
        return "action_checar_primeira_vez"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("gerenciador_faltas_status", "primeira_vez")
        ]


class ActionChecarGrade(Action):
    def name(self):
        return "action_checar_grade"

    def run(self, dispatcher, tracker, domain):

        """
        Script para checar o estado da grade

        1. Receber o status da grade em: 'grade_status'
            
            2.0. 'grade_nao_enviada', caso não consiga extrair os dados

            2.1. 'grade_desatualizada', caso o semestre esteja errado

            2.2. 'grade_atualizada', caso o semestre esteja correto

        """
        
        # ================ Debugging ================ #
        intent = tracker.latest_message['intent'].get('name')

        return [SlotSet("grade_status", intent)]