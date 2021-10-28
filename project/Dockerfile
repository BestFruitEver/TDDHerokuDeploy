FROM python:3.9.6-slim-buster

#Set du working directory
WORKDIR /usr/src/app

#Set des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#installation des dépendences systèmes
RUN apt-get update \
    && apt-get install -y netcat gcc \
    && apt-get clean

#installation des dépendances
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#add app
COPY . .

#add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod  +X /usr/src/app/entrypoint.sh

#On lance le entrypoint
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]