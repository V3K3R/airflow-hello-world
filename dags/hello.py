from datetime import timedelta, datetime
from airflow.decorators import dag, task


@dag(
    schedule=timedelta(minutes=5),
    start_date=datetime.now(),
    tags=["test"],
)
def hello_dag():
    @task()
    def hello_world():
        print("Hello World!")

    hello_world()


hello_dag()
