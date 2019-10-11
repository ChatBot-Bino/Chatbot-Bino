# Chatbot - Bino
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>

# O bot

O Bino foi criado com o propósito de ajudar os alunos da Universidade de Brasília - Campus Gama(FGA) para gerenciar faltas e atividades acadêmicas, como provas e trabalhos.

# Entenda a Arquitetura
<img src="https://i.imgur.com/zpn7hFT.png" alt="drawing" width="1000"/>

O usuário interage com o Chatbot Bino via Telegram,  que manda as mensagens para o Rasa NLU e através do *Bot model*, ele identifica a *intent* do usuário, e responde pelo Rasa Core a determinada mensagem, de acordo com as *stories* e *actions*.  
As *models* utilizadas para a conversação foram geradas pela junção e treinamento dos arquivos <i>domain.yml</i>, *stories* e *intents* depois transferidas para o bot na forma do *Bot Model*, estes
modelos podem ser versionados e evoluídos entre bots.  

### Telegram

1. Trocar as variaveis de acesso do telegram.
        1.1. no arquivo Rasa/credentials.yml.
2. Executar o comando ./ngrok http 5005 para conseguir um endereço https.
3. Trocar o endereço
    3.1. webhook_url:endereço_https/webhooks/telegram/webhook
4. Desse modo o seu arquivo credentials.yml deve ficar assim:
```yml
 telegram:
  access_token: "Token gerado pelo bot father"
  verify: "Usuario do seu bot"
  webhook_url: "https://endereço_https/webhooks/telegram/webhook"
```

<strong><em>Antes de seguir adiante. Importante:</strong></em> As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.

Se ainda não tiver treinado seu bot execute antes:

```sh
docker run -v $(pwd):/app rasa/rasa:latest-full train --domain ./Rasa/domain.yml --data ./Rasa/data --out ./Rasa/models --config ./Rasa/config.yml
``` 
**Atenção**: Necessario possuir o docker.  

Depois dê up o bot para telegram:

```sh
sudo docker-compose up
```

### Console

Se ainda não tiver treinado seu bot execute antes:
```sh
docker run -v $(pwd):/app rasa/rasa:latest-full train --domain ./Rasa/domain.yml --data ./Rasa/data --out ./Rasa/models --config ./Rasa/config.yml
``` 

Depois execute o bot pelo shell:
```sh
docker run -it -v $(pwd):/app rasa/rasa shell --m ./Rasa/models --endpoints ./Rasa/endpoints.yml
```

# Licença

[GPL3](https://github.com/ChatBot-Bino/Chatbot-Bino/blob/master/LICENSE)
