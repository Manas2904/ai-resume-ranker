from utils.embedding import generate_embedding
from utils.similarity import calculate_similarity

resume = """
Python Machine Learning NLP Docker TensorFlow
"""

job_description = """
Looking for an AI Engineer with Python, NLP, Docker and Machine Learning experience.
"""

resume_embedding = generate_embedding(resume)
jd_embedding = generate_embedding(job_description)

score = calculate_similarity(resume_embedding, jd_embedding)

print(f"Similarity Score: {score:.4f}")
print(f"Percentage Match: {score * 100:.2f}%")