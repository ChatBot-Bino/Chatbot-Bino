FROM botbino/botrequirements

WORKDIR /bot

COPY ./bot/ /bot/

RUN make train
