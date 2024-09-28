import requests
from bs4 import BeautifulSoup

from factors.base import ScoringFactor


class SocialDetector(ScoringFactor):

    def __init__(self, debug: bool = True):
        self.debug: bool = debug

    def score(self, url: str, content: str = "") -> int:
        score = 0
        try:
            socials = ["facebook", "instagram"]
            points_per_social = 100 / len(socials)
            soup = BeautifulSoup(content, "html.parser")
            links = soup.find_all("a")
            for link in links:
                if link is None:
                    continue
                for social in socials:
                    score += points_per_social
                    socials.remove(social)
        except Exception as e:
            if self.debug:
                print(f"Error while checking socials: {str(e)}")
        return int(score)
