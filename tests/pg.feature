Feature: testing Airflow and PG

    Scenario: run a simple test
        Given we have airflow running
        And we have postgres running
        When we run the following dag: "pg_dag"
        Then we expect the following
            | name | pet_type | birth_date | owner |
            | Max  | Dog      | 2018-07-05 | Jane  |
