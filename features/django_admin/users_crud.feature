Feature: Managing users

  Scenario: Creating user
     Given I am logged as Super user
      When I create Staff user
      Then Staff user is visible on user list page
       And I should be able to login as Staff user

  Scenario: Updating user
     Given I am logged as Super user
      When I create Staff user
       And I change "Last name" to "Johnson"
       And I click "Save and continue editing" button
      Then I should see "Johnson" in "Last name" field

  Scenario: Deleting user
     Given I am logged as Super user
      When I create Staff user
       And I remove Staff user
      Then Staff user is not visible on user list page

  Scenario Outline: Delete user "<user>"
     Given I am logged as <user> user
      When I create Staff user
       And I remove Staff user
      Then Staff user is not visible on user list page
    Examples:
          | user |
          | foo  |
          | bar  |
