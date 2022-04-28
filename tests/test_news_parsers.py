import pytest
from parsers.news_parsers import newsapi_parser, reddit_parser
from tests.testdata.datadump import news_api_dump, reddit_dump


@pytest.mark.parametrize("value",
                         [{"parser": reddit_parser, "data": reddit_dump},
                          {"parser": newsapi_parser, "data": news_api_dump}])
def test_parsers(value):
    result = value["parser"](value["data"])
    assert all(r in result[0] for r in ["title", "link", "source"])
    assert all(r["title"] for r in result)
