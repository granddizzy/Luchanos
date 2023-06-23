# Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?


count = 0

def func2():
    # global count
    # count += 1
    # здесь счетчик сработает только один раз при запуске объемлющей функции
    # нужно перенести счетчик во вложенную функцию
    def func(a, b):
        global count
        count += 1
        return a + b

    return func

test = func2()

print(test(1, 3))
print(test(1, 3))
print(test(1, 3))
print(test(1, 3))
print(test(1, 3))
print(test(1, 3))
print(test(1, 3))
print(count)