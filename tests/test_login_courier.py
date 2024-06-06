import requests
from variables import Urls, MessageText
import allure
from helpers import Helpers


class TestLoginCourier(Helpers):
    @allure.title('Авторизация курьером')
    def test_login_courier(self):
        login, password, _ = self.data_generate()
        self.create_courier(login, password)
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.login_courier, data=payload)
        assert response.status_code == 200
        assert MessageText.id in response.text
        self.delete_courier(login, password)

    @allure.title('Авторизация курьером без логина')
    def test_login_without_login(self):
        login, password, _ = self.data_generate()
        self.create_courier(login, password)
        payload = {
            "login": '',
            "password": password
        }
        response = requests.post(Urls.login_courier, data=payload)
        assert response.status_code == 400
        assert MessageText.login_courier_without_data in response.text
        self.delete_courier(login, password)

    @allure.title('Авторизация курьером без пароля')
    def test_login_without_password(self):
        login, password, _ = self.data_generate()
        self.create_courier(login, password)
        payload = {
            "login": login,
            "password": ''
        }
        response = requests.post(Urls.login_courier, data=payload)
        assert response.status_code == 400
        assert MessageText.login_courier_without_data in response.text
        self.delete_courier(login, password)

    @allure.title('Авторизация курьером без данных')
    def test_login_without_data(self):
        payload = {
            "login": '',
            "password": ''
        }
        response = requests.post(Urls.login_courier, data=payload)
        assert response.status_code == 400
        assert MessageText.login_courier_without_data in response.text

    @allure.title('Авторизация курьером с несуществующими данными')
    def test_login_with_wrong_data(self):
        login, password, _ = self.data_generate()
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.login_courier, data=payload)
        assert response.status_code == 404
        assert MessageText.login_courier_with_wrong_data in response.text
