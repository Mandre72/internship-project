# Created by matthewandre at 10/12/23
Feature: User can open the community page

  Scenario: User can open the community page
    Given Open the main page
    When Log in to the page
    And Click on settings option
    And Click on Community option
    Then Verify the Community page opens
    And Verify at least two articles are available


