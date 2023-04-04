FROM python:3.9-alpine

WORKDIR /app
COPY . /app

RUN python -m virtualenv v1
RUN source v1/bin/activate
RUN python -m pip install -r requirements.txt

CMD ['flask', '--app', 'app', 'run']
