Feature: problem user

Scenario: problem user login
  Given The Login page is open (problem user)
  When the user enters the username"problem_user"
  Then password "secret_sauce" is used
  And the user clicks the login button that is displayed
  And it takes the user to the products page that displays the cute puppies
