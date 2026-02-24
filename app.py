import os
import sys

# ===============================
# FORCE UTF-8 (MUST BE FIRST)
# ===============================
os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# ===============================
# NOW SAFE TO IMPORT PROJECT CODE
# ===============================
from resume_loader import load_resumes_from_folder
from embedding_engine import EmbeddingEngine
from matcher import match_resumes
from llm_reasoner import LLMReasoner

JOB_DESCRIPTION = """
Looking for an AI/ML Engineer with Python, ML, NLP,
deep learning, and deployment experience.
"""

if __name__ == "__main__":
    resumes = load_resumes_from_folder("data/resumes")

    embedder = EmbeddingEngine()
    reasoner = LLMReasoner()

    resume_embeddings = embedder.embed_documents(resumes)
    job_embedding = embedder.embed_text(JOB_DESCRIPTION)

    rankings = match_resumes(job_embedding, resume_embeddings)

    print("\n📊 Resume Rankings:")
    for r, s in rankings.items():
        print(f"{r} → {s}")

    top_resume = list(rankings.keys())[0]

    print("\n🧠 AI Explanation:\n")
    explanation = reasoner.explain_match(
        resumes[top_resume],
        JOB_DESCRIPTION
    )

    print(explanation)