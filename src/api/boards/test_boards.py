import json
import logging
import allure
import pytest
import requests
from utils.logger import get_logger
from config.config import url_base, auth_params
from helper.rest_client import RestClient
from helper.validate_Response import ValidateResponse

LOGGER = get_logger(__name__, logging.DEBUG)

@allure.story("Boards")
@allure.parent_suite("Boards")
class TestBoards:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.boardId_list = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Board")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_create_board(self, test_log_name):
        """
        Test for create a board
        :param test_log_name:  log the test name
        """
        # body
        request_body = {
            "name": "Board from Pycharm :)"
        }

        # url for create the board
        url_create_board = f"{url_base}boards"
        LOGGER.debug(f"url_create_board: {url_create_board}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_board,
            params=auth_params,
            body=request_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        self.boardId_list.append(response_json["id"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["name"] == "Board from Pycharm :)"
        self.validate.validate_response(response, "create_board")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Get Board")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_get_board(self, create_board, test_log_name):
        """
        Test for get a board
        :param create_board:   (str) Id of the board
        :param test_log_name:    (str) log the test name
        """
        # url for get the board
        url_get_board = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_get_board: {url_get_board}")

        # call GET endpoint
        response = self.rest_client.send_request(
            method_name="GET",
            url=url_get_board,
            params=auth_params
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        self.validate.validate_response(response, "get_board")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Update Board")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_update_board(self, create_board, test_log_name):
        """
        Test for update a board
        :param create_board: (str) Id of the board
        :param test_log_name:  (str) log the test name
        """
        # body
        resquest_body = {
            "name": "Board from Pycharm - UPDATED :)"
        }

        # url for update the board
        url_update_board = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_update_board: {url_update_board}")

        # call PUT endpoint
        response = self.rest_client.send_request(
            method_name="PUT",
            url=url_update_board,
            params=auth_params,
            body=resquest_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["name"] == "Board from Pycharm - UPDATED :)"
        self.validate.validate_response(response, "update_board")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Delete Board")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_delete_board(self, create_board, test_log_name):
        """
        Test for delete a board
        :param create_board:  (str) Id of the board
        :param test_log_name:   (str) log the test name
        """
        # url for delete the board
        url_delete_board = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_delete_board: {url_delete_board}")

        # call DELETE endpoint
        response = self.rest_client.send_request(
            method_name="DELETE",
            url=url_delete_board,
            params=auth_params
        )

        # assertion
        self.validate.validate_response(response, "delete_board")


    #Functional tests
    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Board Without Body")
    @allure.tag("functional", "negative")
    @allure.label("owner", "Diana Rojas")
    def test_create_board_without_body(self, test_log_name):
        """
        Test for create a board without body
        :param test_log_name:  log the test name
        """
        # url for create the board
        url_create_board = f"{url_base}boards"
        LOGGER.debug(f"url_create_board: {url_create_board}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_board,
            params=auth_params
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        self.validate.validate_response(response, "create_board_without_body")

     #Teardown
    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup boards
        LOGGER.info("Test Boards teardown Class")
        for board_id in cls.boardId_list:
            url_delete_board = f"{url_base}boards/{board_id}"
            LOGGER.debug(f"url_delete_board: {url_delete_board}")
            response = requests.delete(
                url=url_delete_board,
                params=auth_params
            )
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 200:
                LOGGER.debug("Board deleted")