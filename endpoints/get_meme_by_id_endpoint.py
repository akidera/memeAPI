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
        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.data = Meme(**self.response_json)
        return self.data

    @allure.step('Asser meme ids match in request and in response')
    def match_ids(self, requested_id, meme_id):
        assert requested_id == meme_id


