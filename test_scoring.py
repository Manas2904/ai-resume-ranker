from utils.scoring import calculate_resume_score

resume = """
Python
Machine Learning
NLP
TensorFlow
Docker
"""

jd = """
Looking for an AI Engineer with Python,
Machine Learning,
Docker,
AWS,
FastAPI.
"""

result = calculate_resume_score(
    resume,
    jd
)

print(result)