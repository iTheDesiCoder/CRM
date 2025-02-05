from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: bool
    message: str = None

    def to_dict(self):
        return self.dict()
