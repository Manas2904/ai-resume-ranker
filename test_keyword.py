from utils.keyword_matcher import keyword_match_score

resume = """
Python Machine Learning NLP TensorFlow Docker
"""

jd = """
Python Machine Learning Docker AWS FastAPI
"""

score, matched, missing = keyword_match_score(resume, jd)

print(f"Keyword Match Score: {score:.2f}")
print("Matched:", matched)
print("Missing:", missing)