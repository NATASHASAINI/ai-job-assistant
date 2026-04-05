import requests
from bs4 import BeautifulSoup

def scrape_job_description(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())

