import pinecone
import os

class VectoreStores:
    def __init__(self, index_name):
        self.api_key = os.environ["PINECONE_API_KEY"]
        self.api_env = os.environ["PINECONE_ENV"]
        self.index_name = index_name

    def get_pinecone_vectorstore(self):
        pinecone.init(
            api_key=self.api_key,
            environment=self.api_env,
        )

        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(
            name=self.index_name,
            metric=os.environ["PINECONE_METRICS"],
            dimension=int(os.environ["PINECONE_DIMENSIONS"])
            )
        index = pinecone.Index(self.index_name)

        return index


    def check_pinecone_config(self):
        api_key = os.environ["PINECONE_API_KEY"]
        api_env = os.environ["PINECONE_ENV"]
        pinecone.init(api_key=api_key, environment=api_env)
        return pinecone.list_indexes()