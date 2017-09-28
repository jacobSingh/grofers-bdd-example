Feature: Adding and removing from the cart

Scenario: User adding a product to the cart
    Given a user is on a L1 category page
#   And there is at least 1 product on the page
    When the user adds 2 quantity of the first product
    And the user goes to the shopping cart
    Then the shopping cart will have 2 products in it
    When the user removes 2 quantity of the first product from the cart
    Then the shopping cart will have 0 products in it

