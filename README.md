# Desafio_Leilao

WIP

Create .env file.

docker-compose up --build
(check if needs to install npm or vue@cli)

docker exec -it django_1 bash
python manage.py migrate (check if needed)
python manage.py loaddata initial_data.json (may need a first registered user)

Django: localhost:8000/api
Vue: localhost:8080
