import faiss
import numpy as np

class FaissIndexer:
    """Class for FAISS-based semantic search indexing."""

    def __init__(self, embeddings):
        """Initialize FAISS index with embeddings."""
        self.dimensions = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimensions)
        self.index.add(np.array(embeddings))

    def search(self, query_embedding, k=3):
        """Search for the top-k nearest neighbors in FAISS index."""
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices