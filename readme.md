# Jobs Dashboard Project

## Overview

The Jobs Dashboard Project is a comprehensive system that allows users to manage job listings, companies, locations, and associated metadata. It is built using a PostgreSQL database, FastAPI for the backend, and Streamlit for the frontend. The database is managed using pgAdmin.

The project uses Poetry for dependency management and Asynchronous SQLAlchemy with Pydantic for data validation. Database schemas are created using SQLAlchemy ORM. Initial data is populated in the database using lifecycle events on the startup of the FastAPI app. Streamlit is used to create a dynamic dashboard to analyze data of the posted jobs from the database.

## Architecture

### Database Entity Diagram
![Database Entity Diagram](https://github.com/nickTheof/jobs-dashboard-project/blob/main/images/database%20entity%20diagram.png)

### Microservices Architecture
![Microservices Architecture](https://github.com/nickTheof/jobs-dashboard-project/blob/main/images/microservices%20architecture.jpg)

## Components

### Database
- **PostgreSQL**: The database is used to store all job-related data, including companies, locations, job titles, and skills.
- **pgAdmin**: A web-based database management tool to manage and monitor the PostgreSQL database.

### Backend
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It handles asynchronous SQL operations using SQLAlchemy.
- **SQLAlchemy ORM**: Used to create and manage database schemas.
- **Pydantic**: Used for data validation.
- **Poetry**: Used for managing project dependencies.
- **Lifecycle Events**: Used to populate initial data into the database at the startup of the FastAPI app.

### Frontend
- **Streamlit**: An open-source app framework for Machine Learning and Data Science teams. It handles HTTP requests and interacts with the FastAPI backend to present data to the user.

## Database Schema

The database schema consists of the following tables:
- **industries**: Stores industry information.
- **shortjobtitles**: Stores short job title information.
- **worklocationtypes**: Stores work location type information.
- **jobscheduletypes**: Stores job schedule type information.
- **cities**: Stores city information.
- **countries**: Stores country information.
- **companies**: Stores company information.
- **jobs**: Stores job information.
- **skills**: Stores skill information.
- **shortjobtitleindustrieslinktable**: Links short job titles to industries.
- **jobskillslinktable**: Links jobs to skills.
- **salaries**: Stores salary information.
- **continents**: Stores continent information.

## How to Run

### Prerequisites

Ensure you have the following software installed:
- Docker
- Docker Compose

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nickTheof/jobs-dashboard-project
    cd jobs-dashboard-project
    ```

2. **Set up environment variables**:
    Create a `.env` file in the root directory and add the necessary environment variables.
    ```env
# FastAPI Backend
BACKEND_SERVICE_NAME=backend
BACKEND_PORT=8000
# Postgres - BACKEND
POSTGRES_SERVICE_NAME=database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_DB=test
POSTGRES_SERVER=local
POSTGRES_PORT=5448
POSTGRES_HOST=localhost
# PG Admin
PGADMIN_PORT=8086
PGADMIN_DEFAULT_EMAIL='admin@test.com'
PGADMIN_DEFAULT_PASSWORD=admintest
PGADMIN_DEFAULT_PASSWORD_FILE=admin
    ```

3. **Build the images**:
    Use Docker Compose to build all images of the services.
    ```bash
    docker-compose build
    ```

4. **Start the services**:
    Use Docker Compose to start all services.
    ```bash
    docker-compose up -d
    ```

5. **Access the application**:
    - **Streamlit (Frontend)**: [http://localhost:8501](http://localhost:8501)
    - **FastAPI (Backend)**: [http://localhost:8000](http://localhost:8000)
    - **pgAdmin**: [http://localhost:8086](http://localhost:8086)

## API Endpoints

The FastAPI backend provides various endpoints to interact with the data. You can access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/nickTheof/jobs-dashboard-project/blob/main/licence.txt) file for details.