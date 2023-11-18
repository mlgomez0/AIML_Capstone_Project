from langchain.document_loaders import PyPDFLoader
import re

class DataLoader:
    def __init__(self, path):
        self.path = path
        self.pages = None
        self.extension = ''

    def check_path_pattern(self):
        allowed_patterns = {'pdf': r'\.pdf$'}
        for k, v in allowed_patterns.items():
            if re.search(v, self.path, re.IGNORECASE):
                self.extension = 'pdf'
                break

    def load(self):
        self.check_path_pattern()
        if self.extension == 'pdf':
            loader = PyPDFLoader(self.path)
            pages = loader.load()
            self.pages = pages

            

    
