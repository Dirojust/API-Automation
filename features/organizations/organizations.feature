@organizations
Feature:  Suite for organizations endpoint from TRELLO API

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-get
  @acceptance @organization_id
  Scenario: Scenario to get an Organization
    When user calls "GET" method to "get" "organizations" endpoint
    Then the status code is 200

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-post
  @acceptance
  Scenario: Scenario to create an Organization
  When user calls "POST" method to "create" "organizations" endpoint using json
  """
    {
      "displayName": "organization from feature file"
    }
  """
  Then the status code is 200

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-put
  @acceptance @organization_id
  Scenario: Scenario to update an Organization
  When user calls "PUT" method to "update" "organizations" endpoint using json
  """
    {
      "displayName": "update organization from feature file"
    }
  """
  Then the status code is 200

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-delete
  @acceptance @organization_id
  Scenario: Scenario to delete an Organization
    When user calls "DELETE" method to "delete" "organizations" endpoint
    Then the status code is 200

  @normal
  @allure.label.owner:Diana_Rojas
  @functional @negative
  Scenario: create an Organization without body
    When user calls "POST" method to "create" "organizations" endpoint without body
    Then the status code is 400