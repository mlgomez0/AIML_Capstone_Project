# django api

This project contains the backend for the natural language processing project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Export the following env variables
```bash
export HUGGINGFACEHUB_API_TOKEN='your api key'
```

## Installation

Go to the backend/ directory and use the following command.

```bash
pip install -r requirements.txt
```

## Project Directory

Go to `backend/api`


## Create superuser

```bash
python manage.py createsuperuser
```

User the admin credential to navigate the app or alternatively, you can create a new user going to http://127.0.0.1:8000/admin once the server is running.

## Start the app

To start the server, run the following command in the directory `backend/api` and then navigate to `http://127.0.0.1:8000` in the browser:

```bash
python manage.py runserver
```

# Script Embeddings Loading

## ChromaDB

This is a in-unit vector store. To create embeddings from files in a folder and store them in a vector store, you can run the following script inside the backend/api directory:

```bash
CHROMA_PATH=docs/chroma/ python ../load_embeddings.py chroma files_directory
```

Then to load the vector store and do similarity searh, use the following:

Set the environmental variable "CHROMA_PATH".

```bash

data_transformer = DataTransformer()
embedder = data_transformer.get_spacy_embedding()

vectorDb = VectorStores().load_chroma_vectorstore(embedder)
question="something related to the docs"
vectorDb.similarity_search(question,k=3)
vectorDb._collection.count()

```
Currently, the project only supports PDF format