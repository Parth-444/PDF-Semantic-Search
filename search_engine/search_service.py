from sentence_transformers import SentenceTransformer
import numpy as np
from .faiss_indexer import FaissIndexer

class SearchService:
    """Main class to manage text processing and FAISS search."""

    def __init__(self, pdf_text, model_name='all-mpnet-base-v2'):
        """Initialize the search service with a pre-trained model."""
        self.model = SentenceTransformer(model_name)
        self.chunk_list = self.chunk_text(pdf_text)
        self.embeddings = self.model.encode(self.chunk_list)
        self.indexer = FaissIndexer(self.embeddings)

    def chunk_text(self, text):
        """Chunk text into small overlapping segments."""
        from .text_chunker import TextChunker
        return TextChunker.chunk_by_words(text)

    def search(self, query, k=3, context_size=2):
        """Perform a search query in FAISS index and return results."""
        query_embedding = self.model.encode([query])
        distances, indices = self.indexer.search(query_embedding, k)

        results = []
        for i, idx in enumerate(indices[0]):
            start_idx = max(0, idx - context_size)
            end_idx = min(len(self.chunk_list), idx + context_size + 1)
            context = " ".join(self.chunk_list[start_idx:end_idx])
            results.append({
                "chunk": self.chunk_list[idx],
                "context": context,
                "distance": float(distances[0][i])
            })
        return results