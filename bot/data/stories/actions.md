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
    - action_listar2rmAtv
    - utter_removerAtv_titulo
    - action_listen
    - utter_removerAtv_data
    - action_listen
    - action_removerAtv

## ModificarAtv
* modificar_atividade{"command":"modificarAtv"}
    -
    - utter_modificar_titulo
    - action_listen
    - utter_modificar_data
    - action_listen
    - utter_modificar_oque
    - action_listen
    - utter_modificar_novo
    - action_listen
    - action_modAtv