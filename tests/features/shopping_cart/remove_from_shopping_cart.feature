Feature: Remove from Shopping Cart

  Scenario: I decide not to buy the Product
    Given Im on Product Page
    When I click on add to shopping cart
    Then I verify my product on Basket
    And Decide to remove the Product
    And Verify that my Product is on the Basket
