import spacy
import numpy as np
from PyPDF2 import PdfReader

class DataTransformer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")  # Load a pre-trained spaCy model

    def embed_text(self, text_data):
        embeddings = []
        for text in text_data:
            doc = self.nlp(text)
            # Calculate the mean vector of word embeddings
            mean_vector = np.mean([word.vector for word in doc if word.has_vector], axis=0)
            embeddings.append(mean_vector)
        return embeddings

    def extract_text_from_pdf(self, pdf_file_path):
        text_data = []
        pdf_reader = PdfReader(pdf_file_path)
        for page in pdf_reader.pages:
            text_data.append(page.extract_text())
        return text_data

    def embed_pdf(self, pdf_file_path):
        text_data = self.extract_text_from_pdf(pdf_file_path)
        embeddings = self.embed_text(text_data)
        return embeddings

# Example usage:
if __name__ == "__main__":
    data_transformer = DataTransformer()
    pdf_file_path = "YourPDFFile.pdf"
    embeddings = data_transformer.embed_pdf(pdf_file_path)
    print(embeddings)
