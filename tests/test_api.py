from pytest_bdd import given, then, when, scenario, parsers
from lib.tools.getPath import get_path
from lib.core.core_api import ApiRequest
import allure
import pytest


@scenario(get_path('tests/bdd/api.feature'), 'API test')
def test_dynamic(_base_url): """ Test body """


@given('Initialize request body')
def init_request(_base_url, _method, _name, _json, _URL):
    global test
    test = ApiRequest(_base_url=_base_url,
                      _name=_name,
                      _method=_method,
                      _URL=_URL,
                      _json=_json)



@then(parsers.parse("Response validation"))
def send_and_validate(_status_code, _method, _name, _base_url, _URL, _json):
    with allure.step("Initialize request body     |    NAME : " + _name +
                     "   |   METHOD : " + _method +
                     "   |   LINK : " + _base_url + _URL +
                     "   |   JSON : " + _json):
        with allure.step("Response validation : " + _status_code):
            test.make_request()
            test.validate_status_code(_status_code)
