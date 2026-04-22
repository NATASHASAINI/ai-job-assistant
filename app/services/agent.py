import json
from app.services.scraper import scrape_job_description
from app.services.prompts import resume_prompt, tailored_prompt
from app.services.llm_service import call_llm

def resume_score(resume, job_url):
    job = scrape_job_description(job_url)
    prompt = resume_prompt(resume, job)
    result = call_llm(prompt)
    return json.loads(result)


def generate_answer(profile, job_url, question):
    job = scrape_job_description(job_url)
    prompt = tailored_prompt(profile, job, question)
    return call_llm(prompt)
