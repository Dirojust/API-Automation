@cards
Feature: Suite for cards endpoint from TRELLO API

  @acceptance @board_id @list_id
  Scenario: Scenario to create a List
  When user calls "POST" method to "create" "cards" endpoint using json
  """
    {
      "name": "Card from feature file",
      "idList": "list_id"
    }
  """
  Then the status code is 200