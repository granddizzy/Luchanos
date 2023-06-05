# Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
# первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов
# (если они есть), переданных по ключу (если они есть).

from random import randint as ri


def test_func_1(arg_1: int, arg_2: int, arg_3: int, arg_4: int, *args: int) -> int:
    return arg_1 + arg_2 + arg_3 + arg_4


def test_func_2(arg_1: int = 0,
                arg_2: int = 0,
                arg_3: int = 0,
                arg_4: int = 0,
                *args: int, **kwargs: int) -> int:
    return args[0] if len(args) > 0 else 0 + args[1] if len(args) > 1 else 0 + (
        kwargs[list(kwargs.keys())[ri(0, len(kwargs.keys()) - 1)]] if len(kwargs.keys()) > 0 else 0)


def test_func_3(*args,
                arg_1: int | None = None,
                arg_2: int | None = None,
                arg_3: int | None = None,
                arg_4: int | None = None,
                **kwargs) -> int:
    list_required_arguments = []
    if arg_1 is not None:
        list_required_arguments.append(arg_1)
    elif arg_2 is not None:
        list_required_arguments.append(arg_2)
    elif arg_3 is not None:
        list_required_arguments.append(arg_3)
    elif arg_4 is not None:
        list_required_arguments.append(arg_4)

    return args[0] if len(args) > 0 else 0 + args[1] if len(args) > 1 else 0 + (
        list_required_arguments[ri(0, len(list_required_arguments) - 1)] if len(list_required_arguments) > 0 else 0)


print(test_func_1(1, 2, 3, 4, 5, 6, 7))
print(test_func_2(5, 7))
print(test_func_3(1, 2, 3, 4, arg_2=5, arg_7=7))
