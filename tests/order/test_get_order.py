import pytest
from meth.order_meth import OrderMeth
import allure

class TestGetOrder:
    @allure.title("Получение заказа по id")
    def test_get_orders(self):
        response = OrderMeth().get_order()
        assert response[0] == 200 and response[1]["orders"] is not None