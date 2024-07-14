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

# Expose the port that Streamlit runs on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
