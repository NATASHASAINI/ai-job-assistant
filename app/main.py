from app.agents.resume_scorer import analyze_resume_and_jd
import json

def run():
    with open("resume.txt", "r") as f:
        resume = f.read()  # <- must be indented inside 'with'

    url = "https://jobs.ashbyhq.com/openai"

    result = analyze_resume_and_jd(resume, url)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    run()


