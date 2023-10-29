import sender_stand_request

# Выполнить запрос на получения заказа по треку заказа
def post_new_order_track():
    new_order_track = sender_stand_request.post_new_orders()
    return new_order_track.json()['track']

# Автотест по треку заказа можно получить данные о заказе
def test_give_order_by_track_success_response():
    order_id = post_new_order_track()
    track_id = sender_stand_request.get_track(order_id).status_code
    assert track_id == 200
