from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionResetSlots(Action):
    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("materia", None),
            SlotSet("horario", None),
            SlotSet("confirmacao", None),
            SlotSet("frequencia_relatorio", None)
        ]

class ActionSetUsoConfirmado(Action):
    def name(self):
        return "action_set_uso_confirmado"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("gerenciador_faltas_status", "uso_confirmado")
        ]

class ActionConfigurarRelatorio(Action):
    def name(self):
        return "action_configurar_relatorio"

    def run(self, dispatcher, tracker, domain):
        
        # ======== Debugging ========
        # grade_status = "grade_nao_enviada"
        # grade_status = "grade_desatualizada"
        grade_status = "grade_atualizada"
            
        return [SlotSet("grade_status", grade_status)]

