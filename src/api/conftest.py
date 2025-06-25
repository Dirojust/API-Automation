import logging
import pytest
import os

import requests

from utils.logger import get_logger
from config.config import url_base, auth_params

LOGGER = get_logger(__name__, logging.DEBUG)

@pytest.fixture
def create_board():
    request_body = {
        "name": "Test Board from fixture",
    }

    url_base = os.getenv("URL_BASE")
    response = requests.post(
        url=f"{url_base}boards",
        params=auth_params,
        json=request_body
    )

    LOGGER.debug(response.json())

    board_id = response.json()["id"]
    yield board_id
    delete_board(board_id)

@pytest.fixture
def create_organization():
    request_body = {
        "displayName": "Test Organization from fixture",
    }

    url_base = os.getenv("URL_BASE")
    response = requests.post(
        url=f"{url_base}organizations",
        params=auth_params,
        json=request_body
    )

    LOGGER.debug(response.json())

    organization_id = response.json()["id"]
    yield organization_id
    delete_organization(organization_id)

def delete_organization(organization_id):
    url_delete_organization = f"{url_base}organizations/{organization_id}"
    LOGGER.debug(f"url_delete_organization: {url_delete_organization}")

    response = requests.delete(
        url=url_delete_organization,
        params=auth_params
    )

@pytest.fixture
def test_log_name(request):
    LOGGER.info(f"Start Test '{request.node.name}'")
    def fin():
        LOGGER.info(f"End Test '{request.node.name}'")
    request.addfinalizer(fin)

def delete_board(board_id):
    url_delete_board = f"{url_base}boards/{board_id}"
    LOGGER.debug(f"url_delete_board: {url_delete_board}")

    response = requests.delete(
        url=url_delete_board,
        params=auth_params
    )

