from typing import Dict, List
import requests
from config.config import get_api_mapping


class NewsExtractor:

    def __init__(self):
        self.API_MAPPING = get_api_mapping()

    def get_top_news(self, limit: int) -> List[Dict]:
        """
        This function will get top news.
        :param limit: Integer number to limit number of responses from each API.
        :return: Return aggregated news results.
        """
        response = []
        for name, api in self.API_MAPPING.items():
            result = requests.get(api["list_url"].format(limit=limit),
                                  headers={'User-agent': 'your bot 0.1'}).json()
            if result:
                response += api["parser"](result)
        return response

    def search_news(self, query: str, limit: int) -> List[Dict]:
        """
         This function will get search results for any given QUERY.
        :param query: Search Query.
        :param limit: Integer number to limit number of responses from each API.
        :return: Return aggregated news results.
        """
        response = []
        for name, api in self.API_MAPPING.items():
            result = requests.get(api["search_url"].format(query=query, limit=limit),
                                  headers={'User-agent': 'your bot 0.1'}).json()
            if result:
                response += api["parser"](result)
        return response
