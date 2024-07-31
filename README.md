# FastAPI ML Deployment

This repository contains a FastAPI application for deploying a machine learning model that classifies iris flowers based on their features. The application is containerized using Docker for easy deployment.

## Features

- **RESTful API**: Provides an endpoint for making predictions based on iris flower features.
- **Machine Learning Model**: Uses a pre-trained model to classify iris flowers into different species.
- **Dockerized**: Easily deployable with Docker.

## Getting Started

### Prerequisites

- Docker: Ensure Docker is installed and running on your machine.

### Running the Application

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/fastapi-iris-predictor.git
    cd fastapi-iris-predictor
    ```

2. **Build the Docker Image**

    ```sh
    docker build -t fastapi-iris .
    ```

3. **Run the Docker Container**

    ```sh
    docker run -d -p 8000:80 fastapi-iris
    ```

4. **Access the API**

    The API will be available at `http://127.0.0.1:8000`. You can use the Swagger UI for testing the endpoints at `http://127.0.0.1:8000/docs`.

### API Endpoints

- **POST /predict/**: Submit iris flower features to receive a prediction of the flower species.

    **Request Body**:

    ```json
    {
      "sepal_length": 5.1,
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    ```

    **Response**:

    ```json
    {
      "prediction": 0
    }
    ```