import re
from urllib.parse import urlparse

import requests

from .base import ScoringFactor

TRUSTPILOT_BASE_URL = "https://www.trustpilot.com"
USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0"
}
HTML_PARSER = "html.parser"
TRUSTSCORE_PATTERN = re.compile(r"TrustScore (\d+(\.\d+)?) out of 5")


class TrustpilotFactor(ScoringFactor):
    def score(self, url: str, content="") -> list[int, list[str]]:
        try:
            cleaned = urlparse(url).netloc
            if "www" not in cleaned:
                cleaned = "www." + cleaned
            url = TRUSTPILOT_BASE_URL + "/review/" + cleaned
            resp = requests.get(url, headers=USER_AGENT)
            web_page = resp.text
            match = TRUSTSCORE_PATTERN.search(web_page)
            if match:
                trust_score = match.group(1)  # Extract the trust score number
                print(f"TrustScore found: {trust_score} out of 5")
            else:
                print("TrustScore no match, this site should exist")
                return 50, ["No TrustScore rating"]
            trust_score_new = trust_score[0] + trust_score[2]  # 4.5 -> 45
            return 50 - int(trust_score_new), [f"TrustScore rating: {trust_score}"]
        except Exception as e:
            print(f"Error while checking trustpilot: {str(e)}")
            return 50, ["Failed to get TrustScore records"]
