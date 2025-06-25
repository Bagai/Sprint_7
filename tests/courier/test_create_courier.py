from meth.courier_meth import CourierMeth
import allure


class TestCourierRegister:

    @allure.step("Создание курьера")
    def test_create_courier_is_created(self, generate_data_for_courier):
        created_courier = CourierMeth().create_courier(
            generate_data_for_courier[0],
            generate_data_for_courier[1],
            generate_data_for_courier[2],
        )
        assert created_courier[0] == 201 and created_courier[1] == '{"ok":true}'

    @allure.step("Создание курьера с тем же логином")
    def test_creating_courier_with_the_same_login_is_denied(
        self, generate_data_for_courier
    ):
        created_courier = CourierMeth().create_courier(
            generate_data_for_courier[0],
            generate_data_for_courier[1],
            generate_data_for_courier[2],
        )
        created_courier = CourierMeth().create_courier(
            generate_data_for_courier[0],
            generate_data_for_courier[1],
            generate_data_for_courier[2],
        )
        assert (
            created_courier[0] == 409
            and created_courier[1]
            == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
        )

    @allure.step("Создание курьера без логина")
    def test_creating_courier_without_login_is_denied(self, generate_data_for_courier):
        created_courier = CourierMeth().create_courier(
            "", generate_data_for_courier[1], generate_data_for_courier[2]
        )
        assert (
            created_courier[0] == 400
            and created_courier[1]
            == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
        )

    @allure.step("Создание курьера без пароля")
    def test_creating_courier_without_password_is_denied(
        self, generate_data_for_courier
    ):
        created_courier = CourierMeth().create_courier(
            generate_data_for_courier[0], "", generate_data_for_courier[2]
        )
        assert (
            created_courier[0] == 400
            and created_courier[1]
            == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
        )

    @allure.step("Создание курьера без имени")
    def test_creating_courier_without_first_name_is_denied(
        self, generate_data_for_courier
    ):
        created_courier = CourierMeth().create_courier(
            generate_data_for_courier[0],
            generate_data_for_courier[1],
            "",
        )
        assert created_courier[0] == 201 and created_courier[1] == '{"ok":true}'
