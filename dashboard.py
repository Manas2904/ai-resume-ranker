import os
import sys
import streamlit as st

# ===============================
# FORCE UTF-8 (WINDOWS FIX)
# ===============================
os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# ===============================
# PROJECT IMPORTS
# ===============================
from resume_loader import load_resumes_from_folder
from embedding_engine import EmbeddingEngine
from matcher import match_resumes
from llm_reasoner import LLMReasoner

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="AI Resume Ranking System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Resume Ranking & Explanation Dashboard")
st.markdown("Rank resumes against a job description using AI embeddings and LLM reasoning.")

# ===============================
# JOB DESCRIPTION INPUT
# ===============================
job_description = st.text_area(
    "📝 Job Description",
    height=150,
    value="""
Looking for an AI/ML Engineer with Python, ML, NLP,
deep learning, and deployment experience.
"""
)

# ===============================
# RUN BUTTON
# ===============================
if st.button("🚀 Run Resume Ranking"):

    with st.spinner("Loading resumes..."):
        resumes = load_resumes_from_folder("data/resumes")

    if not resumes:
        st.error("No resumes found in data/resumes folder.")
        st.stop()

    with st.spinner("Generating embeddings..."):
        embedder = EmbeddingEngine()
        resume_embeddings = embedder.embed_documents(resumes)
        job_embedding = embedder.embed_text(job_description)

    with st.spinner("Matching resumes..."):
        rankings = match_resumes(job_embedding, resume_embeddings)

    # ===============================
    # DISPLAY RANKINGS
    # ===============================
    st.subheader("📊 Resume Rankings")

    for idx, (resume, score) in enumerate(rankings.items(), start=1):
        st.write(f"**{idx}. {resume}** → `{score:.3f}`")

    # ===============================
    # AI EXPLANATION (SAFE)
    # ===============================
    top_resume = list(rankings.keys())[0]

    st.subheader("🧠 AI Explanation (Top Candidate)")

    reasoner = LLMReasoner()

    try:
        with st.spinner("Generating AI explanation..."):
            explanation = reasoner.explain_match(
                resumes[top_resume],
                job_description
            )
        st.success("Explanation generated successfully ✅")
        st.write(explanation)

    except Exception as e:
        st.error("⚠️ AI explanation failed (LLM issue).")
        st.markdown(
            """
            **Possible reasons:**
            - Missing or invalid API key  
            - Network / timeout issue  
            - Model response error  
            """
        )
        st.code(str(e))

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("Built with ❤️ using Python, Embeddings & LLMs")