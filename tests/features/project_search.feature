Feature: Project Search and Access
  As a user of Globant POC application
  I want to search for specific projects
  So that I can access project information easily

  Scenario: User searches and accesses the project 'Acme Corp'
    Given the user enters to Globant POC application
    When the user searches for 'Acme Corp'
    Then the project information should be displayed
    And the project details should be accessible

  Scenario: User attempts to search with invalid project name
    Given the user enters to Globant POC application
    When the user searches for 'NonExistent Project'
    Then an appropriate "No results found" message should be displayed

  Scenario: User can access project after search
    Given the user enters to Globant POC application
    And the user searches for 'Acme Corp'
    When the user clicks on the project result
    Then the complete project details page should load
    And all project information should be visible