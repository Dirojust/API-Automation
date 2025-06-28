import json
import logging
from utils.logger import get_logger
from config.config import url_base, auth_params
from helper.rest_client import RestClient
from helper.validate_Response import ValidateResponse

LOGGER = get_logger(__name__, logging.DEBUG)

class TestLists:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    def test_create_list(self, test_log_name, create_board):
        """
        Test for create a list
        :param test_log_name:  log the test name
        """
        # body
        request_body = {
            "name": "List from Pycharm",
            "idBoard": f"{create_board}"
        }

        # url for create the list
        url_create_list = f"{url_base}lists"
        LOGGER.debug(f"url_create_list: {url_create_list}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_list,
            params=auth_params,
            body=request_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["name"] == "List from Pycharm"
        self.validate.validate_response(response, "create_list")

    def test_get_list(self, create_list, test_log_name):
        """
        Test for get a list
        :param create_list: (str) Id of the list
        :param test_log_name:    (str) log the test name
        """
        # url for get the list
        url_get_list = f"{url_base}lists/{create_list}"
        LOGGER.debug(f"url_get_list: {url_get_list}")

        # call GET endpoint
        response = self.rest_client.send_request(
            method_name="GET",
            url=url_get_list,
            params=auth_params
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        self.validate.validate_response(response, "get_list")