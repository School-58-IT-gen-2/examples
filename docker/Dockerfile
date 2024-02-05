FROM python:3.12-slim

COPY main.py ./main.py
COPY requirements.txt ./requirements.txt
COPY .env ./.env

RUN pip install -r requirements.txt

# CMD python main.py