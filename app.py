import PyPDF2
from sentence_transformers import SentenceTransformer
import numpy as np
from flask import Flask, render_template, request, jsonify
import faiss

model = SentenceTransformer('all-mpnet-base-v2')
app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    pdf_text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdf_text+=page.extract_text()
    return pdf_text

def chunk_by_words(texts,  chunk_size=100, overlap=20):
    words = texts.split()
    chunks=[]
    start = 0

    while start< len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        if start<0:
            start=0
        new_start = end-overlap
        if new_start==start:
            break
        else:
            start=new_start

    return chunks

result_text = extract_text_from_pdf('resume.pdf')
chunk_list = chunk_by_words(result_text)
embeddings = model.encode(chunk_list)
print(embeddings)
dimensions=embeddings.shape[1]
index= faiss.IndexFlat(dimensions)
index.add(np.array(embeddings))

def search_faiss_words_with_context(query, index, model, chunks, k=3, context_size=2):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    results = []
    for i, idx in enumerate(indices[0]):
        start_idx = max(0, idx - context_size)
        end_idx = min(len(chunks), idx + context_size + 1)
        context = " ".join(chunks[start_idx:end_idx])
        results.append({
            "chunk": chunks[idx],
            "context": context,
            "distance": distances[0][i]
        })
    return results


@app.route('/', methods=['POST', 'GET'])
def final():
    if request.method=='POST':
        query=request.form['query']
        results = search_faiss_words_with_context(query, index, model, chunk_list)
        return render_template('index.html', results=results, query=query)
    return render_template('index.html', results=None, query=None)


if __name__ == '__main__':
    app.run(debug=True)