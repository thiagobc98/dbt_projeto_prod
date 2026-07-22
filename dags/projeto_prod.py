from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
import os

DBT_PROJECT_DIR = os.path.join(os.path.dirname(__file__), "dbt", "projeto_prod")

my_dbt_dag = DbtDag(
    project_config=ProjectConfig(DBT_PROJECT_DIR),
    profile_config=ProfileConfig(profile_name="projeto_prod", target_name="dev", profiles_yml_filepath=os.path.join(DBT_PROJECT_DIR, "profiles.yml")),
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    ),
    schedule_interval="@daily",
    start_date=datetime(2026, 7, 22),
    catchup=False,
    dag_id="projeto_prod"
    
)
