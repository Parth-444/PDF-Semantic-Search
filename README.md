# Semantic Search in PDFs Using FAISS

## Overview
This project is a command-line tool that allows users to perform semantic search on text extracted from PDF files. It uses FAISS (Facebook AI Similarity Search) for efficient vector search and SentenceTransformers for generating embeddings. The system is modular, making it easy to maintain and extend.

## Features
- Extracts text from a PDF file
- Splits the text into overlapping chunks
- Uses FAISS for fast similarity search
- Returns search results in JSON format
- CLI-based interface with modular design

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7 or higher is recommended). Install the required dependencies using:

```sh
pip install numpy faiss-cpu sentence-transformers pypdf2
```

## Project Structure
```
semantic_search_project/
│── main.py                  # Entry point for CLI-based search
│── search_engine/
│   ├── __init__.py          # Package initializer
│   ├── pdf_processor.py     # Extracts text from PDF
│   ├── text_chunker.py      # Splits text into chunks
│   ├── faiss_indexer.py     # Handles FAISS indexing & searching
│   ├── search_service.py    # Manages the search process
```

## Usage

### Running the Program
To start the CLI tool, run:
```sh
python main.py
```

### Example Interaction
```
Enter PDF file path: sample.pdf
Processing the PDF file...

Enter your search query (or type 'exit' to quit): lambda function

Search Results (JSON Format):
{
    "query": "lambda function",
    "results": [
        {
            "chunk": "Python supports lambda functions...",
            "context": "Python supports lambda functions... and list comprehensions...",
            "distance": 0.123
        },
        {
            "chunk": "Lambdas are used for anonymous functions...",
            "context": "Lambdas are used for anonymous functions... in Python programming...",
            "distance": 0.187
        }
    ]
}

Enter your search query (or type 'exit' to quit): exit
Exiting program.
```

## How It Works
1. **Extract PDF Text**: The `pdf_processor.py` module extracts text from the given PDF file.
2. **Chunking**: `text_chunker.py` splits the extracted text into overlapping word chunks for better context retention.
3. **Embedding Generation**: `search_service.py` encodes the text chunks using the `SentenceTransformer` model.
4. **Indexing and Search**: `faiss_indexer.py` creates a FAISS index and searches for semantically similar text chunks.
5. **JSON Output**: The search results are displayed in a structured JSON format with relevant context.

## Dependencies
- Python 3.7+
- [FAISS](https://github.com/facebookresearch/faiss)
- [SentenceTransformers](https://www.sbert.net/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- NumPy

## Customization
- Modify `chunk_size` and `overlap` in `text_chunker.py` to change chunking behavior.
- Change the transformer model in `search_service.py` by modifying `model_name`.
- Adjust the `k` value in `search()` to retrieve more or fewer search results.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

