
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
<ol>     
  <li>Baixar o ngrok para poder abrir o link localhost:5001 para o telegram poder usar.
      <ul type="none">
          <li>https://ngrok.com/download</li>
      </ul>
  </li>
  <li>Executar o comando ./ngrok http 5001 para conseguir um endereço https.</li>
  <li>Trocar as variáveis de acesso do telegram.
      <ul type="none">
           <li>No arquivo env/bot-telegram.env:
               <ol>
                    <li>Trocar o endereço
                            <p>TELEGRAM_WEBHOOK: endereço_https/webhooks/telegram/webhook</p>
                    </li>
                    <li>Copiar e colocar o Token gerado pelo bot father.
                            <p>TELEGRAM_TOKEN: Token gerado pelo bot father</p>
                    </li>
                    <li>Inserir o nome do seu bot
                            <p>TELEGRAM_BOT_USERNAME: "Usuario do seu bot"</li>
                    </li>
               </ol>
           </li>
        </ul>
   </li>
   <li> Desse modo o seu arquivo bot-telegram.env deve ficar assim: 
         
        TELEGRAM_BOT_USERNAME=nome do bot
        TELEGRAM_TOKEN=Link Gerado pelo bot father
        TELEGRAM_WEBHOOK=linkHTTPSdoNgrok/webhooks/telegram/webhook"      
   </li>
</ol>

<strong><em>Antes de seguir adiante. Importante:</strong></em> As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.
### Telegram
Para executar o bot no telegram tenha certeza que foi feito o passo anterior e depois execute o comando:

```sh
sudo make bot-telegram
```
Esse comando vai checar as dependências do bot, treinar o bot e deixar ele online para o telegram.

### Console

```sh
sudo make bot-shell
```
Esse comando vai checar as dependências do bot, treinar o bot e executar o bot no terminal.

### Licença

[GPL3](https://github.com/ChatBot-Bino/Chatbot-Bino/blob/master/LICENSE)
