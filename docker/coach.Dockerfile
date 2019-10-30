FROM lappis/botrequirements:boilerplate

COPY ./Rasa/ /Rasa

WORKDIR /Rasa

RUN make train
