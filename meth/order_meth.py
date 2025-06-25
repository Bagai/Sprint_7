import requests
from data import BASE_URL


class OrderMeth:

    def create_order(self, order_data, color):
        payload = {
            "firstName": order_data[0],
            "lastName": order_data[1],
            "address": order_data[2],
            "metroStation": order_data[3],
            "phone": order_data[4],
            "rentTime": order_data[5],
            "deliveryDate": order_data[6],
            "comment": order_data[7],
            "color": color,
        }
        respons = requests.post(f"{BASE_URL}/api/v1/orders", data=payload)
        return respons.status_code, respons.json()

    def get_order(self, curied_id=None, nearestStation=None, limit=None, page=None):
        payload = {
            "courierId": curied_id,
            "nearestStation": nearestStation,
            "limit": limit,
            "page": page,
        }
        respons = requests.get(f"{BASE_URL}/api/v1/orders/", data=payload)
        return respons.status_code, respons.json()
