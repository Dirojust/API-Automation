import requests
import logging
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class RestClient:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method_name, url, params=None, body=None):
        response_data = {}
        methods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "PUT": self.session.put,
            "DELETE": self.session.delete,
        }

        try:
            response = methods[method_name](
                url=url,
                params=params,
                json=body,
            )
            response.raise_for_status()
            response_data["body"] = response.json() if response.text else {"message": "No content"}
            response_data["status_code"] = response.status_code

        except requests.exceptions.HTTPError as e:
            LOGGER.error("HTTP Error: %s", e)
            response_data["body"] = response.json() if response.text else {"message": "HTTP Error"}
            response_data["status_code"] = response.status_code
            response_data["headers"] = dict(response.headers)

        return response_data
