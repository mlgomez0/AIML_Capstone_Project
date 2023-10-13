# AIML_Capstone_Project

## Running the Frontend app

For the App to work, it is needed to have the following packages installed:
- node
- npm
If you don't have those installed in you computer, please install them first.

To starts the development server.
```
npm start
```
To bundles the app into static files for production.
```
npm run build
```
To start the test runner.
```
npm test
```

## To use the vector store Pinecone

Configure the following in your .env
```
PINECONE_API_KEY=xxxxx
PINECONE_ENV=xxxx
PINECONE_METRICS=xxxx
PINECONE_DIMENSIONS=xxx
```
## Running the Backend Tests

```
python -m unittest backend/tests/file_name.py
```
