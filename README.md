# Spotify to AWS ETL Pipeline

## Overview
This project consists of an ETL pipeline designed to extract data from the Spotify Global Top 50 playlist, transform it using Apache Airflow and AWS Glue, and store it in Amazon Redshift for analytics.

## Technologies Used
- **Data Extraction**: Spotify API for data retrieval.
- **Orchestration**: Apache Airflow for managing and scheduling the ETL workflow.
- **Containerization**: Docker and Docker Compose for environment management.
- **Data Transformation**: AWS Glue for transforming the data before loading it into Redshift.
- **Data Storage**: Amazon S3 for staging data and Amazon Redshift for final storage and analysis.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/jradziejewski/spotify_aws.git
   ```
2. Navigate to the project directory:
   ```bash
   cd spotify_aws
   ```
3. Obtain your API keys for Spotify & AWS and store them in `config/config.conf`:
    ```bash
    mkdir config
    touch config/config.conf
    ```
5. Build and run the Docker container:
   ```bash
   docker-compose up
   ```
