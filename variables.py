from faker import Faker
class Urls:
    url = 'https://qa-scooter.praktikum-services.ru'
    create_courier = f'{url}/api/v1/courier'
    create_order = f'{url}/api/v1/orders'
    login_courier = f'{url}/api/v1/courier/login'
    order_list = f'{url}/api/v1/orders'
    delete_courier = f'{url}/api/v1/courier'

class MessageText:
    create_courier = '{"ok":true}'
    create_courier_duplicate = "Этот логин уже используется"
    create_courier_without_data = "Недостаточно данных для создания учетной записи"
    id = 'id'
    login_courier_without_data = "Недостаточно данных для входа"
    login_courier_with_wrong_data = "Учетная запись не найдена"
    create_order = 'track'
    order_list = 'orders'

class Data:
    order_data = [
        [Faker('ru_RU').first_name(), Faker('ru_RU').last_name(), Faker('ru_RU').address(), '4', Faker('ru_RU').phone_number(), '5', '2020-06-06',
         'Only black scooter', "BLACK"],
        [Faker('ru_RU').first_name(), Faker('ru_RU').last_name(), Faker('ru_RU').address(), '6', Faker('ru_RU').phone_number(), '6', '2020-06-06',
         'Only grey scooter', "GREY"],
        [Faker('ru_RU').first_name(), Faker('ru_RU').last_name(), Faker('ru_RU').address(), '7', Faker('ru_RU').phone_number(), '7', '2020-06-06',
         'Black and grey scooters', "BLACK, GREY"],
        [Faker('ru_RU').first_name(), Faker('ru_RU').last_name(), Faker('ru_RU').address(), '4', Faker('ru_RU').phone_number(), '8', '2020-06-06',
         'No color scooter', ""]
    ]