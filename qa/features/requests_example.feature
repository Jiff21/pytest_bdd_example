@medium @cms #priority #feature-name
Feature: Requests can get page

    Scenario: Requests goes to expected page
        Given I get / using requests
        Then the response should be successful
