# Data Ingestion Pipeline

## Overview

This repository provides a comprehensive data ingestion pipeline designed to handle user metrics streams. The pipeline ingests and stores metrics data into a MySQL database. The data includes metrics types such as `talked_time`, `microphone_used`, `speaker_used`, and `voice_sentiment`, each with additional fields for detailed analysis.

The solution is containerized using Docker, with two primary containers:
1. **Application Container**: Runs the data ingestion application.
2. **Database Container**: Hosts a MySQL database.

### Features
- Efficient data ingestion from simulated user metrics.
- Data is persisted in a MySQL database.
- Docker Compose orchestrates the containers, simplifying management and deployment.

## Project Structure

  - `app.py`: Python script to generate and insert random data into the database.
  - `requirements.txt`: Lists the Python dependencies.
  - `Dockerfile`: Dockerfile to build the application image.
  - `user_metrics_db.sql`: SQL script to set up the database schema.
  - `docker-compose.yml`: Docker Compose configuration file.
  - `README.md`: This documentation file.

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Pipeline

### Clone the Repository
To get started, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-repository-url.git
cd your-repository-folder
```

### Verify   Setup
To verify that everything is set up correctly:

Check that both containers are running:
docker ps


Access the application logs to ensure there are no errors:
docker logs data_ingestion_app


Verify that data is being inserted into the MySQL database. You can connect to the MySQL container and check the tables:
docker exec -it data_ingestion_db mysql -u root -pexamplepassword user_metrics
SHOW TABLES;

## Extending the Pipeline

To extend the pipeline:

1. **Add New Metrics**: Update `app.py` to include new metric types and adjust the database schema accordingly.

2. **Performance Optimization**: Consider indexing additional fields or partitioning tables based on the volume of data.

3. **Error Handling**: Implement error handling and logging for better reliability.

## Assumptions and Limitations

### Assumptions

- The environment variables are correctly set in the Docker Compose file.
- The MySQL database is configured correctly with default settings.

### Limitations

- The application currently generates random data for simulation purposes.
- The schema and indices are basic and might need optimization for large-scale production use.

## Future Improvements

1. **Enhanced Data Validation**: Implement data validation to ensure integrity.

2. **Real-Time Data Processing**: Integrate a real-time data processing framework.

3. **Monitoring and Alerts**: Set up monitoring and alerts for the pipeline and database
