import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint
from json_schemas.json_schema import Meme


class UpdateMeme(BaseEdpoint):
    id = None
    body = {
        "id": id,
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
        "updated_by": "Volha",
        "url": "https://media.istockphoto.com/"
    }

    @allure.step('Update meme')
    def update_meme(self, token=None, meme_id=None, body=None):
        body = body if body else UpdateMeme.body
        self.response = requests.put(f'{BaseEdpoint.BASE_URL}/meme/{meme_id}',
                                     headers={'Authorization': f'{token}',
                                              'Content-Type': 'application/json'},
                                     json=body)
        self.response_json = self.response.json() if self.response.ok else {}
        self.response_code = self.response.status_code
        self.data = Meme(**self.response_json) if self.response.ok else {}
