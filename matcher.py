import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def match_resumes(job_embedding, resume_embeddings):
    scores = {}
    for name, emb in resume_embeddings.items():
        scores[name] = round(cosine_similarity(job_embedding, emb), 3)

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))