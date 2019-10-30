build-bot:
	docker build . -f docker/requirements.Dockerfile -t lappis/botrequirements:boilerplate
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