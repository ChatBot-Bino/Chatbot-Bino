train:
	docker run \
	-v "$(pwd)":/app \
	rasa/rasa:latest-full \
	train \
		--domain ./Rasa/domain.yml \
		--data ./Rasa/data \
		--out ./Rasa/models \
		--c ./Rasa/config.yml