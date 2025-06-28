import json
import logging
from utils.logger import get_logger
from config.config import url_base, auth_params
from helper.rest_client import RestClient
from helper.validate_Response import ValidateResponse

LOGGER = get_logger(__name__, logging.DEBUG)

class TestCards:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    def test_create_card(self, test_log_name, create_list):
        """
        Test for create a card
        :param test_log_name:  log the test name
        """
        # body
        request_body = {
            "name": "Card from Pycharm",
            "idList": f"{create_list}"
        }

        # url for create the card
        url_create_card = f"{url_base}cards"
        LOGGER.debug(f"url_create_card: {url_create_card}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_card,
            params=auth_params,
            body=request_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["name"] == "Card from Pycharm"
        self.validate.validate_response(response, "create_card")
