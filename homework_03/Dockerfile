FROM python:3.9-buster

WORKDIR /var/app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

#CMD uvicorn main:app --host=0.0.0.0

#docker build . -t blog
#docker run -p 8000:8000 blog
