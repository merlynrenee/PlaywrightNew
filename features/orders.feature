Feature: Order Management
  Tests related to placing and viewing orders

  Scenario: Verify order is visible in orders page after placing it
    Given a new order is created via API
    And user is on the login page
    When the user logins in with valid credentials
    And the user navigates to the orders page
    Then the order should be visible in the list

    Scenario Outline: Verify orders is visibe in orders page after placing it
      Given a new order is created via API
      And user is on the login page
      When the user logins in with valid credentials
      And the user navigates to the orders page
      Then the order should be visible in the list
      Examples:
          |email                    |password  |
          |merlyn.renee22@gmail.com |Merren@22 |