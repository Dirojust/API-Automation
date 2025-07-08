@organizations
Feature:  Suite for organizations endpoint from TRELLO API

  @acceptance @organization_id
  Scenario: Scenario to get an Organization
    When user calls "GET" method to "get" "organizations" endpoint
    Then the status code is 200

  @acceptance
  Scenario: Scenario to create an Organization
  When user calls "POST" method to "create" "organizations" endpoint using json
  """
    {
      "displayName": "organization from feature file"
    }
  """
  Then the status code is 200

  @acceptance @organization_id
  Scenario: Scenario to update an Organization
  When user calls "PUT" method to "update" "organizations" endpoint using json
  """
    {
      "displayName": "update organization from feature file"
    }
  """
  Then the status code is 200

  @acceptance @organization_id
  Scenario: Scenario to delete an Organization
    When user calls "DELETE" method to "delete" "organizations" endpoint
    Then the status code is 200

  @functional
  Scenario: create an Organization without body
    When user calls "POST" method to "create" "organizations" endpoint without body
    Then the status code is 400