import pinecone
from langchain.vectorstores import Chroma
import os

class VectoreStores:
    def __init__(self):
        self.persist_directory = "docs/chroma/"

    def get_pinecone_vectorstore(self):
        api_key = os.environ["PINECONE_API_KEY"]
        api_env = os.environ["PINECONE_ENV"]
        index_name = index_name
        pinecone.init(
            api_key=api_key,
            environment=api_env,
        )

        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(
            name=self.index_name,
            metric=os.environ["PINECONE_METRICS"],
            dimension=int(os.environ["PINECONE_DIMENSIONS"])
            )
        index = pinecone.Index(index_name)

        return index
    
    def get_chroma_vectorstore(self, tokens, embedder):
        vectorDB = Chroma.from_documents(
            documents=tokens,
            embedding=embedder,
            persist_directory=self.persist_directory
        )
        return vectorDB
    
    def load_chroma_vectorstore(self, embedder):
        vectorDB = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=embedder
        )
        return vectorDB


    def check_pinecone_config(self):
        api_key = os.environ["PINECONE_API_KEY"]
        api_env = os.environ["PINECONE_ENV"]
        pinecone.init(api_key=api_key, environment=api_env)
        return pinecone.list_indexes()