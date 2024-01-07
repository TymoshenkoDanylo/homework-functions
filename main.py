# # Завдання 1
# # Напишіть функцію, яка обчислює добуток елементів списку цілих.
# # Список передається як параметр. Отриманий результат повертається із функції.
#
# import random
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
#
# def product(new_list) -> int:
#     product_number = 1
#     for i in range(len(new_list)):
#         product_number *= new_list[i]
#
#     return product_number
#
#
# try:
#     product = product(number_list)
# except Exception as error:
#     print(f"ExceptionError: {error}")
#
# print(product)

