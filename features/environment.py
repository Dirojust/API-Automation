import logging

from helper.rest_client import RestClient
from utils.logger import get_logger
from config.config import url_base, auth_params

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
     Setup before all Features.
    :param context:  Object  stores test data
    """

    LOGGER.debug("Before all tests")
    context.url_base = url_base
    context.rest_client = RestClient()
    context.board_list = []
    context.organization_list = []
    context.list_list = []


def before_feature(context, feature):
    """
    Setup before feature.
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("Before feature")


def before_scenario(context, scenario):
    """
    Setup before scenario.
    :param context:
    :param scenario:
    """
    LOGGER.debug('Starting scenario: "%s"', scenario.name)

    # create a board
    LOGGER.debug("SCENARIO TAGS %s", scenario.tags)
    if "board_id" in scenario.tags:
        board_body = {
            "name": "Board before scenario",
        }
        LOGGER.debug("create board")
        response = context.rest_client.send_request(
            "POST",
            url=f"{context.url_base}boards",
            params=auth_params,
            body=board_body,
        )
        context.board_id = response["body"]["id"]
        context.board_list.append(context.board_id)
        LOGGER.debug("Board ID: %s", response["body"]["id"])

    if "organization_id" in scenario.tags:
        organization_body = {
            "displayName": "Organization before scenario",
        }
        LOGGER.debug("create organization")
        response = context.rest_client.send_request(
            "POST",
            url=f"{context.url_base}organizations",
            params=auth_params,
            body=organization_body,
        )
        context.organization_id = response["body"]["id"]
        LOGGER.debug(f"Appending ID {response['body']['id']} to organization_list")
        context.organization_list.append(context.organization_id)
        LOGGER.debug("Organization ID: %s", response["body"]["id"])

    if "list_id" in scenario.tags:
        list_body = {
            "name": "List name",
            "idBoard": f"{context.board_id}",
        }
        LOGGER.debug("create list")
        response = context.rest_client.send_request(
            "POST",
            url=f"{context.url_base}lists",
            params=auth_params,
            body=list_body,
        )
        context.list_id = response["body"]["id"]
        context.list_list.append(context.list_id)
        LOGGER.debug("List ID: %s", response["body"]["id"])


def after_scenario(context, scenario):
    """
    Tear down after the scenario.
    :param context:
    :param scenario:
    :return:
    """
    LOGGER.debug('AFTER SCENARIO: Ending scenario: "%s"', scenario.name)

def after_feature(context, feature):
    """
    Tear down after feature.
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("After feature")

def after_all(context):
    """
    Tear down after all.
    :param context:
    :return:
    """
    LOGGER.debug("After all - Cleanup all")
    for board_id in context.board_list:
        LOGGER.debug(f"Deleting board ID: {board_id}")
        url_delete_board = f"{context.url_base}boards/{board_id}"
        try:
            response = context.rest_client.send_request(
                "DELETE", url=url_delete_board, params=auth_params
            )
            if response["status_code"] == 200:
                LOGGER.debug("Board %s deleted", board_id)
            else:
                LOGGER.warning("Failed to delete board %s: status %s", board_id, response["status_code"])
        except Exception as e:
            LOGGER.error(f"Exception while deleting board {board_id}: {e}")

    for organization_id in context.organization_list:
        LOGGER.debug(f"Deleting organization ID: {organization_id}")
        url_delete_organization = f"{context.url_base}organizations/{organization_id}"
        try:
            response = context.rest_client.send_request(
                "DELETE", url=url_delete_organization, params=auth_params
            )
            if response["status_code"] == 200:
                LOGGER.debug("Organization %s deleted", organization_id)
            else:
                LOGGER.warning("Failed to delete organization %s: status %s", organization_id, response["status_code"])
        except Exception as e:
            LOGGER.error(f"Exception while deleting organization {organization_id}: {e}")