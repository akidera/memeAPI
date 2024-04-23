import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint


class GetMemeList(BaseEdpoint):
    token = None

    @allure.step('Get meme list')
    def get_meme_list(self, token):

        self.response = requests.get(f'{BaseEdpoint.BASE_URL}/meme', headers={'Authorization': f'{token}'})
        self.response_json = self.response.json()
        self.response_code = self.response.status_code
