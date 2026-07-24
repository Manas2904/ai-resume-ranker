from utils.embedding import generate_embedding
from utils.similarity import calculate_similarity
from utils.keyword_matcher import keyword_match_score


def calculate_resume_score(resume_text: str, jd_text: str):
    """
    Calculate ATS score by combining semantic similarity
    and keyword matching.
    """

    # Generate embeddings
    resume_embedding = generate_embedding(resume_text)
    jd_embedding = generate_embedding(jd_text)

    # Semantic similarity
    semantic_score = calculate_similarity(
        resume_embedding,
        jd_embedding
    )

    # Keyword matching
    keyword_score, matched_keywords, missing_keywords = keyword_match_score(
        resume_text,
        jd_text
    )

    # Placeholder for skill score
    skill_score = keyword_score

    # Weighted score
    final_score = (
        semantic_score * 0.70 +
        keyword_score * 0.20 +
        skill_score * 0.10
    )

    return {
        "semantic_score": round(semantic_score * 100, 2),
        "keyword_score": round(keyword_score * 100, 2),
        "skill_score": round(skill_score * 100, 2),
        "final_score": round(final_score * 100, 2),
        "matched_keywords": sorted(list(matched_keywords)),
        "missing_keywords": sorted(list(missing_keywords))
    }