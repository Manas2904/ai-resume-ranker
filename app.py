import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.scoring import calculate_resume_score

st.set_page_config(
    page_title="AI Resume Ranker",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Ranker")

st.write("Upload a Job Description and one or more resumes.")

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf"]
)

resume_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Resume"):

    if jd_file is None:
        st.error("Please upload a Job Description.")
        st.stop()

    if len(resume_files) == 0:
        st.error("Please upload at least one Resume.")
        st.stop()

    jd_text = extract_text_from_pdf(jd_file)

    results = []

    for resume in resume_files:

        resume_text = extract_text_from_pdf(resume)

        score = calculate_resume_score(
            resume_text,
            jd_text
        )

        score["Resume"] = resume.name

        results.append(score)

    results = sorted(
        results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    st.success("Analysis Complete!")

    for idx, result in enumerate(results):
        
        st.divider()
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.metric("Score", f"{result['final_score']}%")
            
            if result['final_score'] >= 80:
                st.success("✅ Perfect Match")
            elif result['final_score'] >= 60:
                st.warning("⚠️ Good Match")
            else:
                st.error("❌ Poor Match")
        
        with col2:
            st.subheader(f"📄 {result['Resume']}")
            
            st.write(f"**Semantic Score:** {result['semantic_score']}%")
            st.write(f"**Keyword Score:** {result['keyword_score']}%")
            st.write(f"**Skill Score:** {result['skill_score']}%")
            
            with st.expander("Matched Keywords"):
                st.write(", ".join(result['matched_keywords']))
            
            with st.expander("Missing Keywords"):
                st.write(", ".join(result['missing_keywords']))