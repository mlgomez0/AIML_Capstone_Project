
# Capstone Project Deployment Guide

This document serves as a comprehensive guide for deploying the Capstone Project created for AI and ML Lab at Lambton College.

The steps outlined here will assist you in setting up and running the application both locally and in a Dockerized environment. The guide is divided into several sections: creating a Django superuser, running the API and front-end locally, and finally, creating and publishing Docker images for both the back-end and front-end. Each section provides detailed, step-by-step instructions to ensure a smooth setup and deployment process.

## Run project locally

### Create Django User

To initialize the Django application, start by creating a superuser:

```bash
python ./api/manage.py createsuperuser
```

### Run API

Follow these steps to set up and run the back-end API:

1. Go to the folder `./backend`
2. Install packages
    ```bash
    pip install -r requirements.txt
    ```
3. Activate Python environment.
4. Go to the folder `./backend/api`
5. Set environment variables
    ```bash
    python -m export HUGGINGFACEHUB_API_TOKEN=YOUR_TOKEN
    ```
6. Start the server
    ``` bash
    python .\manage.py runserver
    ```

### Run Front

1. Go to the folder `./frontend`
2. Install packages all the packages project needs
    ```bash
    npm i
    ```
3. Start server
    ```bash
    npm start
    ```

After complete the steps you will be abble to navigate to the page http://localhost:3000 and see the chatbot.

## Create and publish Docker images

### Back-end

1. Create a Docker image
    ```bash
    docker build -t "capstone-api" .
    ```

2. Create a container
    ```bash
    docker create --name=api -p 12000:5000 -e HUGGINGFACEHUB_API_TOKEN=YOUR_TOKEN capstone-api
    ```

3. Create a tag. You can change the version as needed
    ```bash
    docker tag capstone-api your_container_registry_name.azurecr.io/capstone-api:1.0.0
    ```

4. Push the image to Azure Container Registry
    ```bash
    docker push your_container_registry_name.azurecr.io/capstone-api:latest
        ```

### Front-end

1. Create a Docker image
    ```bash
    docker build -t "capstone-front" .
    ```

2. Create a container
    ```bash
    docker create --name=front -p 11000:3000 -e NODE_ENV=production -e REACT_APP_API_URL=YOUR_DJANGO_CONTAINER_URL capstone-front
    ```

3. Create a tag. You can change the version as needed
    ```bash
    docker tag capstone-front your_container_registry_name.azurecr.io/capstone-front:1.0.0
    ```

4. Push the image to Azure Container Registry
    ```bash
    docker push your_container_registry_name.azurecr.io/capstone-front:latest
    ```

After publish the imagen on Azure Container Registry, you will be abble to create an App service to publish the back-end and front-end/