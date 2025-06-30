import pytest
from meth.order_meth import OrderMeth
import allure
from helpers import generate_data_for_order

from data import ORDER_DATA_NO_COLOR, ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BOTH


class TestOrder:

    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize(
        "color",
        [ORDER_DATA_NO_COLOR, ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BOTH],
    )
    def test_creatin_order_now_color_successful(self, color):

        data_order = generate_data_for_order()
        response = OrderMeth().create_order(data_order, color)
        assert response[0] == 201 and response[1]["track"] is not None
