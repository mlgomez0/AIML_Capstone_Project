from data_loader import DataLoader
from data_transformer import DataTransformer
from vector_store import VectoreStores
import sys
import os

   

if __name__ == "__main__":
    def load_to_chromadb():
        dir_name = sys.argv[2]
        docs = []
        files = os.listdir(dir_name)
        for file in files:
            path = dir_name + '/' + file
            loader = DataLoader(path)
            loader.load()
            pages = loader.pages
            docs.extend(pages)
        data_transformer = DataTransformer()
        data_transformer.load_tokens_from_docs(docs)
        embedder = data_transformer.get_spacy_embedding()
        chroma = VectoreStores()
        vectorDB = chroma.get_chroma_vectorstore(
            data_transformer.tokens,
            embedder
        )
        vectorDB.persist()
        print(f"Vector store was created with {vectorDB._collection.count()} records")
    if sys.argv[1] == 'chroma':
        load_to_chromadb()