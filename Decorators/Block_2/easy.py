# Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.

count = 0

def func(a, b):
    global count
    count += 1
    return a + b

print(func(1, 3))
print(func(1, 3))
print(func(1, 3))
print(func(1, 3))
print(func(1, 3))
print(count)