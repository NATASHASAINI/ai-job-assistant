from app.services.scraper import get_job_links, scrape_job_description

company_url = "https://jobs.lever.co/openai"

print("🔍 Step 1: Finding job links...\n")

job_links = get_job_links(company_url)

print("Found jobs:", len(job_links))

for url in job_links[:3]:
    print("\n🔗 Scraping:", url)
    result = scrape_job_description(url)

    if isinstance(result, dict):
        print(result)
    else:
        print(result[:500])
