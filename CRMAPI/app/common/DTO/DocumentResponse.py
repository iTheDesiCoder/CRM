from pydantic import BaseModel
from .BaseResponse import BaseResponse
from typing import List


class Document(BaseModel):
    name: str
    doc_text: List[str]

    def to_dict(self):
        return self.dict()


class DocumentResponse(BaseResponse):
    documents: List[Document]

    def to_dict(self):
        return self.dict()
