import requests
from data import BASE_URL


class CourierMeth:
    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        print(payload)
        respons = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        print(respons)
        return respons.status_code, respons.json()

    def create_courier(self, login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
        respons = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
        return respons.status_code, respons.text
