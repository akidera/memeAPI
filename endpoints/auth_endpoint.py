import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint


class GetAuthToken(BaseEdpoint):
    auth_body = {
        "name": "Volha"
    }

    @allure.step('Get token')
    def get_token(self, auth_body=None):
        auth_body = auth_body if auth_body else self.auth_body
        self.response = requests.post(f"{BaseEdpoint.BASE_URL}/authorize", json=auth_body)
        self.response_json = self.response.json()
        token = self.response.json()['token']

        if self.response:
            assert self.response.status_code == 200

        return token


