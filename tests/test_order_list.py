import requests
import variables
import allure

class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_order_list(self):
        response = requests.get(f'{variables.url}/api/v1/orders')
        assert response.status_code == 200
        assert variables.order_list in response.text