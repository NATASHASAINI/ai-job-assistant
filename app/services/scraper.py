import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ----------------------------
# STEP 1: Get job links
# ----------------------------
def get_job_links(company_url: str):
    response = requests.get(company_url, headers=HEADERS)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        # keep only job links
        if "lever.co" in href and href != company_url:
            links.add(href)

    return list(links)


# ----------------------------
# STEP 2: Scrape job page
# ----------------------------
def scrape_job_description(job_url: str):
    response = requests.get(job_url, headers=HEADERS)

    if response.status_code != 200:
        return {"error": "Job page not accessible"}

    if "job you're looking for" in response.text.lower():
        return {"error": "Job expired or removed"}

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator="\n")

    return text
