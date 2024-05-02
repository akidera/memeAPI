import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint
from json_schemas.json_schema import Meme


class CreateMeme(BaseEdpoint):

    body = {
        "info": {
            "colors": [
                "red",
                "yellow",
                "blue"
            ],
            "objects": [
                "picture",
                "no text"
            ]
        },
        "tags": [
            "pain",
            "people"
        ],
        "text": "suffering man",
        "url": "https://media.istockphoto.com/"
    }

    @allure.step('Create new meme')
    def create_meme(self, token=None, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{BaseEdpoint.BASE_URL}/meme',
                                      headers={'Authorization': f'{token}',
                                               'Content-Type': 'application/json'},
                                      json=body)
        self.response_code = self.response.status_code
        if self.response_code == 200:
            self.response_json = self.response.json()
            self.data = Meme(**self.response_json)
            assert self.response.status_code == 200
            return self.data
