import requests
import allure
from endpoints.BaseEndpoint import BaseEdpoint


class DeleteMeme(BaseEdpoint):
    token = None
    meme_id = None

    @allure.step('Delete meme')
    def delete_meme(self, token, meme_id):
        self.response = requests.delete(f'{BaseEdpoint.BASE_URL}/meme/{meme_id}',
                                        headers={'Authorization': f'{token}'})
        self.response_code = self.response.status_code

    @allure.step('Asserting delete reponse text is correct')
    def check_del_resp_text(self, meme_id):
        assert self.response.text == f'Meme with id {meme_id} successfully deleted'
