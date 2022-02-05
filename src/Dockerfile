FROM python:3.9.10

EXPOSE 5000
WORKDIR /app
# local
#COPY requirements.txt . 

# jenkins gke
COPY ./src/requirements.txt .
#COPY ./src/gunicorn_config.py .

RUN pip install -r requirements.txt

COPY . /app
#WORKDIR /app

ENV PORT 5000
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app