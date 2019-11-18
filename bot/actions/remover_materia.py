from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

import re


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