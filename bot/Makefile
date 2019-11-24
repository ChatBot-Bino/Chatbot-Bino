clean:
	rm -rf graph.html results/ models/*

############################## BOT ############################## 
# NLU
train-nlu:
	rasa train nlu -vv 

test-nlu:
	rasa test nlu -vv 

# CORE
train:
	rasa train --domain domain.yml -vv --out models/

# MENSAGEIROS
shell:
	rasa shell -m models/ -vv --endpoints endpoints.yml --enable-api --port 5004 --cors "*"

telegram:
	rasa run -m models/ -vv --port 5001 --credentials credentials.yml \
	--enable-api --endpoints endpoints.yml 

webchat:
	rasa run -m models/ -vv --endpoints endpoints.yml --credentials credentials.yml --port 5005 --cors '*'

run-api:
	rasa run -m models/ -vv --endpoints endpoints.yml --enable-api

# ACTIONS
run-actions:
	rasa run actions --actions actions -vv
# VALIDATE
validate:
	docker-compose run --rm coach rasa data validate --fail-on-warnings --domain domain.yml --data data/ -vv
