from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class ConfigurarRelatorio(FormAction):

    def name(self):
        # type: () -> Text

        return "configurar_relatorio_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["frequencia_relatorio"]

    def validate_frequencia_relatorio(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate time value."""

        if (tracker.latest_message['intent'].get('name') == 'frequencia_relatorio_dia'):
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"frequencia_relatorio": value}

        elif (tracker.latest_message['intent'].get('name') == 'frequencia_relatorio_semana'):
            return {"frequencia_relatorio": value}

        elif (tracker.latest_message['intent'].get('name') == 'frequencia_relatorio_mes'):
            return {"frequencia_relatorio": value}

        else:
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frequencia_relatorio": None}


    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        intent = tracker.latest_message['intent'].get('name')

        return {"frequencia_relatorio": [self.from_intent(intent='frequencia_relatorio_dia',
                                        value = "dia"),
                                        self.from_intent(intent='frequencia_relatorio_semana',
                                        value = "semana"),
                                        self.from_intent(intent='frequencia_relatorio_mes',
                                        value = "mes"),
                                        ]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_relatorio_configurado', tracker)
        return []