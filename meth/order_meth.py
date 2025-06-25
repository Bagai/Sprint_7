import requests
from data import BASE_URL


class OrderMeth:
    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        print(payload)
        respons = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        print(respons)
        return respons.status_code, respons.json()
