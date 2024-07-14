# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy the dependency files
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy the rest of the application code
COPY ./app /code/app

# Set the working directory for the app
WORKDIR /code/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
