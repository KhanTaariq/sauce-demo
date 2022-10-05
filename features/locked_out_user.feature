Feature: locked out user

Scenario: locked out user login
  Given sourcedemo login page is open
  When the user inputs the username "locked_out_user"
  Then for password "secret_sauce" is entered
  And the login button is clicked
  And displays error message for locked out user "Epic sadface: Sorry, this user has been locked out."
