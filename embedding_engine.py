from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_text(self, text):
        return self.model.encode(text)

    def embed_documents(self, docs):
        return {k: self.embed_text(v) for k, v in docs.items()}