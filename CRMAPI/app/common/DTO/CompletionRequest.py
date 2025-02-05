from pydantic import BaseModel


class CompletionRequest(BaseModel):
    query: str
    context: str

    def to_dict(self):
        return self.dict()
