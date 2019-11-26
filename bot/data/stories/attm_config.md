## 1. gerenciador_faltas + primeira_vez
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso

## 1.1 gerenciador_faltas + primeira_vez + negar_uso
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* negar
  - action_checar_uso_gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_deixar_pra_depois

## 1.2 gerenciador_faltas + primeira_vez + afirmar_uso
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_checar_uso_gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade


## 1.2.1. gerenciador_faltas + primeira_vez + afirmar_uso + grade_desatualizada
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
  - action_get_grade_status
  - slot{"grade_status": "grade_desatualizada"}
  - utter_grade_desatualizada


## 1.2.2. gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio

## 1.2.2.1 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_diario
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_dia
  - action_set_relatorio_status
  - slot{"frequencia_relatorio": "dia"}
  - utter_configurado_dia

## 1.2.2.2 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_semanal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_semana
  - action_set_relatorio_status
  - slot{"frequencia_relatorio": "semana"}
  - utter_configurado_semana

## 1.2.2.3 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_mensal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_mes
  - action_set_relatorio_status
  - slot{"frequencia_relatorio": "mes"}
  - utter_configurado_mes

## 2.1 gerenciador_faltas + uso_confirmado + grade_nao_enviada
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_nao_enviada
  - action_get_grade_status
  - slot{"grade_status": "grade_nao_enviada"}
  - utter_ask_grade
  - utter_guia_enviar_grade

## 2.2 gerenciador_faltas + uso_confirmado + grade_desatualizada
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_desatualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_desatualizada"}
  - utter_grade_desatualizada
  - utter_guia_enviar_grade

## 2.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_nao_configurado
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_nao_configurado"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio

## 2.3.1 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_nao_configurado + relatorio_diario
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_nao_configurado"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_dia
  - action_set_relatorio_status
  - slot{"relatorio_status": "relatorio_diario"}
  - utter_configurado_dia

## 2.3.2 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_nao_configurado + relatorio_semanal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_nao_configurado"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_semana
  - action_set_relatorio_status
  - slot{"relatorio_status": "relatorio_semanal"}
  - utter_configurado_semana

## 2.3.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_nao_configurado + relatorio_mensal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_nao_configurado"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
* frequencia_relatorio_mes
  - action_set_relatorio_status
  - slot{"relatorio_status": "relatorio_mensal"}
  - utter_configurado_mes

## 2.3.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_diario
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_diario"}
  - utter_gerenciador_faltas

## 2.3.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_semanal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_semanal"}
  - utter_gerenciador_faltas

## 2.3.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_mensal
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
* grade_atualizada
  - action_get_grade_status
  - slot{"grade_status": "grade_atualizada"}
  - action_checar_relatorio_status
  - slot{"relatorio_status": "relatorio_mensal"}
  - utter_gerenciador_faltas