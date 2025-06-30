BASE_URL = "https://qa-scooter.praktikum-services.ru"

courier_credentials = {
    "login": "czdtkhxfow",
    "password": "ozeiyzlfly",
    "firstName": "htndblgagu",
}
curier_id = 555656

ORDER_DATA_NO_COLOR = []
ORDER_DATA_BLACK = ["BLACK"]
ORDER_DATA_GREY = ["GREY"]
ORDER_DATA_BOTH = ["BLACK", "GREY"]

curier_creation_answer = '{"ok":true}'
curier_already_exist_answer = (
    '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
)
curier_creation_missed_data_answer = (
    '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
)
