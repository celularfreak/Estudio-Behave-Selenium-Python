Feature: Logo chrome
  Scenario: Logo presence on Google Page
    Given launch chrome browser
    When  open google page
      Then verify that the logo present on page
      And close browser