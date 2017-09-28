Feature: Search recommendations

Scenario: Fruit and veg cart page
    Given a user is on the "/cn/fruits-vegetables/cid/9" URL
    And the user chooses New Delhi as their location
    Then the title will be Fruits & Vegetables

@manual
Scenario: Searching for L1 suggests sub-types (L2)
    Given a user is on the "/" URL
    When the user searches for Atta
    And they scroll down past the 3rd row
    Then they will see the Whole Wheat Atta product (ID:123456)

 # Make some scenarios manual, track manual effort over time, set team limits for manual testing effort.