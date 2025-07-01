from meth.courier_meth import CourierMeth
from data import courier_credentials
import allure


class TestCourierLogin:

    @allure.title("Логин курьера с валидными данными")
    def test_login_courier_is_successful(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"], courier_credentials["password"]
        )
        assert login_courier[0] == 200 and login_courier[1]["id"] is not None

    @allure.title("Логин курьера с отсутствующим логином")
    def test_login_courier_withot_login_is_denied(self):
        login_courier = CourierMeth().login_courier("", courier_credentials["password"])
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    @allure.title("Логин курьера с отсутствующим паролем")
    def test_login_courier_withot_password_is_denied(self):
        login_courier = CourierMeth().login_courier(courier_credentials["login"], "")
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    @allure.title("Логин курьера с отсутствующим логином и паролем")
    def test_login_courier_withot_login_and_password_is_denied(self):
        login_courier = CourierMeth().login_courier("", "")
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    @allure.title("Логин курьера с неверным логином")
    def test_login_courier_with_incorrect_login_is_denied(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"][1:], courier_credentials["password"]
        )
        assert (
            login_courier[0] == 404
            and login_courier[1]["message"] == "Учетная запись не найдена"
        )

    @allure.title("Логин курьера с неверным паролем")
    def test_login_courier_with_incorrect_password_is_denied(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"], courier_credentials["password"][1:]
        )
        assert (
            login_courier[0] == 404
            and login_courier[1]["message"] == "Учетная запись не найдена"
        )
