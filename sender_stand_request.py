import requests
import configuration
import request_data as data 

def post_new_order(body):
    """Отправить POST-запрос на создание нового заказа."""
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=body, timeout=10)

def get_track_order(track):
    """Отправить GET-запрос на получение заказа по треку."""
    url = configuration.URL_SERVICE + configuration.GET_TRACK
    return requests.get(url, params={"t": str(track)}, timeout=10)