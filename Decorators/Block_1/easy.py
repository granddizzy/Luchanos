# Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
# а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
# Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
# Вызвать функцию суммирования через переменную, в которую вы только что её записали.

def test_func(text: str, number: int) -> str:
    lower_text = text.lower()
    upper_text = text.upper()
    return "".join([upper_text if i % 2 else lower_text for i in range(number)])


test = test_func
print(test)  # вижу ссылку на область памяти, где лежит функция test_func
print(test("test", 3))
