# Понкратова Алина, Qa_pl-08-а — Дипломный проект


import requests

from config import ORDER_CREATE_URL, ORDER_GET_BY_TRACK_URL

def test_order_creation_and_retrieval():
   # Шаг 1: Выполнить запрос на создание заказа
   order_data = {
       "firstName": "Ivan",
       "lastName": "Ivanov",
       "address": "Lenina 16",
       "metroStation": 12,
       "phone": "+7 911 111 11 11",
       "rentTime": 5,
       "deliveryDate": "2024-06-06"
   }
   response_create = requests.post(ORDER_CREATE_URL, json=order_data)


   # Шаг 2: Сохранить номер трека заказа
   order_track = response_create.json()["track"]


   # Шаг 3: Выполнить запрос на получение заказа по треку заказа
   get_params = {"t": order_track}
   response_get = requests.get(ORDER_GET_BY_TRACK_URL, params=get_params)


   # Шаг 4: Проверить, что код ответа равен 200
   assert response_get.status_code == 200