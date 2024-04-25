import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from .models import ExtractedText  # Import the ExtractedText model
from .models import RawPDF
from .views import *
from .serializer import RawPDFSerializer

def process_raw_pdf(raw_pdf_instance):
    # Extract the pdf_file from the RawPDF instance
    pdf_file = raw_pdf_instance.pdf_file

    # Process the PDF file
    raw_text = ''
    reader = PyPDF2.PdfReader(pdf_file)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    # Split the text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    processed_text = text_splitter.split_text(raw_text)
    
    # Create an instance of ExtractedText and set its text_content field
    extracted_text_instance = ExtractedText.objects.create(
        raw_pdf=raw_pdf_instance,
        text_content='\n'.join(processed_text)  # Join the processed text chunks into a single string
    )
    
    return processed_text
