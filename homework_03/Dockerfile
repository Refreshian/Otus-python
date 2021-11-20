FROM python:3.9-buster

WORKDIR /var/app

COPY ./blog/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY blog .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

#CMD uvicorn main:app --host=0.0.0.0