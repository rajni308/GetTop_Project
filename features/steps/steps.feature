# Created by rajni at 7/16/22
Feature: # A test to verify search bar works

  Scenario:  Verify user can search existing product

    Given Open home page
    When Mouse hover on search icon
    And Search for watch
    Then Click on search icon
    And Verify search results have watch




Scenario:  Verify user can search non existing product and sees error message

    Given Open home page
    When Mouse hover on search icon
    And Search for dress
    Then Click on search icon
    And Verify search results have dress
