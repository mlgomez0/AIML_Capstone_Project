
import os

import chromadb
import torch
from langchain import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig, pipeline)

class LargeLanguageModel:

    def __init__(self, document_folder_path: str) -> None:
        self.document_folder_path = document_folder_path
        self.model_name = "anakin87/zephyr-7b-alpha-sharded"
        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()
        self.stop_token_ids = [0]
        self.initialize_chroma_db()
        self.pipeline = self.build_pipeline()

    def load_model(self):
        
        print('Initializing BitsAndBytesConfig')

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=False,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float32  # changed from torch.bfloat16
        )

        print('Initializing model', self.model_name)

        model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            load_in_4bit=False,
            torch_dtype=torch.float32,
            quantization_config=bnb_config
        )

        return model

    def load_tokenizer(self):

        print('Initializing tokenizer')

        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        tokenizer.bos_token_id = 1  # Set beginning of sentence token id
        return tokenizer

    def build_pipeline(self):

        print('Initializing pipeline')

        model_pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            use_cache=True,
            device_map="auto",
            max_length=2048,
            do_sample=True,
            top_k=5,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        # specify the llm
        return HuggingFacePipeline(pipeline=model_pipeline)

    def initialize_chroma_db(self):

        print('Reading PDFs')

        # Read all files of the root folder
        loader = PyPDFDirectoryLoader(self.document_folder_path)
        documents = loader.load()
        if len(documents) == 0:
            raise "No documents found"

        # Split documents in chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        all_splits = text_splitter.split_documents(documents)

        # specify embedding model (using huggingface sentence transformer)
        embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
        model_kwargs = {"device": "cpu"}
        embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name, model_kwargs=model_kwargs)

        # Create vector database and save the documents
        vectordb = Chroma.from_documents(documents=all_splits, embedding=embeddings, persist_directory="./chroma_db")

        # specify the retriever
        self.retriever = vectordb.as_retriever()

    # build conversational retrieval chain with memory (rag) using langchain
    def create_conversation(self, query: str, chat_history: list) -> tuple:
        
        try:

            memory = ConversationBufferMemory(memory_key='chat_history', return_messages=False)
            print(self.pipeline)
            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=self.pipeline,
                retriever=self.retriever,
                memory=memory,
                get_chat_history=lambda h: h,
            )

            result = qa_chain({'question': query, 'chat_history': chat_history})
            chat_history.append((query, result['answer']))
            return '', chat_history


        except Exception as e:
            chat_history.append((query, e))
            return '', chat_history
