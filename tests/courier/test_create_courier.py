from meth.courier_meth import CourierMeth
import allure
from helpers import generate_data_for_courier
from data import (
    curier_creation_answer,
    curier_already_exist_answer,
    curier_creation_missed_data_answer,
)

class TestCourierRegister:

    @allure.title("Стандартное успешное создание курьера")
    def test_create_courier_is_created(self):
        curier_data = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            curier_data[0],
            curier_data[1],
            curier_data[2],
        )
        assert (
            created_courier[0] == 201 and created_courier[1] == curier_creation_answer
        )

    @allure.title("Создание курьера с тем же логином")
    def test_creating_courier_with_the_same_login_is_denied(self):
        data_curier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            data_curier[0],
            data_curier[1],
            data_curier[2],
        )
        created_courier = CourierMeth().create_courier(
            data_curier[0],
            data_curier[1],
            data_curier[2],
        )
        assert (
            created_courier[0] == 409
            and created_courier[1] == curier_already_exist_answer
        )

    @allure.title("Создание курьера без логина")
    def test_creating_courier_without_login_is_denied(self):

        data_curier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            "", data_curier[1], data_curier[2]
        )
        assert (
            created_courier[0] == 400
            and created_courier[1] == curier_creation_missed_data_answer
        )

    @allure.title("Создание курьера без пароля")
    def test_creating_courier_without_password_is_denied(self):

        data_curier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            data_curier[0], "", data_curier[2]
        )
        assert (
            created_courier[0] == 400
            and created_courier[1] == curier_creation_missed_data_answer
        )

    @allure.title("Создание курьера без имени")
    def test_creating_courier_without_first_name_is_denied(self):
        data_curier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            data_curier[0],
            data_curier[1],
            "",
        )
        assert (
            created_courier[0] == 201 and created_courier[1] == curier_creation_answer
        )
