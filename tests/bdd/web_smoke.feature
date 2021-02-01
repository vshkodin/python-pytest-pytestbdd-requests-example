Feature: Smoke tests
    Content description...

    Scenario Outline: Web smoke test

        Given Name Method URL
        Then Response validation

        Examples:
        |  _name                            |  _method  |  _status_code |  _URL  |
        |    home page                      |    GET    |      200      |   /    |
