"""
Задание 5. Функции, параметры и return.

В main():
1. Вызови calculate_total с двумя аргументами и со всеми тремя.
2. Сделай вызов с именованными аргументами.
3. Сохрани возвращённое значение в переменную и используй в вычислении.
4. Напиши в комментариях, чем параметр отличается от аргумента,
   а print — от return.
Числа в заданиях неотрицательные, discount находится в диапазоне [0, 1].
"""


def calculate_total(price, quantity=1, discount=0):
    """Верни стоимость: цена * количество * (1 - скидка).
    discount=0.1 означает скидку 10%. Округление не требуется.
    calculate_total(100, 3, 0.1) -> 270.0
    """
    return price * quantity * (1 - discount)


def add_task(tasks, task):
    """Верни НОВЫЙ список: исходные задачи плюс task в конце.
    Исходный список не изменяй.
    """
    return tasks + [task]

def format_greeting(name, greeting="Привет"):
    """Верни строку, например "Привет, Анна!".
    format_greeting("Иван", greeting="Здравствуйте") -> "Здравствуйте, Иван!"
    """
    return f"{greeting}, {name}!"

def main():
    print("Без скидки:", calculate_total(100, 3))
    print("Со скидкой:", calculate_total(100, 3, 0.1))
    print("Именованные аргументы:", calculate_total(price=200, quantity=2, discount=0.25))
    print("Количество по умолчанию:", calculate_total(100))
    result = calculate_total(100, 3, 0.1)
    # После реализации calculate_total раскомментируй:
    print("Стоимость с доставкой:", result + 50)
    tasks = ["Изучить строки"]
    print("Новый список:", add_task(tasks, "Изучить функции"))
    print("Исходный список:", tasks)
    print(format_greeting("Анна"))
    print(format_greeting("Иван", greeting="Здравствуйте"))


if __name__ == "__main__":
    main()
