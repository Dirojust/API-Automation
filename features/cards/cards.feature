@cards
Feature: Suite for cards endpoint from TRELLO API

  @normal
  @allure.label.owner:Diana_Rojas
  @allure.link:https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
  @acceptance @board_id @list_id
  Scenario: Scenario to create a Card
  When user calls "POST" method to "create" "cards" endpoint using json
  """
    {
      "name": "Card from feature file",
      "idList": "list_id"
    }
  """
  Then the status code is 200