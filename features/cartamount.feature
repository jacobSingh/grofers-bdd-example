Feature: Cart amount total is automatically updated. (cart_amount)

Scenario: Adding products increments the total
    Given a user is on the "/" URL
    And the user chooses New Delhi as their location
    And there is at least one product to choose
    When 1 quantity of the first product is added to cart
    Then the cart total will be equal to 1 times the price of the product

Scenario: Adding muliple products increments the total
    Given a user is on the "/" URL
    And the user chooses New Delhi as their location
    And there is at least one product to choose
    When 3 quantity of the first product is added to cart
    Then the cart total will be equal to 3 times the price of the product

@quicktest
Scenario: Fruit and veg cart page
    Given a user is on the "/cn/fruits-vegetables/cid/9" URL
    And the user chooses New Delhi as their location
    Then the title will be Fruits & Vegetables

@wip
Scenario: Fruit and veg cart page
    Given a user is on the "/cln/most-popular/clid/59ba31fbf7c3490f93054c81" URL
    And the user chooses New Delhi as their location
    Then the title will be Every Day Low Prices


Scenario: Moving App to background during transition doesn't crash it
    Given a User is opening a window
    When I...


#@manual
#Scenario: ...