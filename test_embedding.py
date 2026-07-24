from utils.embedding import generate_embedding

text = "Python Machine Learning NLP"

embedding = generate_embedding(text)

print("Embedding shape:", embedding.shape)
print(embedding[:10])  # First 10 values