## 1. gerenciador_faltas + primeira_vez
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "primeira_vez"}
  - utter_gerenciador_faltas
  - utter_ask_confirmar_uso
> check_gerenciador_faltas_primeira_vez_ask_confirmar_uso

## 1.1 gerenciador_faltas + primeira_vez + negar_uso
> check_gerenciador_faltas_primeira_vez_ask_confirmar_uso
* negar
  - utter_deixar_pra_depois

## 1.2 gerenciador_faltas + primeira_vez + afirmar_uso
> check_gerenciador_faltas_primeira_vez_ask_confirmar_uso
* afirmar
  - action_set_uso_confirmado
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_comemorar
  - utter_ask_grade
  - utter_guia_enviar_grade
> check_gerenciador_faltas_primeira_vez_afirmar_uso

## 1.2.1. gerenciador_faltas + primeira_vez + afirmar_uso + grade_desatualizada
> check_gerenciador_faltas_primeira_vez_afirmar_uso
* grade_enviada
  - action_receber_grade
  - slot{"grade_status": "grade_desatualizada"}
  - utter_grade_desatualizada

## 1.2.2. gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada
> check_gerenciador_faltas_primeira_vez_afirmar_uso
* grade_enviada
  - action_receber_grade
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
> check_gerenciador_faltas_primeira_vez_afirmar_uso_perguntar_freq_relatorio

## 1.2.2.1 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_diario
> check_gerenciador_faltas_primeira_vez_afirmar_uso_perguntar_freq_relatorio
* frequencia_relatorio_dia
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "dia"}
  - utter_configurado_dia

## 1.2.2.2 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_semanal
> check_gerenciador_faltas_primeira_vez_afirmar_uso_perguntar_freq_relatorio
* frequencia_relatorio_semana
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "semana"}
  - utter_configurado_semana

## 1.2.2.3 gerenciador_faltas + primeira_vez + afirmar_uso + grade_atualizada + relatorio_mensal
> check_gerenciador_faltas_primeira_vez_afirmar_uso_perguntar_freq_relatorio
* frequencia_relatorio_mes
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "mes"}
  - utter_configurado_mes

## 2. gerenciador_faltas + uso_confirmado
* gerenciador_faltas
  - slot{"gerenciador_faltas_status": "uso_confirmado"}
  - utter_gerenciador_faltas
> gerenciador_faltas_uso_confirmado

## 2.1 gerenciador_faltas + uso_confirmado + grade_nao_enviada
> gerenciador_faltas_uso_confirmado
* grade_nao_enviada
  - action_checar_grade
  - slot{"grade_status": "grade_nao_enviada"}
  - utter_ask_grade
  - utter_guia_enviar_grade

## 2.2 gerenciador_faltas + uso_confirmado + grade_desatualizada
> gerenciador_faltas_uso_confirmado
* grade_desatualizada
  - action_checar_grade
  - slot{"grade_status": "grade_desatualizada"}
  - utter_grade_desatualizada
  - utter_guia_enviar_grade

## 2.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_nao_configurado
> gerenciador_faltas_uso_confirmado
* grade_atualizada
  - action_checar_grade
  - slot{"grade_status": "grade_atualizada"}
  - utter_tudo_certo
  - utter_configurar_relatorio
  - utter_ask_frequencia_relatorio
> check_gerenciador_faltas_uso_confirmado_grade_atualizada_perguntar_freq_relatorio

## 2.3.1 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_diario
> check_gerenciador_faltas_uso_confirmado_grade_atualizada_perguntar_freq_relatorio
* frequencia_relatorio_dia
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "dia"}
  - utter_configurado_dia

## 2.3.2 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_semanal
> check_gerenciador_faltas_uso_confirmado_grade_atualizada_perguntar_freq_relatorio
* frequencia_relatorio_semana
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "semana"}
  - utter_configurado_semana

## 2.3.3 gerenciador_faltas + uso_confirmado + grade_atualizada + relatorio_mensal
> check_gerenciador_faltas_uso_confirmado_grade_atualizada_perguntar_freq_relatorio
* frequencia_relatorio_mes
  - action_configurar_relatorio
  - slot{"frequencia_relatorio": "mes"}
  - utter_configurado_mes

