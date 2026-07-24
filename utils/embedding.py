from sentence_transformers import SentenceTransformer

# Load the model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    """
    Convert text into a semantic embedding vector.
    """

    return model.encode(text, convert_to_numpy=True)