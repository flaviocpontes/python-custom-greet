FROM python:3.11-alpine

EXPOSE 8000

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0", "--log-config", "logging.ini", "main:app"]