class TextChunker:
    """Class to chunk text into word-based segments."""

    @staticmethod
    def chunk_by_words(text, chunk_size=30, overlap=10):
        """Splits text into overlapping word chunks."""
        words = text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = min(start + chunk_size, len(words))
            chunk = ' '.join(words[start:end])
            chunks.append(chunk)
            new_start = end - overlap
            if new_start == start:
                break
            start = new_start

        return chunks