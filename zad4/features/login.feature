Feature: Login Test

  Scenario: success
    Given Chrome browser
    And Gmail login page
    When we write login wolnikowa@example.com and click login button
    And we write password haslo321 and click login button
    Then we will login

  Scenario: wrong login
    Given Chrome browser
    And Gmail login page
    When we write login wolnikowa@exam and click login button
    Then we will not login

  Scenario: wrong password
    Given Chrome browser
    And Gmail login page
    When we write login wolnikowa@example.com and click login button
    And we write password pawel123 and click login button
    Then we will not login

  Scenario: empty password
    Given Chrome browser
    And Gmail login page
    When we write login wolnikowa@example.com and click login button
    And click login button on password page
    Then we will not login

  Scenario: empty login
    Given Chrome browser
    And Gmail login page
    When click login button on login page
    Then we will not login