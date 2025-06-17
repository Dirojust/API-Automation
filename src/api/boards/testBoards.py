import json
import logging
import requests
from utils.logger import get_logger
from config.config import url_base, auth_params

LOGGER = get_logger(__name__, logging.DEBUG)

class TestProject:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.boardId_list = []

    def test_create_project(self, test_log_name):
        project_body = {
            "name": "Test Project from Pycharm :)"
        }

        url_create = f"{url_base}boards"
        LOGGER.debug(f"url_create_project: {url_create}")

        response = requests.post(
            url=url_create,
            params=auth_params,
            json=project_body
        )

        response_json = response.json()
        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))
        self.boardId_list.append(response.json()["id"])

        assert response.status_code == 200
        assert "id" in response_json
        assert response_json["name"] == "Test Project from Pycharm :)"

    def test_get_project(self, create_board, test_log_name):
        url_get_project = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_get_project: {url_get_project}")

        response = requests.get(
            url=url_get_project,
            params=auth_params
        )

        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))

        assert response.status_code == 200

    def test_update_project(self, create_board, test_log_name):
        url_update_project = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_update_project: {url_update_project}")

        project_body = {
            "name": "Test Project from Pycharm - UPDATED :)"
        }

        response = requests.put(
            url=url_update_project,
            params=auth_params,
            json=project_body
        )

        response_json = response.json()
        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))

        assert response.status_code == 200
        assert "id" in response_json
        assert response_json["name"] == "Test Project from Pycharm - UPDATED :)"

    def test_delete_project(self, create_board, test_log_name):
        url_delete_project = f"{url_base}boards/{create_board}"
        LOGGER.debug(f"url_delete_project: {url_delete_project}")

        response = requests.delete(
            url=url_delete_project,
            params=auth_params
        )

        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))

        assert response.status_code == 200

    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup projects
        LOGGER.info("Test Project teardown Class")
        for board_id in cls.boardId_list:
            url_delete_project = f"{url_base}boards/{board_id}"
            LOGGER.debug(f"url_delete_project: {url_delete_project}")
            response = requests.delete(
                url=url_delete_project,
                params=auth_params
            )
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 200:
                LOGGER.debug("Project deleted")