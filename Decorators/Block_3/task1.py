def dec(text: str):
    print(text)
    def func(a: int, b: int):
        return a + b
    return func

test = dec("Покупайте наших котиков!")
print(test(1, 2))
