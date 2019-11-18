## start
* start{"comando": "start"}
  - utter_start

## help
* help{"comando": "help"}
  - utter_help

## cumprimentar
* cumprimentar

  - utter_cumprimentar

## despedir
* despedir
  - utter_despedir

## agradecer
* agradecer
  - utter_agradecer

## gerenciador_faltas
* gerenciador_faltas
  - utter_gerenciador_faltas

## gerenciador_atividades
* gerenciador_atividades
  - utter_gerenciador_atividades

## enviar_grade
* enviar_grade
  - utter_enviar_grade

## saber_grade
* saber_grade
  - utter_saber_grade

## alterar_grade
* alterar_grade
  - utter_alterar_grade

## adicionar_materia
* adicionar_materia
  - utter_adicionar_materia 
  - adicionar_materia_form
  - form{"name": "adicionar_materia_form"}
  - form{"name": null}
  - action_reset_slots

## remover_materia
* remover_materia
  - utter_remover_materia 
  - remover_materia_form
  - form{"name": "remover_materia_form"}
  - form{"name": null}
  - action_reset_slots

## configurar_relatorio dia
* configurar_relatorio
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_dia
  - action_configurar_relatorio
  - utter_configurado_dia
  - slot{"frquencia_relatorio": null}

## configurar_relatorio semana
* configurar_relatorio
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_semana
  - action_configurar_relatorio
  - utter_configurado_semana
  - slot{"frquencia_relatorio": null}

## configurar_relatorio mes
* configurar_relatorio
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_mes
  - action_configurar_relatorio
  - utter_configurado_mes
  - slot{"frquencia_relatorio": null}


