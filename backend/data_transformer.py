import spacy
from langchain.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

class DataTransformer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def clean_text_with_nlp(self, text):
        doc = self.nlp(text)
        cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        cleaned_text = ' '.join(cleaned_tokens)
        return cleaned_text

    def tokenize_words(self, text):
        tokens = text.split()
        return tokens

    def get_spacy_embedding(self, tokens):
        embedder = SpacyEmbeddings()
        embeddings = embedder.embed_documents(tokens)
        return embeddings
    
    def get_hugging_face_embedding(self, model_name, tokens):
        embedder = HuggingFaceEmbeddings(model_name=model_name)
        embeddings = embedder.embed_documents(tokens)
        return embeddings
