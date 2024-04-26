import allure


class BaseEdpoint:

    BASE_URL = 'http://167.172.172.115:52355'

    response = None
    response_code = None
    response_json = None
    data = None
    token = None

    @allure.step('Asserting response is 200')
    def check_resp_code_is_200(self):
        assert self.response_code == 200, 'Status code is not 200'

    @allure.step('Asserting response is 201')
    def check_resp_code_is_201(self):
        assert self.response_code == 201, 'Status code is not 201'

    @allure.step('Asserting response is 201')
    def check_resp_code_is_401(self):
        assert self.response_code == 401, 'Status code is not 401'

    @allure.step('Asserting response is 400')
    def check_resp_is_400(self):
        assert self.response_code == 400, "Status code is not 400"

    @allure.step('Asserting response is 403')
    def check_resp_code_is_403(self):
        assert self.response_code == 403, 'Status code is not 403'

    @allure.step('Asserting response is 404')
    def check_resp_code_is_404(self):
        assert self.response_code == 404, 'Status code is not 404'

    @allure.step("asserting response is 500")
    def check_resp_is_500(self):
        assert self.response_code == 500, 'Status code is not 500'
