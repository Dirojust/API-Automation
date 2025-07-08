@lists
Feature: Suite for lists endpoint from TRELLO API

  @acceptance @board_id @list_id
  Scenario: Scenario to get a List
    When user calls "GET" method to "get" "lists" endpoint
    Then the status code is 200


  @acceptance @board_id
  Scenario: Scenario to create a List
  When user calls "POST" method to "create" "lists" endpoint using json
  """
    {
      "name": "List from feature file",
      "idBoard": "board_id"
    }
  """
  Then the status code is 200