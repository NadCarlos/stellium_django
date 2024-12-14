build:
	sudo docker-compose build

up:
	sudo docker-compose up

up-d:
	docker compose up -d

down:
	docker compose down

prod-up:
	docker compose -f docker-compose-prod.yaml up --build -d

prod-down:
	docker compose -f docker-compose-prod.yaml down

prod-restart:
	docker compose -f docker-compose-prod.yaml restart

run:
	docker compose build && docker compose up

down-v:
	docker compose down -v

migrate:
	sudo docker-compose run web python stellium/manage.py migrate

makemigrations:
	sudo docker-compose run web python stellium/manage.py makemigrations

create-superuser:
	sudo docker-compose run web python stellium/manage.py createsuperuser

shell:
	docker compose run web python manage.py shell

bash:
	sudo docker exec -it stellium_web bash

logs-web:
	docker logs gym_web

backup:
	docker compose exec web python gym/manage.py dbbackup

restore:
	docker compose exec web python gym/manage.py dbrestore -i "$(file)"

load:
	docker compose exec web ./load_db_to_docker_mysql.sh $(file)

dump:
	docker compose exec web ./dump_db_from_docker.sh 