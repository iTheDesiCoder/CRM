from fastapi.responses import JSONResponse
from app.common.Logging import logger
from app.common.DTO.BaseResponse import BaseResponse


class GlobalExceptionHandler:

    @staticmethod
    async def exception_handler(request, exc):
        if request is not None:
            logger.error(f"An error occurred: {str(exc)} with request {request}")
        else:
            logger.error(f"An error occurred: {str(exc)}")
        base_response = BaseResponse(status=False, message=str(exc))
        return JSONResponse(
            status_code=500,
            content=base_response.to_dict(),
        )
