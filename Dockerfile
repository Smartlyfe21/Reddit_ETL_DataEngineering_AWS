# Use Apache Airflow version 2.7.1 as base
FROM apache/airflow:2.7.1

# Copy requirements.txt into the container
COPY requirements.txt /opt/airflow/requirements.txt

# Switch to root to install system dependencies
USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    wget \
    curl \
    nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Install only extra dependencies (NOT airflow itself)
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
