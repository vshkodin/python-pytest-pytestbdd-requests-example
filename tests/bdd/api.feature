Feature: API tests
    Top 4 mobile journeys...


    Scenario Outline: API test

        Given Initialize request body
        Then Response validation

        Examples:
        |  _name                    |  _method |  _status_code | _user_logged_in |  _URL                   | _json |
        |  search                   |    GET   |      200      |   False         |   /api/planets/1/       |  ""   |
