from resume_parser import load_all_resumes
from embedding_engine import EmbeddingEngine
from matcher import match_resumes
from recruiter_chat import RecruiterChat

JOB_DESCRIPTION = """
Looking for an AI/ML Engineer with experience in Python, ML, NLP, and deployment.
"""

resumes = load_all_resumes("data/resumes")
embedder = EmbeddingEngine()
chatbot = RecruiterChat()

resume_embeddings = embedder.embed_documents(resumes)
job_embedding = embedder.embed_text(JOB_DESCRIPTION)
rankings = match_resumes(job_embedding, resume_embeddings)

context = f"""
Job Description:
{JOB_DESCRIPTION}

Resume Rankings:
{rankings}

Resumes:
{resumes}
"""

print("🤖 AI Recruiter Chat (type 'exit' to quit)\n")

while True:
    user_q = input("You: ")
    if user_q.lower() == "exit":
        break

    response = chatbot.ask(user_q, context)
    print("\nAI Recruiter:", response, "\n")