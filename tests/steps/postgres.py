from behave import given
import psycopg

DB_CONN = "postgresql://airflow:airflow@localhost:5432/airflow"


@given("we have postgres running")
def step_impl(context):
    with psycopg.connect(DB_CONN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                        SELECT * FROM dag;
                """
            )
