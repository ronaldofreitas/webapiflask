FROM python:3.9.10

EXPOSE 5000

# local
#COPY requirements.txt . 

# jenkins gke
COPY ./src/requirements.txt .

RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app

ENV PORT 5000
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 src.app:app