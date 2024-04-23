import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint


class CheckAuthToken(BaseEdpoint):
    token = None

    @allure.step('Get token')
    def check_token(self, token):
        self.response = requests.get(f"{BaseEdpoint.BASE_URL}/authorize/{token}")
        self.response_code = self.response.status_code

        return True if self.response_code == 200 else False
