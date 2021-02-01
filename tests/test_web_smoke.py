from pytest_bdd import given, then, scenario
from lib.tools.getPath import get_path
import requests, allure


@scenario(get_path('tests/bdd/web_smoke.feature'), 'Web smoke test', )
def test_dynamic(_base_url): """ Test body """

@given('Name Method URL')
def init_step(): """init_step"""


@then('Response validation')
def send_and_validate_statuscode(_base_url, _name, _method, _URL, _status_code):
    with allure.step("Response validation     |    NAME : " + _name +
                     "   |   METHOD : " + _method +
                     "   |   LINK : " + _base_url + _URL +
                     "   |   STATUS CODE : " + _status_code):
        r = requests.get(str(_base_url) + _URL, allow_redirects=False)
        assert r.status_code == int(_status_code)
