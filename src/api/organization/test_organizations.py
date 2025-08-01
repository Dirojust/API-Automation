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

@allure.story("Organization")
@allure.parent_suite("Organization")
class TestOrganizations:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.organizationId_list = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Organization")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_create_organization(self, test_log_name):
        """
        Test for create an organization
        :param test_log_name:  log the test name
        """
        # body
        request_body = {
            "displayName": "Organization from Pycharm"
        }

        # url for create the organization
        url_create_organization = f"{url_base}organizations"
        LOGGER.debug(f"url_create_organization: {url_create_organization}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_organization,
            params=auth_params,
            body=request_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        self.organizationId_list.append(response_json["id"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["displayName"] == "Organization from Pycharm"
        self.validate.validate_response(response, "create_organization")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Get Organization")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_get_organization(self, create_organization, test_log_name):
        """
        Test for get an organization
        :param create_organization:   (str) Id of the organization
        :param test_log_name:    (str) log the test name
        """
        # url for get the organization
        url_get_organization = f"{url_base}organizations/{create_organization}"
        LOGGER.debug(f"url_get_organization: {url_get_organization}")

        # call GET endpoint
        response = self.rest_client.send_request(
            method_name="GET",
            url=url_get_organization,
            params=auth_params
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        self.validate.validate_response(response, "get_organization")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Update Organization")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_update_organization(self, create_organization, test_log_name):
        """
        Test for update an organization
        :param create_organization: (str) Id of the organization
        :param test_log_name:  (str) log the test name
        """
        # body
        resquest_body = {
            "displayName": "Organization from Pycharm - UPDATED :)"
        }

        # url for update the organization
        url_update_organization = f"{url_base}organizations/{create_organization}"
        LOGGER.debug(f"url_update_organization: {url_update_organization}")

        # call PUT endpoint
        response = self.rest_client.send_request(
            method_name="PUT",
            url=url_update_organization,
            params=auth_params,
            body=resquest_body
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        assert response["status_code"] == 200
        assert "id" in response_json
        assert response_json["displayName"] == "Organization from Pycharm - UPDATED :)"
        self.validate.validate_response(response, "update_organization")

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Delete Organization")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Diana Rojas")
    def test_delete_organization(self, create_organization, test_log_name):
        """
        Test for delete an organization
        :param create_organization:  (str) Id of the organization
        :param test_log_name:   (str) log the test name
        """
        # url for delete the organization
        url_delete_organization = f"{url_base}organizations/{create_organization}"
        LOGGER.debug(f"url_delete_organization: {url_delete_organization}")

        # call DELETE endpoint
        response = self.rest_client.send_request(
            method_name="DELETE",
            url=url_delete_organization,
            params=auth_params
        )

        # assertion
        assert response["status_code"] == 200
        self.validate.validate_response(response, "delete_organization")

    # Functional tests
    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Organization Without Body")
    @allure.tag("functional", "negative")
    @allure.label("owner", "Diana Rojas")
    def test_create_organization_without_body(self, test_log_name):
        """
        Test for create an organization without body
        :param test_log_name:  log the test name
        """
        # url for create the organization
        url_create_organization = f"{url_base}organizations"
        LOGGER.debug(f"url_create_organization: {url_create_organization}")

        # call POST endpoint
        response = self.rest_client.send_request(
            method_name="POST",
            url=url_create_organization,
            params=auth_params
        )

        response_json = response["body"]
        LOGGER.debug("Response: %s", json.dumps(response_json, indent=4))
        LOGGER.debug("Status Code: %s", response["status_code"])

        # assertion
        self.validate.validate_response(response, "create_organization_without_body")


    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup organizations
        LOGGER.info("Test organization teardown Class")
        for organization_id in cls.organizationId_list:
            url_delete_organization = f"{url_base}organizations/{organization_id}"
            LOGGER.debug(f"url_delete_organization: {url_delete_organization}")
            response = requests.delete(
                url=url_delete_organization,
                params=auth_params
            )
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 200:
                LOGGER.debug("Organization deleted")