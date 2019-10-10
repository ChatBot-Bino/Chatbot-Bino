#Treinar o bot
docker run -v $(pwd):/app rasa/rasa:latest-full train --domain ./Rasa/domain.yml --data ./Rasa/data --out ./Rasa/models --config ./Rasa/config.yml

#Iniciar o webhook
./ngrok http 5005

#Testar o bot no shell
docker run -it -v $(pwd):/app rasa/rasa shell --model ./Rasa/models --endpoints ./Rasa/endpoints.yml

#Subir o bot para o telegram
docker-compose up

