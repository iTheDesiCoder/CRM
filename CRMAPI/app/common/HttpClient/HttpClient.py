import httpx
from injector import singleton
from app.common.Logging import logger


@singleton
class HttpClient:

    def __init__(self):
        self.client = httpx.Client()

    def post(self, url, data=None, json=None, **kwargs):
        logger.debug(f"Sending POST request to {url} with data {data or json}")
        response = self.client.post(url, data=data, json=json, **kwargs)
        logger.debug(f"Received response with status code {response.status_code}")
        return response

    def get(self, url, params=None, **kwargs):
        logger.debug(f"Sending GET request to {url} with params {params}")
        response = self.client.get(url, params=params, **kwargs)
        logger.debug(f"Received response with status code {response.status_code}")
        return response
