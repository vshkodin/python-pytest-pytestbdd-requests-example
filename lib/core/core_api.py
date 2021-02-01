import json
import random
import requests
import string


class ApiRequest:

    # Initializer / Instance Attributes
    def __init__(self, **kwargs):
        self._base_url = kwargs["_base_url"]
        self._name = kwargs["_name"]
        self._method = kwargs["_method"]
        self._URL = kwargs["_URL"]
        self._json = kwargs["_json"]
        self.r = None
        self._json_for_auth = None
        self._headers = None
        self._params = {}
        self._headers = {}
        self._json = json.loads(self._json)


    def make_request(self):

        if self._method == "GET":
            self.r = requests.get(str(self._base_url) + self._URL,
                                  params=self._params, allow_redirects=False)
        elif self._method == "POST":
            self.r = requests.post(str(self._base_url) + self._URL,
                                   params=self._params, json=self._json, allow_redirects=False)
        elif self._method == "PUT":
            self.r = requests.put(str(self._base_url) + self._URL,
                                  params=self._params, json=self._json, allow_redirects=False)
        elif self._method == "DELETE":
            self.r = requests.delete(str(self._base_url) + self._URL,
                                     params=self._params, json=self._json, allow_redirects=False)
        elif self._method == "PATCH":
            self.r = requests.patch(str(self._base_url) + self._URL, params=self._params,
                                    json=self._json, allow_redirects=False)
    def validate_status_code(self, _status_code):
        assert self.r.status_code == int(_status_code)
