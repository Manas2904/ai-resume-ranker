import subprocess

class LLMReasoner:
    def __init__(self, model="llama3"):
        self.model = model

    def explain_match(self, resume_text, job_description):
        prompt = f"""
You are an AI hiring assistant.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

TASK:
1. Explain why this resume matches or does not match the job.
2. List key matching skills.
3. Mention missing skills (if any).
4. Give a short hiring recommendation.
"""

        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            text=True,
            capture_output=True
        )

        return result.stdout.strip()