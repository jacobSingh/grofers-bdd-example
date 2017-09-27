Feature: Cart amount total is automatically updated. (cart_amount)

Scenario: Adding products increments the total
    Given a user is on the "/" URL
    And the user chooses New Delhi as their location
    And there is at least one product to choose
    When 1 quantity of the first product is added to cart
    Then the cart total will be equal to the price of the product

# Scenario: Adding multiple products increments the total
#    Given a user is on the "/" URL
#    And there is at least one product to choose
#    When 3 quantity of the first product is added to cart
#    Then the cart total will be equal to three times the price of the product
