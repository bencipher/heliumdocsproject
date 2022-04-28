import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import applications

from libs.news_extractor import NewsExtractor
from patch.swagger_patch import swagger_monkey_patch

app = FastAPI()
logger = logging.getLogger(__name__)
applications.get_swagger_ui_html = swagger_monkey_patch


# === Application Main Endpoint
@app.get("/")
def hello():
    return {"message": "Welcome to HeliumDocs"}


@app.get("/news")
async def news_aggregator(query: str = None, limit: int = 10):
    """
    Top level endpoint to get top news or news from search query
    :param query: Search query in request url.
    :param limit: Integer number to limit number of results to fetch from each dependent API.
    :return: JSON response of aggregated results.
    """
    new_extractor = NewsExtractor()
    try:
        if query:
            # call search endpoint
            result = new_extractor.search_news(query, limit)
        else:
            # call top news endpoint
            result = new_extractor.get_top_news(limit)
        return result
    except Exception as e:
        logger.error('Error Occurred while loading news', exc_info=True)
        raise HTTPException(detail="Error Occurred while loading news", status_code=404)


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
