FROM botrequirements

WORKDIR /bot

COPY ./bot /bot

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
