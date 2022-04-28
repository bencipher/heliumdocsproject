from typing import Optional
from pydantic import BaseModel


class ResponseParserModel(BaseModel):
    title: str
    link: str
    source: Optional[str]
