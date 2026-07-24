from utils.skill_matcher import calculate_skill_score

resume = """
Python
Machine Learning
TensorFlow
Docker
NLP
"""

jd = """
Python
Machine Learning
Docker
AWS
FastAPI
"""

score, matched, missing = calculate_skill_score(resume, jd)

print("Skill Score:", round(score * 100, 2))

print("\nMatched Skills")
print(matched)

print("\nMissing Skills")
print(missing)