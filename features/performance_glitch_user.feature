Feature: performance glitch user

Scenario: Perfromance Glitch user login
  Given The Login page is open (performance)
  When the user enters the username"performance_glitch_user"
  Then enter the password "secret_sauce"
  And the user logs in
  And it takes the user to the next page "PRODUCTS"
