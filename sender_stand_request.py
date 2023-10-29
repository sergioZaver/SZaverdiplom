import configuration
import requests
import data

# Создание заказа
def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.orders_body)
#print(post_new_orders().json())

# Сохранение номера заказа
def get_track(new_order_track):
    track_number = configuration.RECEIVING_ORDERS + "?t=" + str(new_order_track)
    return requests.get(configuration.URL_SERVICE + track_number)
#print(get_track(new_order_track=672834))