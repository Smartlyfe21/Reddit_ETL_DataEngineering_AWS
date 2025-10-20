from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import praw
import pandas as pd
import os
import configparser

def extract_reddit_data():
    # Read config file
    CONFIG_PATH = "/opt/airflow/config/config.conf"
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(CONFIG_PATH)

    CLIENT_ID = config.get("api_keys", "CLIENT_ID")
    SECRET = config.get("api_keys", "SECRET")
    SUBREDDIT = config.get("etl_settings", "subreddit") if config.has_option("etl_settings", "subreddit") else "dataengineering"

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        user_agent="airflow_reddit_etl"
    )

    subreddit = reddit.subreddit(SUBREDDIT)

    posts = []
    for post in subreddit.hot(limit=20):
        posts.append({
            "id": post.id,
            "title": post.title,
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "url": post.url
        })

    df = pd.DataFrame(posts)

    output_path = "/data/output"
    os.makedirs(output_path, exist_ok=True)

    file_path = os.path.join(
        output_path,
        f"reddit_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )
    df.to_csv(file_path, index=False)
    print(f"DEBUG: Data saved to {file_path}")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="reddit_extraction",
    default_args=default_args,
    description="Extract Reddit posts using PRAW",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["reddit", "etl"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_reddit_posts",
        python_callable=extract_reddit_data,
    )
