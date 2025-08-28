
import sender_stand_request as api
import request_data as data

def test_create_and_get_order():
   
    create_response = api.post_new_order(data.order_body)
    assert create_response.status_code == 201, (
        f"Ошибка: ожидается статус 201, получено {create_response.status_code}"
    )

    json_data = create_response.json()
    assert "track" in json_data and json_data["track"], "В ответе нет номера трека заказа"
    track_number = json_data["track"]

    get_response = api.get_track_order(track_number)
    assert get_response.status_code == 200, (
        f"Ошибка: ожидается статус 200 при запросе по треку, получено {get_response.status_code}"
    )

    order_data = get_response.json().get("order", {})
    assert order_data.get("firstName") == data.order_body["firstName"], "Имя не совпадает"
    assert order_data.get("lastName") == data.order_body["lastName"], "Фамилия не совпадает"
    assert order_data.get("address") == data.order_body["address"], "Адрес не совпадает"
    assert str(order_data.get("metroStation")) == str(data.order_body["metroStation"]), "Метро не совпадает"
    assert order_data.get("phone") == data.order_body["phone"], "Телефон не совпадает"
    assert order_data.get("rentTime") == data.order_body["rentTime"], "Срок аренды не совпадает"

    if data.order_body.get("color"):
        assert set(data.order_body["color"]).issubset(order_data.get("color", [])), "Цвет(а) не совпадают"

    assert order_data.get("comment") == data.order_body["comment"], "Комментарий не совпадает"