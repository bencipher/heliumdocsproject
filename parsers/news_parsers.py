from core.models import ResponseParserModel


def reddit_parser(results):
    """
    :param results: JSON Object
    :return: List of dictionaries
            [
                {
                    "title": "title of the news",
                    "link": "original link of the news source",
                    "source":"your-api-name"
                },
            ...
            ]
    """
    response = []
    for child in results["data"]["children"]:
        extract = {
            "title": child["data"]["title"],
            "link": child["data"]["url"],
            "source": "reddit"
        }
        ResponseParserModel(**extract)
        response.append(extract)
    return response


def newsapi_parser(results):
    """
    :param results: JSON Object
    :return: List of dictionaries
            [
                {
                    "title": "title of the news",
                    "link": "original link of the news source",
                    "source":"your-api-name"
                },
            ...
            ]
    """
    response = []
    for child in results["articles"]:
        extract = {
            "title": child["title"],
            "link": child["url"],
            "source": "newsapi"
        }
        ResponseParserModel(**extract)
        response.append(extract)
    return response
