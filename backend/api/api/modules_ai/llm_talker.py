from .vector_store import VectoreStores
from .data_transformer import DataTransformer
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

class LlmTalker:
    
    def __init__(self):
        self.vector_DB = None
        self.llm = None
        self.talker = None
        self.conversation = []

    def start_chat(self, question):
        repo_id = "google/flan-t5-xxl"
        llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 1, "max_length": 1000000}
        )
        llm_chain = load_qa_chain(llm, chain_type='stuff')
        chroma = VectoreStores()
        embedder = DataTransformer().get_hugging_face_embedding()
        self.vector_DB = chroma.load_chroma_vectorstore(embedder)
        docs = self.vector_DB.similarity_search(question)
        response = llm_chain.run(input_documents=docs, question=question)
        return response
    
  
    
    def start_chat_openai(self):
        template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
        {context}
        Question: {question}
        Helpful Answer:"""
        TEMPLATE_PROMPT = PromptTemplate.from_template(template)
        chroma = VectoreStores()
        embedder = DataTransformer().get_spacy_embedding()
        self.vector_DB = chroma.load_chroma_vectorstore(embedder)
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        self.talker = RetrievalQA.from_chain_type(
            self.llm,
            retriever=self.vector_DB.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": TEMPLATE_PROMPT}
        )
    
    def chat(self, question):
        response = self.start_chat(question)
        return response