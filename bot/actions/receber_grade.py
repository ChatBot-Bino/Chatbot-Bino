from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionReceberGrade(Action):
    def name(self):
        return "action_receber_grade"

    def run(self, dispatcher, tracker, domain):

        """
        
        1. Extrair e processar os dados do PDF

        2. Receber o status da grade em: 'grade_status'
            
            2.0. 'grade_nao_enviada', caso não consiga extrair os dados

            2.1. 'grade_desatualizada', caso o semestre esteja errado

            2.2. 'grade_atualizada', caso o semestre esteja correto

        """
        
        # ======== Debugging ========
        # grade_status = "grade_nao_enviada"
        # grade_status = "grade_desatualizada"
        grade_status = "grade_atualizada"

        if (grade_status == "grade_desatualizada"):
            
            return [SlotSet("grade_status", "grade_desatualizada")]

        elif (grade_status == "grade_atualizada"):
            
            return [SlotSet("grade_status", "grade_atualizada")]
        
        else:
            
            return [SlotSet("grade_status", "grade_nao_enviada")]
