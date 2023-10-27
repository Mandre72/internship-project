# Created by matthewandre at 10/26/23
Feature: User can open the community page

  Scenario: User can open the community page
    Given Open the main page
    When Login to the page
    And Click on menu option
    And Click on Community option
    Then Verify the Community page opens
    And Verify two articles are available
