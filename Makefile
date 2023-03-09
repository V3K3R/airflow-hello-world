init:
	docker compose up airflow-init -d

bootstrap:
	docker compose up

format:
	pipenv run black .

test:
	pipenv run behave ./tests

cleanup:
	docker compose down --volumes --remove-orphans
