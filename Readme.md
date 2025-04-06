# FastAPI Docker Project

This project provides a template for deploying a FastAPI application using Docker. It includes configurations for building and running the application in a containerized environment.

## Features

- **FastAPI Application**: A simple FastAPI app with a basic endpoint.
- **Docker Integration**: Dockerfile and docker-compose configurations for containerization.
- **Environment Variables**: Support for environment variables to configure the application.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/awaismughal2020/fastapi-docker.git
   cd fastapi-docker
   ```

2. **Build and Run the Application**:

   Use Docker Compose to build and run the application:

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker image and starts the FastAPI application.

3. **Access the Application**:

   Once the container is running, access the application at `http://localhost:8000`.

4. **Interactive API Documentation**:

   FastAPI provides interactive API documentation using Swagger UI. Access it at `http://localhost:8000/docs`.

## Project Structure

```
fastapi-docker/
├── app/
│   ├── main.py
│   └── ...
├── Dockerfile
├── docker-compose.yml
└── README.md
```

- `app/`: Contains the FastAPI application code.
- `Dockerfile`: Defines the Docker image for the FastAPI application.
- `docker-compose.yml`: Configuration for Docker Compose to run the application.

## Environment Variables

The application can be configured using environment variables. Update the `.env` file or set them directly in your environment.
