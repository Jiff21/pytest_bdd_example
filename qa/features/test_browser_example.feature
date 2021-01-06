@medium @cms #priority #feature-name
Feature: Requests can get page

    Scenario: Browser can get correct page
        Given I get the index page
        Then I should be on home
