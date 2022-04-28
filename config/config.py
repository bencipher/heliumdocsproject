import functools

from decouple import config

from parsers.news_parsers import newsapi_parser, reddit_parser

NEWS_API_KEY = config('NEWS_API_KEY')


@functools.lru_cache
def get_api_mapping():
    return {
        "REDDIT": {
            "api_name": "reddit",
            "parser": reddit_parser,
            "list_url": ('https://www.reddit.com/r/news/top.json?'
                         'limit={limit}'),
            "search_url": ('https://www.reddit.com/r/news/search.json?'
                           'q={query}&'
                           'limit={limit}')
        },
        "NEWS": {
            "api_name": "newsapi",
            "parser": newsapi_parser,
            "list_url": 'http://newsapi.org/v2/top-headlines?category=general&pageSize={limit}&page=1&' +
                        'apiKey={api_key}'.format(api_key=NEWS_API_KEY),
            "search_url": 'http://newsapi.org/v2/everything?q={query}&pageSize={limit}&page=1&' +
                          'apiKey={api_key}'.format(api_key=NEWS_API_KEY)
        }
    }
