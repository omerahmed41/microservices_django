reload:
	make stop; make run

run:
	docker-compose up

run-d:
	docker-compose up -d; docker-compose exec    notification_service  python3 utils/consumer.py

stop:
	docker-compose down

clean:
	docker-compose down --remove-orphans --volumes

setup:
	make build; make run-d; make makemigrations; make migrate;  make create_superuser; make logs_web

build:
	docker-compose build
	
migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

create_superuser:
	docker-compose exec web python manage.py createsuperuser

test:
	docker-compose exec -T web  python manage.py test  --keepdb

format_with_black:
	black .

flake8:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude venv; flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude venv

sort_imports:
	isort .; isort --check --diff .

checks:
	make format_with_black; make flake8; make sort_imports; make test
logs_web:
	docker-compose logs web --tail 10 --follow

grep:
	docker-compose logs web --follow | grep -i $(keyword)




