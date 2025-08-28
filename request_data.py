from datetime import datetime

order_body = {
    "firstName": "Stacey",
    "lastName": "Testova",
    "address": "Москва, ул. Примерная, д. 1",
    "metroStation": 4,
    "phone": "+7 999 111-22-33",
    "rentTime": 3,
    "deliveryDate": datetime.now().strftime("%Y-%m-%d"),
    "comment": "Тестовый заказ. Автотест Стэйси",
    "color": ["BLACK"]
}