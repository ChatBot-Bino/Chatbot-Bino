# Gerenciador de Faltas

## 1. Requisitos

### Objetivo

O ChatBot Bino tem como objetivo otimizar o tempo do universitário, aumentando a facilidade do mesmo em organizar seus horários. Através do controle de faltas nas disciplinas nas quais o aluno está matriculado, o aluno será notificado de acordo com o limite permitido por cada matéria.

### Razão
Evitar reprovações mantendo o controle sobre as faltas do usuário.

### Tecnologias

- Python 3

## 2. Arquitetura

### 1. *Input*

#### Grade horária
A entrada inicial de dados será principalmente pelo arquivo PDF, obtido no Matrícula Web e enviado pelo usuário, contendo sua grade horária de disciplinas. Ele também poderá ser enviado manualmente (digitado), como segunda opção.

#### Verificação de presença

- O bot saberá se o usuário compareceu ou não às aulas através dos botões "sim" e "não" mostrados no chat do Telegram.

 - Eles ficarão disponíveis a partir do início da aula (para evitar falsa confirmação) até o fim do dia.

 - O valor padrão, para caso não haja resposta, será de presença, visto que é necessário três vezes mais presenças do que faltas para a aprovação em uma disciplina.

- Haverá relatórios periódicos sobre as presenças para que o usuário não se perca, caso tenha esquecido de marcar alguma falta.

- Será possível alterar a presença em uma aula sempre que desejado.

### 2. Processamento
O bot ficará responsável por:

- Armazenar todas as presenças e faltas;
- Calcular o limite de faltas com base na quantidade de créditos de cada disciplina;
- Calcular o percentual de comparecimento;
- Gerar relatórios de presença;
- Alertar e prevenir as faltas.

### 3. *Output*
A saída de dados do gerenciador de faltas será através de mensagens, alertas e notificações. notificações.

## 3. Linha do tempo

### 1. Leitor de PDF
Para melhorar a usabilidade, basta que o usuário envie sua grade horária em formato PDF, obtida no Matrícula Web, no chat do bot. O Bino ficará responsável por extrair todos os dados presentes no documento. É necessário escolher entre as várias ferramentas e bibliotecas em Pyhton a que melhor se encaixa para o nosso uso.

### 2. Armazenamento de dados

Para o armazenamento, vamos utilizar o banco de dados MongoDB.

### 3. Comunicação

#### Notificações

O usuário receberá notificações para responder sobre sua presença sempre a partir do horário de início da aula. Também serão enviados alertas para a prevenção de faltas.

### 4. Relatório 

Os relatórios serão periódicos enviados diariamente, semanalmente e/ou mensalmente para que o usuário sempre esteja ciente de seus limites de faltas.