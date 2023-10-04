import PyPDF2
import re

class DataLoader:
    def __init__(self, path):
        self.path = path
        self.text = ''
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
            reader = PyPDF2.PdfReader(self.path)
            for page in reader.pages:
                self.text += page.extract_text()

    
