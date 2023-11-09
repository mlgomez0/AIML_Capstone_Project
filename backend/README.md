# django api

This project contains the backend for the natural language processing project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Go to the backend/ directory and use the following command.

```bash
pip install -r requirements.txt
```

To start the server, run the following command in the directory `backend/api` and then navigate to `http://127.0.0.1:8000/items` in the browser:

```bash
python manage.py runserver
```

# Script Embeddings Loading

## ChromaDB

This is a in-unit vector store. To create embeddings from files in a folder and store them in a vector store, you can run the following script inside the backend directory:

```bash
CHROMA_PATH=db_path python load_embeddings.py chroma files_directory
```

Currently, the project only supports PDF format