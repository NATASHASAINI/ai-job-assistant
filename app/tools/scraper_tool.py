from app.services.scraper import scrape_job_description

def scrape_job_tool(url: str):
    return scrape_job_description(url)
