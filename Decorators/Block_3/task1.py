def func(a, b):
    return a + b


def dec(func, text: str):
    def another_func(*args, **kwargs):
        print(text)
        return func(*args, **kwargs)

    return another_func


test = dec(func, "Покупайте наших котиков!")
print(test(1, 2))
