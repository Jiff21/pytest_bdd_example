@smoke @normal @home
Feature: Example Requests test

    Scenario: Requests receives a success message
        When I get the index using requests
        Then the response should be successful
