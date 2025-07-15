@boards
Feature:  Suite for boards endpoint from TRELLO API

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-get
  @acceptance @board_id
  Scenario: Scenario to get a Board
    When user calls "GET" method to "get" "boards" endpoint
    Then the status code is 200
    And the response is validated with "get_board" file

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-post
  @acceptance
  Scenario: Scenario to create a Board
  When user calls "POST" method to "create" "boards" endpoint using json
  """
    {
      "name": "board from feature file"
    }
  """
  Then the status code is 200
    And the response is validated with "create_board" file

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-put
  @acceptance @board_id
  Scenario: Scenario to update a Board
  When user calls "PUT" method to "update" "boards" endpoint using json
  """
    {
      "name": "update board from feature file"
    }
  """
  Then the status code is 200
    And the response is validated with "update_board" file

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-delete
  @acceptance @board_id
  Scenario: Scenario to delete a board
    When user calls "DELETE" method to "delete" "boards" endpoint
    Then the status code is 200
    And the response is validated with "delete_board" file

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:
  @functional @negative
  Scenario: create a board without body
    When user calls "POST" method to "create" "boards" endpoint without body
    Then the status code is 400
    And the response is validated with "create_board_without_body" file