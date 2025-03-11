import PyPDF2

class PDFProcessor:

    @staticmethod
    def extract_text(pdf_path):
        """Extract text from a given PDF file."""
        pdf_text = ''
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                pdf_text += page.extract_text() or ''
        return pdf_text
