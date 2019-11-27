## Start
* start{"command":"start"}
    - action_start
    - utter_start

## adicionar_atividade
* adicionar_atividade{"command":"adicionar_atividade"}
    - utter_atividades_tipo
    - action_listen
    - action_adicionar
    - utter_adicionarData
    - action_listen
    - action_adicionarData
    - utter_adicionarOBS
    - action_listen
    - action_adicionarOBS

## Help
* help{"command":"help"}
    - utter_help

## listar
* listar{"command":"listar"}
    - action_listarAtv

## remover_atividade
* remover_atividade{"command":"remover_atividade"}
    - action_listar2rm
    - action_listen
    - action_salvarNomeAtv2rm
    - action_listen
    - action_salvarDataAtv2rm
    - action_removerAtv

## modificar_atividade
* modificar_atividade{"command":"modificar_atividade"}
    - action_listar2ModAtv
    - action_listen
    - action_salvarNomeAtv
    - action_listen
    - action_salvarDataAtv
    - action_listen
    - action_salvarOqMod
    - action_listen
    - action_salvarNewInfoMod
