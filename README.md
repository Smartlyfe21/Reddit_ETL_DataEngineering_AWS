# 🟥 Reddit ETL Data Engineering on AWS ☁️

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.7-orange)](https://airflow.apache.org/)
[![AWS](https://img.shields.io/badge/AWS-S3%2C%20IAM%2C%20EC2-lightgrey)](https://aws.amazon.com/)

Python • Airflow • AWS • Reddit

---

## 🔹 Overview

This repository contains a complete end-to-end ETL pipeline that extracts Reddit posts, processes the data, and stores it in AWS S3, orchestrated using Apache Airflow. The project is designed for **real-world scalable deployment** and integrates fully with AWS services.

---

## 🔹 Key Features

- 📝 Extracts Reddit posts using PRAW (Python Reddit API Wrapper)  
- 🔄 ETL pipeline for transforming and cleaning Reddit data  
- ☁️ Uploads processed data to AWS S3  
- ⏱️ Uses Airflow DAGs for scheduling and orchestration  
- 🐳 Dockerized environment for easy deployment  
- 🔐 Full integration with AWS services: S3, IAM, EC2, Glue Crawlers, CloudWatch  
- ⚙️ Configurable via a single `config.conf` file  

---

## 📂 Repository Structure

RedditDataEngineering/
├── dags/ Airflow DAGs and ETL scripts
│ ├── etl_reddit_pipeline.py
│ ├── reddit_dag.py
│ ├── reddit_extraction.py
│ └── utils/constants.py
├── etls/ AWS ETL scripts
│ ├── aws_etl.py
│ └── reddit_etl.py
├── pipelines/ Modular pipelines
│ ├── aws_s3_pipeline.py
│ └── reddit_pipeline.py
├── data/ Input/output data
│ ├── input/
│ └── output/
├── config/ Configuration
│ └── config.conf # Excluded in .gitignore (contains secrets)
├── Dockerfile Docker setup
├── docker-compose.yml Docker Compose for Airflow
├── requirements.txt Python dependencies
├── .gitignore
└── README.md

**Note:** Sensitive files like `config/config.conf`, `.venv/`, `logs/`, `__pycache__/`, and `data/output/` are excluded via `.gitignore`.

---

## 🚀 Visual Pipeline Diagram

+-----------------+
| Reddit API |
| (PRAW) |
+--------+--------+
|
v
+-----------------+
| ETL Scripts |
| (Extraction, |
| Transformation,|
| Loading) |
+--------+--------+
|
v
+-----------------+
| AWS S3 Bucket |
| (Processed CSV)|
+--------+--------+
|
v
+-----------------+
| Apache Airflow |
| DAG Scheduler |
+-----------------+

**Explanation:**

- 🟥 Reddit API fetches posts using PRAW  
- 🔄 ETL scripts clean, transform, and prepare the data  
- ☁️ Data is uploaded to AWS S3 bucket  
- ⏱️ Airflow orchestrates, schedules, and monitors the ETL pipeline  

---

## 🐳 Running the Project

1. **Start Docker Compose**
```bash
docker-compose up -d

Access Airflow Web UI
Open your browser: http://localhost:8080
DAGs are available under Reddit ETL Pipeline
Trigger manually or wait for scheduled runs
Monitor Logs & Output
Processed CSVs saved to data/output/
Automatically uploaded to your AWS S3 bucket

📦 Python Dependencies
pandas – Data manipulation
boto3 – AWS S3 integration
praw – Reddit API
apache-airflow – Workflow orchestration
python-dotenv – Environment variable management
Install all dependencies:
pip install -r requirements.txt

📝 License
MIT License
