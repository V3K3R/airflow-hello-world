from behave import given, when, then
import requests

AIRFLOW_URL = "http://localhost:8080"


@given("we have airflow running")
def step_impl(context):
    res = requests.get(f"{AIRFLOW_URL}/health", auth=("airflow", "airflow"))
    assert res.status_code == 200
    assert res.json()["metadatabase"] == {"status": "healthy"}

@when('we run the following dag: "dag"')
def step_impl(context, dag):
    pass

@given("we expect the following")
def step_impl(context):
    pass
