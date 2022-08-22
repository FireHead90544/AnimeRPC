import requests
from bs4 import BeautifulSoup
from typing import List, Dict

class GogoAnimeClient:
    """
    The Client class which scrapes gogoanime for anime info.

    Available Methods:
    - get_current_domain
    - search
    """
    def __init__(self) -> None:
        self.session = requests.Session()
        self.MAIN_DOMAIN = "https://gogoanime.pe"
        self.BASE = self.get_current_domain()

    def get_current_domain(self) -> str:
        """Get current gogoanime domain."""
        return self.session.get(self.MAIN_DOMAIN).url[0:-1]

    def search(self, query: str) -> List[Dict]:
        """Search for the given query and get results as a list of dictionaries.
        Each dictionary contains the following keys:
            - title: str
            - url: str
            - image_url: str
            - released: int
        """
        url = f"{self.BASE}/search.html?keyword={query}"
        soup = BeautifulSoup(self.session.get(url).content, 'html.parser')
        results = soup.select('#wrapper_bg > section > section.content_left > div > div.last_episodes > ul > li')
        animes = []
        for item in results:
            try:
                animes.append({
                    "title": item.div.a['title'].strip(),
                    "url": self.BASE + item.div.a['href'].strip(),
                    "image_url": item.div.img['src'].strip(),
                    "released": int(item.find('p', {'class': 'released'}).getText().strip().replace("Released: ", ""))
                })
            except Exception:
                pass

        return animes
