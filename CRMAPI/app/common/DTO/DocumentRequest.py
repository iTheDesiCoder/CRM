from pydantic import BaseModel
from typing import List


class DocumentBase64(BaseModel):
    name: str
    base64_pdf: str

    def to_dict(self):
        return self.dict()


class DocumentRequest(BaseModel):
    documents: List[DocumentBase64]

    def to_dict(self):
        return self.dict()
