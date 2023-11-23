import nltk
import spacy
from langchain.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import os

class DataTransformer:
    def __init__(self):
        self.tokens = []
        self.embeddings = []

    def clean_text_with_nlp(self, text):
        nltk.download('punkt')
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        cleaned_text = ' '.join(cleaned_tokens)
        return cleaned_text

    def load_tokens_from_docs(
            self, docs, method='RecursiveCharacter',
            chunk_size=1500, chunk_overlap=150
        ):
        if method == 'RecursiveCharacter':
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size = chunk_size,
                chunk_overlap = chunk_overlap
            )
            self.tokens = text_splitter.split_documents(docs)

    def open_ai_embeddings(self):
        open_ai_api_key = os.environ["OPENAI_API_KEY"]
        embedder = OpenAIEmbeddings(openai_api_key=open_ai_api_key)
        return embedder
        

    def get_spacy_embedding(self):
        embedder = SpacyEmbeddings()
        return embedder
    
    def get_hugging_face_embedding(self, model_name=None):
        if model_name:
            embedder = HuggingFaceEmbeddings(model_name=model_name)
        else:
            embedder = HuggingFaceEmbeddings()
        return embedder
