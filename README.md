# PDF Semantic Search using FAISS and Sentence Transformers

## Overview
This project implements a **semantic search engine** for extracting relevant information from a PDF document using **FAISS (Facebook AI Similarity Search)** and **Sentence Transformers**. The application is built with **Flask** to provide a web interface where users can enter queries and retrieve the most relevant text chunks from the uploaded PDF.

## Features
- Extracts text from a PDF file
- Splits text into overlapping word chunks for better context
- Encodes chunks using **Sentence Transformers**
- Indexes and searches the text chunks using **FAISS**
- Provides a web interface for searching text within the PDF

## Project Structure
```plaintext
project-folder/
│── main.py                
│── Python Cheat Sheet - The Basics Coursera.pdf  # Sample PDF file
│── templates/
│   └── index.html         # Frontend HTML template
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Installation
### 1. Clone the Repository
```sh
git clone <repo-link>
cd project-folder
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### 1. Run the Flask App
```sh
python app.py
```
The application will start on **http://127.0.0.1:5000/**

### 2. Search for Keywords
- Open your browser and go to **http://127.0.0.1:5000/**
- Enter a search query in the input field and submit
- View relevant results with surrounding context

## Technologies Used
- **Python**: Core programming language
- **Flask**: Web framework for the UI
- **PyPDF2**: Extract text from PDFs
- **Sentence Transformers**: Convert text into numerical embeddings
- **FAISS**: Efficient similarity search for embeddings
- **NumPy**: Handling arrays and matrices

## Future Improvements
- Support for uploading custom PDFs
- Multiple document indexing
- Improved UI for better usability

## License
This project is open-source and available under the MIT License.

