current_dir := $(shell pwd)

clean:
	sudo docker-compose down

############################## BOILERPLATE ############################## 
build:
	make build-requirements
	make build-coach
	make build-bot

build-requirements:
	docker build . -f docker/requirements.Dockerfile -t botrequirements

build-bot:
	docker-compose build bot
	
build-coach:
	docker-compose build coach

run-console:
	docker-compose run --rm --service-ports bot make shell


run-telegram:
	docker-compose run -d --rm --service-ports bot_telegram make telegram

train:
	docker-compose up coach
	docker-compose build bot

visualize:
	docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain domain.yml --stories data/stories.md --config config.yml --nlu data/nlu.md --out ./graph.html -vv
	sensible-browser --no-sandbox bot/graph.html
