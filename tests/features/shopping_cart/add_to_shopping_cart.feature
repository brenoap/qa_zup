Feature: Buy Product

  Scenario: I buy a Product
    Given Im at Product Page
    When I click on add to shopping cart
    And I go to Shopping Cart Page
    Then Verify that my Product is on the Basket