import json
import logging

from helper.rest_client import RestClient
from helper.validate_Response import ValidateResponse
from utils.logger import get_logger
from config.config import auth_params
from behave import when, then, step

LOGGER = get_logger(__name__, logging.DEBUG)

rest_client = RestClient()
validator = ValidateResponse()

def get_feature_id(endpoint_name, context):
    LOGGER.debug("Feature id %s", endpoint_name)
    feature_id = None
    if endpoint_name == "boards":
        feature_id = context.board_id
    elif endpoint_name == "organizations":
        feature_id = context.organization_id
    elif endpoint_name == "lists":
        feature_id = context.list_id
    return feature_id

def update_json_data(context, body):
    mapping = {
        "idBoard": "board_id",
        "idList": "list_id"
    }
    LOGGER.debug("Method update json data")
    for body_key, context_key in mapping.items():
        if body_key in body and hasattr(context, context_key):
            body[body_key] = getattr(context, context_key)
            LOGGER.debug("Key changed %s", body_key)
    LOGGER.debug("Update body %s", body)
    return body

def append_to_feature_list(endpoint_name, context, feature_id):
    if endpoint_name == "boards":
        context.board_list.append(feature_id)
    elif endpoint_name == "organizations":
        context.organization_list.append(feature_id)

# Steps Definitions
@when('user calls "{method}" method to "{action}" "{endpoint_name}" endpoint')
def call_endpoints(context, method, action, endpoint_name):
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    feature_id = get_feature_id(endpoint_name, context)
    url_get = f"{context.url_base}{endpoint_name}/{feature_id}"
    response = rest_client.send_request(
        method,
        url=url_get,
        params=auth_params
    )
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]
    context.response = response


@when('user calls "{method}" method to "{action}" "{endpoint_name}" endpoint using json')
def call_endpoints_with_json(context, method, action, endpoint_name):
    LOGGER.debug("JSON: %s", context.text)
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    url_create = f"{context.url_base}{endpoint_name}"
    if action == "update":
        feature_id = get_feature_id(endpoint_name, context)
        url_create = f"{context.url_base}{endpoint_name}/{feature_id}"
    body = json.loads(context.text)
    
    body_updated = update_json_data(context, body)

    response = rest_client.send_request(
        method, url=url_create,
        params=auth_params,
        body=body_updated
    )
    # add to list of boards for clean up
    LOGGER.debug("Response %s", response)
    if action == "create" and "id" in response["body"]:
        append_to_feature_list(endpoint_name, context, response["body"]["id"])
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]
    context.response = response


@then("the status code is {status_code:d}")
def verify_status_code(context, status_code):
    LOGGER.debug("Step verify status code %s", status_code)
    assert context.status_code == status_code


@when('user calls "{method}" method to "{action}" "{endpoint_name}" endpoint without body')
def call_endpoint_without_body(context, method, action, endpoint_name):
    LOGGER.debug("Step %s using %s method WITHOUT body", endpoint_name, method)
    url = f"{context.url_base}boards"

    response = rest_client.send_request(
        method,
        url=url,
        params=auth_params,
        body=None
    )

    LOGGER.debug(response)
    context.status_code = response["status_code"]
    context.response = response

@step('the response is validated with "{json_file}" file')
def validate_json(context, json_file):
    validator.validate_response(context.response, json_file)