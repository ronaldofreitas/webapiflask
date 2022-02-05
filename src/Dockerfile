FROM python:3.9.10

EXPOSE 5000

# local
#COPY requirements.txt . 

# jenkins gke
COPY ./src/requirements.txt .

#COPY ./src/gunicorn_starter.sh .

RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

#ENTRYPOINT ["./gunicorn_starter.sh"]
CMD gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:5000
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "-c", "config.py", "app:app"]