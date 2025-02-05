from pydantic import BaseModel
from .BaseResponse import BaseResponse


class CompletionResponse(BaseResponse):
    completion_content: str

    def to_dict(self):
        return self.dict()
