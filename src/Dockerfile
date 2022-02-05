FROM python:3.9.10

EXPOSE 5000

# local
#COPY requirements.txt . 

# jenkins gke
COPY ./src/requirements.txt .
#COPY ./src/gunicorn_config.py .

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app


#RUN chmod +x gunicorn_starter.sh
#ENTRYPOINT ["sh", "gunicorn_starter.sh"]

#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
CMD ["/usr/local/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "-t", "30", "--pythonpath", "/app", "app:create_app()"]

#ENTRYPOINT ["./gunicorn_starter.sh"]
#CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "-c", "config.py", "app:app"]