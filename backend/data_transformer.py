from langchain.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

class DataTransformer:
    def __init__(self):
        pass


    def get_spacy_embedding(self, tokens):
        embedder = SpacyEmbeddings()
        embeddings = embedder.embed_documents(tokens)
        return embeddings
    
    def get_hugging_face_embedding(self, model_name, tokens):
        embedder = HuggingFaceEmbeddings(model_name=model_name)
        embeddings = embedder.embed_documents(tokens)
        return embeddings
