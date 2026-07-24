from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_embedding, jd_embedding) -> float:
    """
    Calculate cosine similarity between two embeddings.
    """

    score = cosine_similarity(
        resume_embedding.reshape(1, -1),
        jd_embedding.reshape(1, -1)
    )

    return float(score[0][0])