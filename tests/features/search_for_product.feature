Feature: Search for Product

  Scenario: Search for a Product
    Given Im on Home Page
    When I search for Galaxy s20
    Then I should see my product on the list
    And I should open the Product Page

  Scenario: Search for a Product using the Filter
    Given Im on Home Page
    When I search for Galaxy s20
    And I filter by Smartphone
    Then I should see my product on the list
    And I should open the Product Page
