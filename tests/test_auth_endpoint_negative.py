import allure
import pytest
import requests
from tests.base_test import BaseTest
from endpoints.BaseEndpoint import BaseEdpoint


class TestAuth(BaseTest):

    @pytest.mark.test
    @allure.feature('Negative auth test - req body not provided')
    def test_auth_body_not_given(self):
        response = requests.post(f"{BaseEdpoint.BASE_URL}/authorize")
        assert response.status_code == 500

    @pytest.mark.test
    @allure.feature('Negative auth test - invalid')
    @pytest.mark.parametrize("auth_body",
                             [({"name": 123}),
                              ({"vname": "Heken"}),
                              {}])
    def test_auth_body_not_given(self, auth_body):
        response = requests.post(f"{BaseEdpoint.BASE_URL}/authorize", json=auth_body)
        assert response.status_code == 400

    def test_check_invalid_token_error(self, check_auth_token):
        check_auth_token.check_token(token='123')
        check_auth_token.check_resp_code_is_404()

