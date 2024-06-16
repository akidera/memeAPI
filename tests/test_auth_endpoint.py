import allure
import pytest
import requests
from tests.base_test import BaseTest
from endpoints.BaseEndpoint import BaseEdpoint


class TestAuth(BaseTest):

    @pytest.mark.regression
    @allure.feature('Positive test - req body not provided')
    def test_auth_is_success(self,get_auth_token):
        get_auth_token.get_token()

    @pytest.mark.regression
    @allure.feature('Positive test - req body not provided')
    def test_token_verification_success(self, get_auth_token, check_auth_token):
        token = get_auth_token.get_token()
        check_auth_token.check_token(token=token)
        check_auth_token.check_resp_code_is_200()

    @pytest.mark.regression
    @allure.feature('Negative auth test - req body not provided')
    def test_auth_body_not_given(self,get_auth_token):
        response = requests.post(f"{BaseEdpoint.BASE_URL}/authorize")
        assert response.status_code == 500

    @pytest.mark.regression
    @allure.feature('Negative auth test - invalid auth body')
    @pytest.mark.parametrize("auth_body",
                             [({"name": 123}),
                              ({"vname": "FFFF"})])
    def test_auth_body_invalid(self, get_auth_token, auth_body):

        get_auth_token.get_token(auth_body=auth_body)
        get_auth_token.check_resp_is_400()

    @pytest.mark.regression
    @allure.feature('Negative auth test - check invalid token')
    def test_check_invalid_token_error(self, check_auth_token):
        check_auth_token.check_token(token='123')
        check_auth_token.check_resp_code_is_404()

