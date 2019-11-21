from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import re


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

class AdicionarMateriaForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "adicionar_materia_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["materia", "horario"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"materia": [self.from_text()],
                "horario": [self.from_text()]}

    def validate_horario(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate time value."""

        if bool(re.match(r"[0-9]{2}:[0-9]{2}", value)):
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"horario": value}
        else:
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"horario": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_materia_adicionada', tracker)
        return []


class RemoverMateriaForm(FormAction):

    def name(self):
        # type: () -> Text
        """Identificador do form"""

        return "remover_materia_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """Lista de slots que o form deve preencher"""

        return ["materia", "confirmacao"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"materia": [self.from_text()],
                "confirmacao": [self.from_intent(intent='afirmar', value=True),
                                self.from_intent(intent='negar', value=False)]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_materia_removida', tracker)
        return []