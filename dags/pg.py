from datetime import timedelta, datetime
from airflow.decorators import dag, task
from airflow.providers.postgres.operators.postgres import PostgresOperator

DB_URL = "postgresql+psycopg2://airflow:airflow@postgres/airflow"


@dag(
    schedule=timedelta(minutes=5),
    start_date=datetime.now(),
    tags=["test"],
)
def pg_dag():
    @task()
    def create_table():
        create_pet_table = PostgresOperator(
            task_id="create_pet_table",
            sql="""
                CREATE TABLE IF NOT EXISTS pet (
                pet_id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                pet_type VARCHAR NOT NULL,
                birth_date DATE NOT NULL,
                OWNER VARCHAR NOT NULL);
            """,
        )

    @task()
    def populate_table():
        populate_pet_table = PostgresOperator(
            task_id="populate_pet_table",
            sql="""
                INSERT INTO pet (name, pet_type, birth_date, OWNER)
                VALUES ( 'Max', 'Dog', '2018-07-05', 'Jane');
                """,
        )

    @task()
    def get_pets():
        get_all_pets = PostgresOperator(
            task_id="get_all_pets", sql="SELECT * FROM pet;"
        )

    create_table()
    populate_table()
    get_pets()


pg_dag()
