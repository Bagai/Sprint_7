from meth.courier_meth import CourierMeth
from data import courier_credentials


class TestCourierLogin:
    def test_login_courier_is_successful(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"], courier_credentials["password"]
        )
        print(login_courier)
        assert login_courier[0] == 200 and login_courier[1]["id"] is not None

    def test_login_courier_withot_login_is_denied(self):
        login_courier = CourierMeth().login_courier("", courier_credentials["password"])
        print(login_courier)
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    def test_login_courier_withot_password_is_denied(self):
        login_courier = CourierMeth().login_courier(courier_credentials["login"], "")
        print(login_courier)
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    def test_login_courier_withot_login_and_password_is_denied(self):
        login_courier = CourierMeth().login_courier("", "")
        print(login_courier)
        assert (
            login_courier[0] == 400
            and login_courier[1]["message"] == "Недостаточно данных для входа"
        )

    def test_login_courier_with_incorrect_login_is_denied(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"][1:], courier_credentials["password"]
        )
        print(login_courier)
        assert (
            login_courier[0] == 404
            and login_courier[1]["message"] == "Учетная запись не найдена"
        )
    def test_login_courier_with_incorrect_password_is_denied(self):
        login_courier = CourierMeth().login_courier(
            courier_credentials["login"], courier_credentials["password"][1:]
        )
        print(login_courier)
        assert (
            login_courier[0] == 404
            and login_courier[1]["message"] == "Учетная запись не найдена"
        )
