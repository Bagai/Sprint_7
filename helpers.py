# import random
# import string


# # метод регистрации нового курьера возвращает список из логина и пароля
# # если регистрация не удалась, возвращает пустой список
# def generate_data_for_register():
#     # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
#     def generate_random_string(length):
#         letters = string.ascii_lowercase
#         random_string = "".join(random.choice(letters) for i in range(length))
#         return random_string

#     # создаём список, чтобы метод мог его вернуть
#     login_pass = []

#     # генерируем логин, пароль и имя курьера
#     login = generate_random_string(10)
#     password = generate_random_string(10)
#     first_name = generate_random_string(10)

#     login_pass.append(login)
#     login_pass.append(password)
#     login_pass.append(first_name)

#     return login_pass
