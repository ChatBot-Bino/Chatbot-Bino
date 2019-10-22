# train:
# 	docker run \
# 	-v "$(pwd)":/app \
# 	rasa/rasa:latest-full \
# 	train \
# 		--domain ./Rasa/domain.yml \
# 		--data ./Rasa/data \
# 		--out ./Rasa/models \
# 		--c ./Rasa/config.yml

build-bot:
	./docker/build-base.sh
	make train

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

run-telegram:
	docker-compose up bot_telegram

run-console:
	docker-compose run bot make run-console

test-dialogue:
	docker-compose run --rm bot make e2e