import logging
import pytest
import os

import requests

from utils.logger import get_logger
from config.config import url_base, auth_params
from dotenv import load_dotenv

LOGGER = get_logger(__name__, logging.DEBUG)

@pytest.fixture
def create_board():
    project_body = {
        "name": "Test Board from fixture",
    }

    url_base = os.getenv("URL_BASE")
    response = requests.post(
        url=f"{url_base}boards",
        params=auth_params,
        json=project_body
    )

    LOGGER.debug(response.json())

    project_id = response.json()["id"]
    yield project_id
    delete_board(project_id)

@pytest.fixture
def test_log_name(request):
    LOGGER.info(f"Start Test '{request.node.name}'")
    def fin():
        LOGGER.info(f"End Test '{request.node.name}'")
    request.addfinalizer(fin)

def delete_board(project_id):
    url_delete_project = f"{url_base}boards/{project_id}"
    LOGGER.debug(f"url_delete_project: {url_delete_project}")

    response = requests.delete(
        url=url_delete_project,
        params=auth_params
    )

