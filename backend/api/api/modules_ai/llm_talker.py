from .vector_store import VectoreStores
from .data_transformer import DataTransformer
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import LLMChain
import string

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
        chroma = VectoreStores()
        embedder = DataTransformer().get_hugging_face_embedding()
        self.vector_DB = chroma.load_chroma_vectorstore(embedder)
        docs = self.vector_DB.similarity_search(question)
        docs_page_content = " ".join([d.page_content for d in docs])
        template = """
            You are VTL, a virtual technical leader that can answer questions about Dollarama.
            
            To answer the question, you only use the factual information in {docs}.
            
            If you feel like you don't have enough information to answer the question, say "I don't know".
            
            Your answers should be verbose and detailed.
            """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # Human question prompt
        human_template = "Answer the following question: {question}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chain = LLMChain(llm=llm, prompt=chat_prompt)

        cleaned_question = self.clean_user_input(question)
        response = chain.run(question=cleaned_question, docs=docs_page_content)
        response = response.replace("\n", "")
        response_template = f"Thanks for asking! {response}"
        return response_template
    
    def clean_user_input(self, text):
        result = text.translate(str.maketrans('','', string.punctuation))
        return result.lower()
  
    
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