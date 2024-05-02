import allure
import pytest
from tests.base_test import BaseTest


class TestDeleteMeme(BaseTest):
    @pytest.mark.test
    @allure.feature('Delete meme')
    def test_meme_delete(self, auth_token, create_meme, delete_meme):
        """Test that memes can be deleted by it\'s owner"""
        meme1 = create_meme.create_meme(token=auth_token)

        delete_meme.delete_meme(token=auth_token, meme_id=meme1.id)
        delete_meme.check_del_resp_text(meme1.id)

    @pytest.mark.test
    @allure.feature('Negative: Delete meme not by an owner')
    def test_meme_is_not_deleted_by_not_owner(self, create_meme, delete_meme,
                                              get_auth_token, auth_token):
        """Test that memes cannot be deleted by not an owner"""
        meme = create_meme.create_meme(token=auth_token)

        # Delete meme by not an owner
        token2 = get_auth_token.get_token(auth_body={"name": "Lola"})
        delete_meme.delete_meme(token=token2, meme_id=meme.id)
        delete_meme.check_resp_code_is_403()

        # Clean up this mess
        delete_meme.delete_meme(token=auth_token, meme_id=meme.id)
        delete_meme.check_resp_code_is_200()
        delete_meme.check_del_resp_text(meme.id)

    @pytest.mark.test
    @allure.feature('Send unauthorized request')
    def test_meme_delete_unauthorized(self,  delete_meme):

        delete_meme.delete_meme(token='1', meme_id='asd')
        delete_meme.check_resp_code_is_401()

    @pytest.mark.test
    @allure.feature('Negative: Delete meme by invalid id')
    def test_meme_delete_invalid_id(self, delete_meme, auth_token):
        delete_meme.delete_meme(token=auth_token, meme_id='asd')
        delete_meme.check_resp_code_is_404()
