def exact_match_score(jd_skills, resume_skills):
    jd = set(skill.lower() for skill in jd_skills)
    resume = set(skill.lower() for skill in resume_skills)

    matched = jd.intersection(resume)
    score = (len(matched) / len(jd)) * 100 if jd else 0

    return score, list(matched)