from app.services.scraper import scrape_job_description
from app.services.llm_service import call_llm, safe_json_parse
from app.services.prompts import RESUME_SCORE_PROMPT, TAILORED_ANSWER_PROMPT


def resume_score(resume: str, job_url: str):
    job_text = scrape_job_description(job_url)

    prompt = RESUME_SCORE_PROMPT.format(
        resume=resume,
        job=job_text
    )

    result = call_llm(prompt)
    return safe_json_parse(result)


def generate_answer(profile: dict, job_url: str, question: str):
    job_text = scrape_job_description(job_url)

    prompt = TAILORED_ANSWER_PROMPT.format(
        profile=profile,
        job=job_text,
        question=question
    )

    return call_llm(prompt)
