init:
	docker compose up airflow-init

bootstrap:
	docker compose up

cleanup:
	docker compose down --volumes --remove-orphans
