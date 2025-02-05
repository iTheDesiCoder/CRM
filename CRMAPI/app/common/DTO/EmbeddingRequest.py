from pydantic import BaseModel


class EmbeddingRequest(BaseModel):
    text: str

    def to_dict(self):
        return self.dict()
