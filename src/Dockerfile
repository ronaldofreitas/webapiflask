FROM python:3.9.10

EXPOSE 5000

# local
#COPY requirements.txt . 

# jenkins gke
COPY ./src/requirements.txt .
COPY ./src/gunicorn_config.py .

RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

#RUN chmod +x gunicorn_starter.sh
#ENTRYPOINT ["sh", "gunicorn_starter.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]

#ENTRYPOINT ["./gunicorn_starter.sh"]
#CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "-c", "config.py", "app:app"]