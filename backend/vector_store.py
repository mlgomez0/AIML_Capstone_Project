from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
import numpy as np


def get_vectorstore(data):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore =FAISS.from_texts(texts=data, embedding=embeddings)
    return vectorstore


num_vectors = 10
dimension = 256

dummy_data = np.random.rand(num_vectors, dimension).astype('float32')


vectorstore = get_vectorstore(dummy_data)







print(vectorstore)