def func(a, b):
    return a // b


def dec(func, text: str, number_of_attempts: int = 10):
    def another_func(*args, **kwargs):
        print(text)
        count = 0
        while count < number_of_attempts:
            try:
                return func(*args, **kwargs)
            except:
                count += 1

        raise Exception(f'Пробовал {count} раз. Ошибка')

    return another_func


test = dec(func, "Покупайте наших котиков!")
print(test(1, 0))
