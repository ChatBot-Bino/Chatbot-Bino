from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionConfigurarRelatorio(Action):
    def name(self):
        return "action_configurar_relatorio"

    def run(self, dispatcher, tracker, domain):

        """
        Script para configurar a frequência do relatório
        
        1. Receber o status do relatorio em: 'relatorio_status'
            
            2.0. 'relatorio_nao_configurado', padrão

            2.1. 'relatorio_diario', caso o semestre esteja errado

            2.2. 'relatorio_semanal', caso o semestre esteja correto
            
            2.2. 'relatorio_mensal', caso o semestre esteja corretp
        
        """

        intent = tracker.latest_message['intent'].get('name')

        if (intent == "frequencia_relatorio_dia"):
            frequencia = "relatorio_diario"

        elif (intent == "frequencia_relatorio_semana"):
            frequencia = "relatorio_semanal"

        elif (intent == "frequencia_relatorio_mes"):
            frequencia = "relatorio_mensal"
        
        else:
            frequencia = "relatorio_nao_configurado"

        return [SlotSet("frequencia_relatorio", frequencia)]
