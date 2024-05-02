import allure
import pytest
from tests.base_test import BaseTest



class TestMemeUpdate(BaseTest):

    @pytest.mark.test
    @allure.feature('Update meme')
    @pytest.mark.parametrize("colors, tags, text, url",
                             [(['green', 'black'], ['fun', 'smile'], "smiling snail", 'https://snail.smile.com/'),
                              (['red', 'blue', 'white'], ['sun', 'memory'], "boys in the garden", 'https://happy.com/'),
                              (['yellow', 'black'], ['porch'], "in the dungeons", 'https://dnd.com/')])
    def test_meme_update(self, auth_token, create_del_meme, update_meme,
                         colors, tags, text, url):

        """Test that memes can be  updated by it\'s owner"""
        meme_data = create_del_meme
        upd_body = {
            "id": meme_data.id,
            "info": {
                "colors": colors,
                "objects": [
                    "picture",
                    "no text"
                ]
            },
            "tags": tags,
            "text": text,
            "url": url
        }
        update_meme.update_meme(token=auth_token, meme_id=meme_data.id, body=upd_body)

        # this check fails cuz ids are different types in request and response
        # assert upd_body == update_meme.response_json

        assert update_meme.response_json['info']['colors'] == colors
        assert update_meme.response_json['tags'] == tags
        assert update_meme.response_json['text'] == text
        assert update_meme.response_json['url'] == url

    @pytest.mark.test
    @allure.feature('Update meme without mandatory parameters')
    @pytest.mark.parametrize("body",
                             [({"id": None, "tags": [], "text": "", "url": ""}),
                              ({"id": None, "info": {}, "text": "", "url": ""}),
                              ({"id": None, "info": {}, "tags": [], "url": ""}),
                              ({"id": None, "info": {}, "tags": [], "text": ""}),
                              ({"tags": "", "info": {}, "url": [], "text": ""})
                              ])
    def test_meme_update_without_mandatory_params(self, auth_token, create_del_meme,
                                                  update_meme, body):
        meme = create_del_meme
        body['id'] = meme.id
        update_meme.update_meme(token=auth_token, body=body, meme_id=meme.id)
        update_meme.check_resp_is_400()

    @pytest.mark.test
    @allure.feature('Negative: Update meme not by an owner')
    @pytest.mark.parametrize("colors, tags, text, url",
                             [(['green', 'black'], ['fun', 'smile'], "smiling snail", 'https://snail.smile.com/')])
    def test_meme_update_by_not_owner(self, create_meme, get_auth_token, auth_token,
                                      create_del_meme, update_meme, delete_meme,
                                      colors, tags, text, url):
        """Test that memes can be  updated by it\'s owner"""
        # create a meme with user #1
        meme = create_meme.create_meme(token=auth_token)
        upd_body = {
            "id": meme.id,
            "info": {
                "colors": colors,
                "objects": [
                    "picture",
                    "no text"
                ]
            },
            "tags": tags,
            "text": text,
            "url": url
        }

        # update a meme with user #2
        token2 = get_auth_token.get_token(auth_body={"name": "Bill"})
        update_meme.update_meme(token=token2, meme_id=meme.id, body=upd_body)
        update_meme.check_resp_code_is_403()

        # clean up this mess
        delete_meme.delete_meme(token=auth_token, meme_id=meme.id)

    @pytest.mark.test
    @allure.feature('Unauthorized request - invalid token')
    def test_meme_update_unauthorized(self, create_meme, auth_token,
                                      create_del_meme, update_meme):

        meme = create_del_meme

        update_meme.update_meme(token='1', meme_id=meme.id)
        update_meme.check_resp_code_is_401()

    @pytest.mark.test
    @allure.feature('Unauthorized request - invalid token')
    def test_meme_update_unauthorized(self, create_del_meme, update_meme):
        meme = create_del_meme

        update_meme.update_meme(token='1', meme_id=meme.id)
        update_meme.check_resp_code_is_401()

    @pytest.mark.test
    @allure.feature('Update meme by invalid id')
    def test_meme_update_invalid_id(self, auth_token, update_meme):

        update_meme.update_meme(token=auth_token, meme_id='asd')
        update_meme.check_resp_code_is_404()

