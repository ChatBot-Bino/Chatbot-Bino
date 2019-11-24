from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionChecarRelatorioStatus(Action):
    def name(self):
        return "action_checar_relatorio_status"

    def run(self, dispatcher, tracker, domain):

        """
        Script para checar a frequência do relatório
        
        1. Receber o status do relatorio em: 'relatorio_status'
            
            2.0. 'relatorio_nao_configurado', padrão

            2.1. 'relatorio_diario', caso o semestre esteja errado

            2.2. 'relatorio_semanal', caso o semestre esteja correto
            
            2.2. 'relatorio_mensal', caso o semestre esteja corretp
        
        """

        relatorio_status = tracker.get_slot("relatorio_status")

        if (relatorio_status == "relatorio_nao_configurado"):
            return [SlotSet("relatorio_status", "relatorio_nao_configurado")]
        
        if (relatorio_status == "relatorio_diario"):
            return [SlotSet("relatorio_status", "relatorio_diario")]

        if (relatorio_status == "relatorio_semanal"):
            return [SlotSet("relatorio_status", "relatorio_semanal")]

        if (relatorio_status == "relatorio_mensal"):
            return [SlotSet("relatorio_status", "relatorio_mensal")]

        return []
        



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

        last_intent = tracker.latest_message['intent'].get('name')

        if (last_intent == "frequencia_relatorio_dia"):
            return [SlotSet("relatorio_status", "relatorio_diario")]
        
        if (last_intent == "frequencia_relatorio_semana"):
            return [SlotSet("relatorio_status", "relatorio_semanal")]

        if (last_intent == "frequencia_relatorio_mes"):
            return [SlotSet("relatorio_status", "relatorio_mensal")]

        return []
        
