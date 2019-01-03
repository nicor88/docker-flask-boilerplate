FROM python:3.6-slim

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

WORKDIR /app

CMD exec gunicorn app:app --bind 0.0.0.0:8000 --workers 4
