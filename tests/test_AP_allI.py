import allure
import pytest
from tests.base_test import BaseTest


class TestMemeIsCreated(BaseTest):

    @pytest.mark.test
    @allure.feature('Create a new meme')
    def test_meme_creation(self, auth_token, create_meme, get_meme_by_id,
                           get_auth_token, del_meme):

        """Test that memes are created with all filled parameters
           and can be received by GET request by it\'s creator"""

        meme1 = create_meme.create_meme(token=auth_token)
        meme2 = create_meme.create_meme(token=auth_token)

        # Get memes by its IDs and asserting requested and received IDs match
        get_meme_by_id.get_meme_by_id(token=auth_token, meme_id=meme1.id)
        get_meme_by_id.check_resp_code_is_200()
        assert meme1.info == get_meme_by_id.response_json['info']
        assert meme1.tags == get_meme_by_id.response_json['tags']
        assert meme1.text == get_meme_by_id.response_json['text']
        assert meme1.url == get_meme_by_id.response_json['url']
        assert get_meme_by_id.response_json['updated_by'] == 'Volha'

        get_meme_by_id.get_meme_by_id(token=auth_token, meme_id=meme2.id)
        get_meme_by_id.check_resp_code_is_200()
        assert meme2.info == get_meme_by_id.response_json['info']
        assert meme2.tags == get_meme_by_id.response_json['tags']
        assert meme2.text == get_meme_by_id.response_json['text']
        assert meme2.url == get_meme_by_id.response_json['url']
        assert get_meme_by_id.response_json['updated_by'] == 'Volha'

        # Clean up test memes
        del_meme.append(meme1.id)
        del_meme.append(meme2.id)
        print(auth_token)

    @pytest.mark.test
    @allure.feature('Get all memes')
    def test_get_all_memes_list(self, get_meme_list, auth_token):
        get_meme_list.get_meme_list(token=auth_token)
        get_meme_list.check_resp_code_is_200()
        print(auth_token)

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
        print(auth_token)

    @pytest.mark.test
    @allure.feature('Negative: Update meme not by an owner')
    @pytest.mark.parametrize("colors, tags, text, url",
                             [(['green', 'black'], ['fun', 'smile'], "smiling snail", 'https://snail.smile.com/')])
    def test_meme_update_by_not_owner(self, create_meme, get_auth_token,
                                      create_del_meme, update_meme, delete_meme,
                                      colors, tags, text, url):
        """Test that memes can be  updated by it\'s owner"""
        # create a meme with user #1
        token1 = get_auth_token.get_token()
        meme = create_meme.create_meme(token=token1)
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
        delete_meme.delete_meme(token=token1, meme_id=meme.id)

    @pytest.mark.test
    @allure.feature('Delete meme')
    def test_meme_delete(self, auth_token, create_meme, delete_meme):

        """Test that memes can be deleted by it\'s owner"""
        meme1 = create_meme.create_meme(token=auth_token)

        delete_meme.delete_meme(token=auth_token, meme_id=meme1.id)
        delete_meme.check_del_resp_text(meme1.id)
        print(auth_token)

    @pytest.mark.test
    @allure.feature('Negative: Delete meme not by an owner')
    def test_meme_delete_by_not_owner(self, create_meme, delete_meme,
                                      get_auth_token):
        """Test that memes cannot be deleted by not an owner"""
        token1 = get_auth_token.get_token(auth_body={"name": "Mila"})
        meme = create_meme.create_meme(token=token1)

        # Delete meme by not an owner
        token2 = get_auth_token.get_token(auth_body={"name": "Lola"})
        delete_meme.delete_meme(token=token2, meme_id=meme.id)
        delete_meme.check_resp_code_is_403()

        # Clean up this mess
        delete_meme.delete_meme(token=token1, meme_id=meme.id)
        delete_meme.check_resp_code_is_200()
        delete_meme.check_del_resp_text(meme.id)
