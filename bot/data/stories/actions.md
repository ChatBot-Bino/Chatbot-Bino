## Start
* start{"command":"start"}
    - action_start
    - utter_start

## Faltas
* faltas{"command":"faltas"}
    - action_faltas

## Adicionar_Atividade
* adicionar_atividade{"command":"adicionar"}
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

## ListarAtv
* Listar{"command":"listarAtv"}
    - action_listarAtv

## RemoverAtv
* remover_atividade{"command":"removerAtv"}
    - action_listar2rmOrModAtv
    - action_listen
    - action_salvarNomeAtv
    - action_listen
    - action_salvarDataAtv
    - action_listen
    - action_removerAtv

## ModificarAtv
* modificar_atividade{"command":"modificarAtv"}
    - action_listar2rmOrModAtv
    - action_listen
    - action_salvarNomeAtv
    - action_listen
    - action_salvarDataAtv
    - action_listen
    - action_salvarOqMod
    - action_listen
    - action_salvarNewInfoMod
    - action_modAtv
