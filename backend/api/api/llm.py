from langchain import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import chromadb
import gradio as gr
import os
import torch

class LlModel:

    def __ini__(self):
        self.model_name = "anakin87/zephyr-7b-alpha-sharded"

    def load_quantized_model(model_name: str):
        # Since bfloat16 may not be supported on Windows or your device, use float32
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=False,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float32  # changed from torch.bfloat16
        )

        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_4bit=False,
            torch_dtype=torch.float32,  # changed from torch.bfloat16
            quantization_config=bnb_config
        )

        return model

    def initialize_tokenizer(model_name: str):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.bos_token_id = 1  # Set beginning of sentence token id
        return tokenizer

        # load model

    def initialize(self):

        self.model = self.load_quantized_model(self.model_name)

        # initialize tokenizer
        self.tokenizer = self.initialize_tokenizer(self.model_name)

        # specify stop token ids
        self.stop_token_ids = [0]
