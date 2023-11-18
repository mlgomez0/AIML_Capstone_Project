import unittest
from unittest.mock import patch
from modules_ai.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_check_path_pattern_with_pdf_extension(self):
        data_loader = DataLoader("sample.pdf")
        data_loader.check_path_pattern()
        self.assertEqual(data_loader.extension, 'pdf')

    def test_check_path_pattern_with_non_pdf_extension(self):
        data_loader = DataLoader("document.txt")
        data_loader.check_path_pattern()
        self.assertEqual(data_loader.extension, '')

    def test_load_with_pdf_extension(self):
        class MockPdfPage:
            def extract_text(self):
                return "This is a PDF document."

        class MockPdfReader:
            def __init__(self, path):
                pass

            @property
            def pages(self):
                return [MockPdfPage()]

        with patch('PyPDF2.PdfReader', MockPdfReader):
            data_loader = DataLoader("sample.pdf")
            data_loader.load()
            self.assertEqual(data_loader.text, "This is a PDF document.")

    def test_load_with_non_pdf_extension(self):
        data_loader = DataLoader("document.txt")
        data_loader.load()
        self.assertEqual(data_loader.text, '')
