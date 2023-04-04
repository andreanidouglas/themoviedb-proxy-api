FROM python:3.9-bullseye

WORKDIR /app
EXPOSE 5000

ENV VIRTUAL_ENV=/app/venv
RUN python3 -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY app.py .
COPY domain domain
COPY data data 
COPY config config

CMD ["flask", "--app", "app", "run", "--host", "0.0.0.0"]
