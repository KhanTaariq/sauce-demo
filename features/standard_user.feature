Feature: standard user

  Scenario: standard user login
    Given The Login page is open
    When the user enters the username "standard_user"
    Then password "secret_sauce"
    And the user clicks the login button
    And it takes the user to the products page

    Scenario: standard user incorrect password
      Given The Login page is open a second time
      When the user enters the username "standard_user" a second time
      Then password "incorrect"
      And the user clicks the login button a second time
      And the user get the error message "Epic sadface: Username and password do not match any user in this service"
