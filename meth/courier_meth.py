import requests
import json
from tests.data import BASE_URL


class CourierMeth:
    def login_courier(self, login, password):
        payload = json.dumps({"login": login, "password": password})
        respons = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        return respons.status_code, respons.text

    def create_courier(self, login, password, first_name):
        payload = json.dumps(
            {"login": login, "password": password, "firstName": first_name}
        )
        respons = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
        return respons.status_code, respons.text

    def delete_courier(self, courier_id):
        payload = json.dumps({"id": courier_id})
        respons = requests.delete(f"{BASE_URL}/api/v1/courier/", data=payload)
        return respons.status_code, respons.text