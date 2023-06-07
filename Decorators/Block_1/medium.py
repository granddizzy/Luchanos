# Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
# В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
# дополнительных аргументов. Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
# прокинуть в функцию только 1 аргумент
# прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
# создать кортеж со значениями и распаковать его при вызове функции с помощью *
# создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?


def test_func(arg_1: int, arg_2: int, arg_3: int, arg_4: int, *args: int) -> int:
    return arg_1 + arg_2 + arg_3 + arg_4 + sum(args)


print(test_func(1, 2, 3, 4, 5, 6, 7))

try:
    print(test_func(1))
except:
    print("Ошибка т.к. не переданы все обязательные аргументы (и в них не заданы значения по умолчанию)")

try:
    print(test_func(1, 2, 3, 4, arg_1=1, arg_2=2, arg_3=3, arg_4=4))
except:
    print("Unexpected argument")

numbers = (1, 2, 3, 4, 5, 6, 7)
print(test_func(*numbers))

numbers = {"arg_4": 4, "arg_2": 2, "arg_3": 3, "arg_1": 1}
try:
    print(test_func(*numbers))
except:
    print(
        "Ошибка т.к. * распакует только ключи словаря, которые передадутся как значения в аргументы функции как строки")

print(test_func(**numbers))
