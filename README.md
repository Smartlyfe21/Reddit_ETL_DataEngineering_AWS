# Reddit ETL Data Engineering on AWS

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.7-orange)](https://airflow.apache.org/)
[![AWS](https://img.shields.io/badge/AWS-S3%2C%20IAM%2C%20EC2%2C%20Glue%2C%20CloudWatch-lightgrey)](https://aws.amazon.com/)

---

## Overview

This repository contains a complete **end-to-end ETL pipeline** that extracts Reddit posts, processes the data, and stores it in **AWS S3**, orchestrated using **Apache Airflow**. The project is built for **real-world scalable deployment** and integrates fully with AWS services.

**Key Features:**
- Extracts Reddit posts using **PRAW** (Python Reddit API Wrapper)
- ETL pipeline for transforming and cleaning Reddit data
- Uploads processed data to **AWS S3**
- Uses **Airflow DAGs** for scheduling and orchestration
- Dockerized environment for easy deployment
- Full integration with **AWS services**: S3, IAM, EC2, Glue Crawlers, CloudWatch
- Configurable via a single `config.conf` file

---

## Repository Structure

RedditDataEngineering/
├── dags/
│ ├── etl_reddit_pipeline.py
│ ├── reddit_dag.py
│ ├── reddit_extraction.py
│ └── utils/constants.py
├── etls/
│ ├── aws_etl.py
│ └── reddit_etl.py
├── pipelines/
│ ├── aws_s3_pipeline.py
│ └── reddit_pipeline.py
├── data/
│ ├── input/
│ └── output/
├── config/
│ └── config.conf # Excluded in .gitignore (contains secrets)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md


**Note:** Sensitive files like `config/config.conf`, `.venv/`, `logs/`, `__pycache__/`, and output data are excluded via `.gitignore`.


     +-----------------+
     |   Reddit API    |
     |   (PRAW)        |
     +--------+--------+
              |
              v
     +-----------------+
     |   ETL Scripts   |
     |  (Extraction,   |
     |  Transformation,|
     |  Loading)       |
     +--------+--------+
              |
              v
     +-----------------+
     |   AWS S3 Bucket |
     |  (Processed CSV)|
     +--------+--------+
              |
              v
     +-----------------+
     | Apache Airflow  |
     |   DAG Scheduler |
     +-----------------+


**Explanation:**
- Reddit API fetches posts using PRAW  
- ETL scripts clean, transform, and prepare the data  
- Data is uploaded to AWS S3 bucket  
- Airflow orchestrates, schedules, and monitors the ETL pipeline  

## Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/Smartlyfe21/Reddit_ETL_DataEngineering_AWS.git
cd Reddit_ETL_DataEngineering_AWS

---

## Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/Smartlyfe21/Reddit_ETL_DataEngineering_AWS.git
cd Reddit_ETL_DataEngineering_AWS


Setup Virtual Environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


Configure AWS and API Keys
Update config/config.conf with your credentials
[aws]
aws_region = YOUR_AWS_REGION
aws_access_key_id = YOUR_AWS_ACCESS_KEY
aws_secret_access_key = YOUR_AWS_SECRET_KEY
s3_bucket_name = s3-reddit-etl-data-engineering

[api_keys]
CLIENT_ID = YOUR_REDDIT_CLIENT_ID
SECRET = YOUR_REDDIT_SECRET

[database]
database_host = localhost
database_port = 5432
database_username = airflow
database_password = airflow
db_name = airflow

[file_paths]
input_data_path = ./data/input
output_data_path = ./data/output
logs_path = ./logs

[etl_settings]
schedule_interval = 0 0 * * *
batch_size = 100
max_retries = 3
retry_delay_minutes = 5
log_level = INFO


AWS Setup (Fully Automated via Code)
IAM User or Role
Create an IAM user with programmatic access
Attach S3FullAccess policy (or minimal policy for your bucket)
Copy Access Key ID and Secret Key into config.conf
S3 Bucket
Create a bucket (name matches s3_bucket_name in config.conf)
Ensure correct permissions for IAM user
Optional AWS Tools
CloudWatch for logging/monitoring
Glue Crawler for schema discovery (if extending pipeline)
EC2 to run Airflow/Docker in cloud (if not local)
Running the Project

## Visual Pipeline Diagram

```mermaid
flowchart TD
    A[Reddit API (PRAW)] --> B[Extract & Transform (ETL Scripts)]
    B --> C[Local CSV Storage (data/output/)]
    C --> D[AWS S3 Bucket]
    D --> E[Airflow DAGs Orchestration & Scheduling]
    E --> F[Monitoring & Logging]


1. Start Docker Compose
docker-compose up -d

2. Access Airflow Web UI
Open your browser: http://localhost:8080
DAGs are available under Reddit ETL Pipeline
Trigger manually or wait for scheduled runs
3. Monitor Logs & Output
Processed CSVs saved to data/output/
Automatically uploaded to your AWS S3 bucket
Python Dependencies
pandas – data manipulation
boto3 – AWS S3 integration
praw – Reddit API
apache-airflow – workflow orchestration
python-dotenv – environment variable management
Install all dependencies:
pip install -r requirements.txt

License
MIT License
