from faker import Faker
import requests
import variables
import allure


class Helpers:
    @allure.step('Удаление курьера')
    def delete_courier(self, login, password):
        r = requests.post(f'{variables.url}/api/v1/courier/login', data={
            "login": login,
            "password": password
        })
        id = r.json()['id']
        requests.delete(f'{variables.url}/api/v1/courier/{id}')

    @allure.step('Генератор данных для регистрации курьера')
    def data_generate(self):
        fake = Faker()
        login = fake.user_name()
        password = fake.password(length=4, special_chars=False)
        name = fake.first_name()
        return login, password, name

    @allure.step('Создание курьера')
    def create_courier(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        return requests.post(f'{variables.url}/api/v1/courier', data=payload)