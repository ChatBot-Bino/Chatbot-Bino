FROM botrequirements

COPY ./bot /bot

WORKDIR /bot

RUN make train
