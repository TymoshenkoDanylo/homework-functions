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

# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
#
# import random
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
#
# def search_min(new_list) -> int:
#     min_number = min(new_list)
#     return min_number
#
#
# try:
#     search_min = search_min(number_list)
#     print(search_min)
# except Exception as error:
#     print(f"ExceptionError: {error}")


# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр.
# Отриманий результат повертається із функції.

# import random
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
#
# def count_prime(new_list):
#     count = 0
#     for i in new_list:
#         if prime(i):
#             count += 1
#
#     return count
#
#
# def prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
#
# try:
#     count_prime_numbers = count_prime(number_list)
#     print(count_prime_numbers)
# except Exception as error:
#     print(f"ExceptionError: {error}")


# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

# import random
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
#
#
# def remove_number(list_, number):
#     count = 0
#     for i in range(len(list_)):
#         if list_[i] == number:
#             list_.pop(i)
#             count += 1
#     return count
#
#
# try:
#     remove_number = remove_number(number_list, 3)
#     print(remove_number)
# except Exception as error:
#     print(f"ExceptionError: {error}")


# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр
# і повертає список, що містить елементи обох списків.

# import random
#
# first_letter = [random.randint(1, 5) for _ in range(5)]
# second_letter = [random.randint(1, 5) for _ in range(5)]
# print(first_letter)
# print(second_letter)
#
#
# def combine_lists(list1, list2):
#     return list(set().union(list1, list2))
#

# try:
#     combine_lists = combine_lists(first_letter,second_letter)
#     print(combine_lists)
# except Exception as error:
#     print(f"ExceptionError: {error}")


# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.
#
# import random
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
#
# def my_pow(lists, degree):
#     new_list = []
#     for i in lists:
#         new_list.append(i ** degree)
#     return new_list
#
#
# try:
#     my_pow = my_pow(number_list, 2)
#     print(my_pow)
# except Exception as error:
#     print(f"ExceptionError: {error}")
