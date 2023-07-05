from datetime import datetime
import time

def wrapper(*agrs1, **kwargs1):
    def dec(func):
        cache = {}

        def another_func(*args, **kwargs):
            if "text" in kwargs1:
                print(kwargs1["text"])

            caching_time = 10
            if "caching_time" in kwargs1:
                caching_time = kwargs1["caching_time"]

            now = time.time()
            key = args + tuple(kwargs.keys())
            if key in cache.keys() and now - cache[key]["time"] <= caching_time:
                res = cache[key]["data"]
            else:
                res = func(*args, **kwargs)
                cache[key] = {"time": time.time(), "data": res}
                print("Выполнил")

            return res

        return another_func

    return dec


@wrapper(text="Покупайте наших котиков", caching_time=9)
def func(a, b):
    return a // b


print(func(4, 2))
time.sleep(10)
print(func(4, 2))
print(func(4, 2))
