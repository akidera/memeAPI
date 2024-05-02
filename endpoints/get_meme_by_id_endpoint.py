import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint
from json_schemas.json_schema import Meme


class GetMemeById(BaseEdpoint):
    token = None
    id = None
    requestedId = None

    @allure.step('Get meme list')
    def get_meme_by_id(self, token, meme_id):
        self.response = requests.get(f'{BaseEdpoint.BASE_URL}/meme/{meme_id}',
                                     headers={'Authorization': f'{token}'})
        self.response_code = self.response.status_code
        if self.response_code == 200:
            self.response_json = self.response.json()
            self.data = Meme(**self.response_json)
            return self.data

    @allure.step('Asser meme ids match in request and in response')
    def match_ids(self, meme_id):
        assert meme_id == self.data.id


