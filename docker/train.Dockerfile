FROM rasa/rasa:latest-full

COPY ./Rasa .

RUN train --domain domain.yml --data data --out models --config config.yml