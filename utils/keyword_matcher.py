import re


def extract_keywords(text: str) -> set:
    """
    Extract unique keywords from text.

    Args:
        text: Input text.

    Returns:
        Set of unique keywords.
    """

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    return set(words)


def keyword_match_score(resume_text: str, jd_text: str):
    """
    Compare keywords between resume and job description.

    Returns:
        score,
        matched_keywords,
        missing_keywords
    """

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = resume_keywords.intersection(jd_keywords)

    missing = jd_keywords.difference(resume_keywords)

    score = len(matched) / len(jd_keywords) if jd_keywords else 0

    return score, matched, missing