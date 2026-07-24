from utils.skills import AI_SKILLS


def extract_skills(text: str):
    """
    Extract AI/ML skills from text.
    """

    text = text.lower()

    found_skills = []

    for skill in AI_SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def calculate_skill_score(resume_text: str, jd_text: str):
    """
    Compare extracted skills between resume and JD.
    """

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)

    score = len(matched) / len(jd_skills) if jd_skills else 0

    return score, matched, missing