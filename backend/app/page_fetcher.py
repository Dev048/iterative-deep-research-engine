import requests
from bs4 import BeautifulSoup


def fetch_page_text(url: str):

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = [p.get_text() for p in soup.find_all("p")]

        text = "\n".join(paragraphs)

        return text[:20000]

    except Exception:
        return ""