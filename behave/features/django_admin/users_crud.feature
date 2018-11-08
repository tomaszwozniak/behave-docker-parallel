Feature: Managing users

  Scenario: Creating user
     Given I am logged as Super user
      When I create Stuff user
      Then Stuff user is visible on user list page
       And I should be able to login as stuff user

  Scenario: Updating user
     Given I am logged as Super user
      When I create Stuff user
       And I change "Last name" to "Johnson"
       And I click "Save and continue editing" button
      Then I should see "Johnson" in "Last name" field

  Scenario: Deleting user
     Given I am logged as Super user
      When I create Stuff user
       And I remove Stuff user
      Then Stuff user is not visible on user list page

  Scenario Outline: Deleting user outline
     Given I am logged as <user> user
      When I create Stuff user
       And I remove Stuff user
      Then Stuff user is not visible on user list page
    Examples:
          | user |
          | foo  |
          | bar  |
