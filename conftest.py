import pytest
import random
import string
from datetime import datetime, timedelta


@pytest.fixture
def generate_data_for_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    return login_pass


@pytest.fixture
def generate_data_for_order():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_number(length):
        numbers = string.digits
        random_number = "".join(random.choice(numbers) for i in range(length))
        return random_number

    def generate_random_date():
        start_date = datetime(2023, 1, 1)
        end_date = datetime.now()

        def random_date(start, end):
            delta = end - start
            random_days = random.randint(0, delta.days)
            return start + timedelta(days=random_days)

        return random_date(start_date, end_date)

    # создаем список, чтобы метод мог его вернуть
    order_data = []
    # генерируем данные для заказа
    firstName = generate_random_string(10)
    lastName = generate_random_string(10)
    address = generate_random_string(10)
    metroStation = generate_random_string(10)
    phone = generate_random_number(10)
    rentTime = generate_random_number(2)
    deliveryDate = generate_random_date()
    comment = generate_random_string(30)
    order_data.append(firstName)
    order_data.append(lastName)
    order_data.append(address)
    order_data.append(metroStation)
    order_data.append(phone)
    order_data.append(rentTime)
    order_data.append(deliveryDate)
    order_data.append(comment)
    return order_data
