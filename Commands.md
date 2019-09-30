#Treinar o bot
docker run -v $(pwd):/app rasa/rasa:latest-full train --domain ./Rasa/domain.yml --data ./Rasa/data --out ./Rasa/models --config ./Rasa/config.yml

#Iniciar o webhook
./ngrok http 5005

#Subir o bot
docker-compose up

