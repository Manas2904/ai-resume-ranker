import subprocess
import sys

# Ensure stdout uses UTF-8 (important for Windows)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass  # For older Python versions


class RecruiterChat:
    def __init__(self, model: str = "llama3"):
        """
        RecruiterChat uses a local LLM (Ollama) to reason about resumes
        and job descriptions in natural language.
        """
        self.model = model

    def _run_llm(self, prompt: str) -> str:
        """
        Runs the Ollama model with proper UTF-8 handling
        to avoid Windows encoding errors.
        """
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",   # 🔥 FIXES UnicodeDecodeError
            errors="ignore"     # 🔥 Safely skips bad bytes
        )

        if result.returncode != 0:
            return f"LLM Error: {result.stderr}"

        return result.stdout.strip()

    def analyze_resume(self, resume_text: str, job_description: str) -> str:
        """
        Ask the LLM to analyze why a resume matches or does not match a job.
        """
        prompt = f"""
You are an AI recruiter.

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume_text}

TASK:
1. Explain why this resume matches or does not match the job.
2. List key matching skills.
3. List missing skills (if any).
4. Give a hiring recommendation.

Respond clearly in structured points.
"""
        return self._run_llm(prompt)

    def answer_followup(self, context: str, question: str) -> str:
        """
        Allows conversational follow-up questions on the same resume.
        """
        prompt = f"""
You are an AI recruiter assistant.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear, professional answer.
"""
        return self._run_llm(prompt)