import allure
import pytest
from tests.base_test import BaseTest
from endpoints.BaseEndpoint import BaseEdpoint


class TestMemeIsCreated(BaseTest, BaseEdpoint):

    @pytest.mark.smoke
    @allure.feature('Create a new meme')
    def test_meme_creation(self, auth_token, create_meme, del_meme):

        """Test that memes are created with all filled parameters"""

        body = {
            "info": {
                "colors": [
                    "green"
                ],
                "objects": [
                    "clouds"
                ]
            },
            "tags": [
                "sky"
            ],
            "text": "nature",
            "url": "https://lalala.test.me/"
        }

        meme1 = create_meme.create_meme(token=auth_token, body=body)
        assert meme1.info == body['info']
        assert meme1.tags == body['tags']
        assert meme1.text == body['text']
        assert meme1.url == body['url']

        # Clean up test memes
        del_meme.append(meme1.id)

    @pytest.mark.test
    @allure.feature('Check creating with incorrect params types')
    @pytest.mark.parametrize("body",
                             [({"text": 123, "url": "", "tags": [], "info": {}}),
                              ({"text": "", "url": 456, "tags": [], "info": {}}),
                              ({"text": "", "url": "", "tags": "invalid", "info": {}}),
                              ({"text": "", "url": "", "tags": [], "info": "invalid"})])
    def test_check_creation_with_incorrect_data_types(self, auth_token, create_meme, body):

        create_meme.create_meme(token=auth_token, body=body)
        create_meme.check_resp_is_400()

    @pytest.mark.test
    @allure.feature('Check creating without mandatory fields')
    @pytest.mark.parametrize("body",
                             [({"tags": [], "text": "", "url": ""}),
                              ({"info": {}, "text": "", "url": ""}),
                              ({"info": {}, "tags": [], "url": ""}),
                              ({"info": {}, "tags": [], "text": ""})])
    def test_check_mandatory_params(self, auth_token, create_meme,
                                    body):

        """Test that all parameters are mandatory"""

        create_meme.create_meme(token=auth_token, body=body)
        create_meme.check_resp_is_400()

    @pytest.mark.test
    @allure.feature('Check invalid authorization request')
    def test_check_invalid_auth_request(self, create_meme):

        create_meme.create_meme(token="1")
        create_meme.check_resp_code_is_401()

    @pytest.mark.test
    @allure.feature('Check empty token request')
    def test_check_unauthorized_request(self, create_meme):

        create_meme.create_meme(token="")
        create_meme.check_resp_is_500()
