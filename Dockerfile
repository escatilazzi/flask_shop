FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update -y
RUN apt-get install tk -y
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
