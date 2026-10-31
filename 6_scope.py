"""
Задание 6. Область видимости.

1. ДО запуска предскажи вывод scope_demo() и print(value) после вызова.
   Запиши ответ и объяснение в комментарии.
2. Запусти файл и сравни с прогнозом.
3. Объясни, почему локальная переменная не меняет глобальную.
4. Реализуй increase(value, step=1), возвращающую увеличенное значение.
   Не используй global и не изменяй глобальные переменные.
5. В main() сохрани результат increase в локальную переменную.
6. Объясни в комментарии, почему имя local_result недоступно
   за пределами main(). Не оставляй в файле вызов, вызывающий NameError.
"""

value = 10


def scope_demo():
    value = 20
    print("Внутри scope_demo:", value)


def increase(value, step=1):
    return value + step


def main():
    scope_demo()
    print("После scope_demo:", value)
    local_result = increase(value, step=5)
    print("Результат increase:", local_result)
    print("Глобальное значение:", value)


if __name__ == "__main__":
    main()

