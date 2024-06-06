import requests
from variables import Urls, MessageText
import allure

class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_order_list(self):
        response = requests.get(Urls.order_list)
        assert response.status_code == 200
        assert MessageText.order_list in response.text