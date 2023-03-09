import json
from datetime import datetime

import requests
from behave import given, then, when

AIRFLOW_URL = "http://localhost:8080"


@given("we have airflow running")
def step_impl(context):
    res = requests.get(f"{AIRFLOW_URL}/health", auth=("airflow", "airflow"))
    assert res.status_code == 200
    assert res.json()["metadatabase"] == {"status": "healthy"}


@when('we run the following dag: "{dag}"')
def step_impl(context, dag):
    res = requests.post(
        f"{AIRFLOW_URL}/api/v1/dags/{dag}/dagRuns",
        auth=("airflow", "airflow"),
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "dag_run_id": f'dheker_test_{datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}',
            }
        ),
    )
    assert res.status_code == 200


@then("we expect the following")
def step_impl(context):
    pass
