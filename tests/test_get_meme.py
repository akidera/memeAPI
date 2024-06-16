import allure
import pytest
from tests.base_test import BaseTest


class TestGetMemeAll(BaseTest):
    @pytest.mark.smoke
    @allure.feature('Get all memes')
    def test_get_all_memes_list(self, get_meme_list, auth_token):
        get_meme_list.get_meme_list(token=auth_token)
        get_meme_list.check_resp_code_is_200()

    @pytest.mark.test
    @allure.feature('Get all memes with invalid token')
    def test_get_all_memes_list_invalid_token(self, get_meme_list):
        get_meme_list.get_meme_list(token='123')
        get_meme_list.check_resp_code_is_401()


class TestGetMeme(BaseTest):
    @pytest.mark.smoke
    @allure.feature('Get meme by id')
    def test_get_meme(self, auth_token, get_meme_by_id, create_del_meme):
        meme1 = create_del_meme

        get_meme_by_id.get_meme_by_id(token=auth_token, meme_id=meme1.id)
        get_meme_by_id.match_ids(meme1.id)

    @pytest.mark.test
    @allure.feature('Get meme by invalid id')
    def test_get_meme_invalid_id(self, auth_token, get_meme_by_id, create_del_meme):

        get_meme_by_id.get_meme_by_id(token=auth_token, meme_id='asd')
        get_meme_by_id.check_resp_code_is_404()

    @pytest.mark.test
    @allure.feature('Send unauthorized request')
    def test_get_meme_invalid_id(self, auth_token, get_meme_by_id):

        get_meme_by_id.get_meme_by_id(token='1', meme_id=1)
        get_meme_by_id.check_resp_code_is_401()

