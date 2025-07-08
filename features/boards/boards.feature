@boards
Feature:  Suite for boards endpoint from TRELLO API

  @acceptance @board_id
  Scenario: Scenario to get a Board
    When user calls "GET" method to "get" "boards" endpoint
    Then the status code is 200

  @acceptance
  Scenario: Scenario to create a Board
  When user calls "POST" method to "create" "boards" endpoint using json
  """
    {
      "name": "board from feature file"
    }
  """
  Then the status code is 200

  @acceptance @board_id
  Scenario: Scenario to update a Board
  When user calls "PUT" method to "update" "boards" endpoint using json
  """
    {
      "name": "update board from feature file"
    }
  """
  Then the status code is 200

  @acceptance @board_id
  Scenario: Scenario to delete a board
    When user calls "DELETE" method to "delete" "boards" endpoint
    Then the status code is 200

  @functional
  Scenario: create a board without body
    When user calls "POST" method to "create" "boards" endpoint without body
    Then the status code is 400
    And the response is validated with "create_board_without_body" file