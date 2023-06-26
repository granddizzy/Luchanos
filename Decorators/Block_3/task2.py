def wrapper(*agrs1, **kwargs1):
    def dec(func):
        def another_func(*args, **kwargs):
            if "text" in kwargs1:
                print(kwargs1["text"])
            count = 0

            if "number_of_attempts" in kwargs1:
                number_of_attempts = kwargs1["number_of_attempts"]
            else:
                number_of_attempts = 10

            while count < number_of_attempts:
                try:
                    return func(*args, **kwargs)
                except:
                    count += 1

            raise Exception(f'Пробовал {count} раз. Ошибка')

        return another_func
    return dec


@wrapper(number_of_attempts=15, text="Покупайте наших котиков")
def func(a, b):
    return a // b

print(func(4, 0))