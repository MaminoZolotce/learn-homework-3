"""
Задание 2. Списки.

Не изменяй переданные списки. Используй циклы или списковые включения.
В main() проверь каждую функцию на обычном и пустом списке.
"""


def filter_scores(scores, minimum=60):
    """Верни новый список значений >= minimum, сохранив порядок.
    filter_scores([40, 60, 90, 55]) -> [60, 90]
    """
    return [score for score in scores if score >= minimum]

def unique_in_order(values):
    """Верни элементы без повторов в порядке первого появления.
    unique_in_order(["a", "b", "a", "c"]) -> ["a", "b", "c"]
    """
    check = []
    for i in values:
        if i not in check:
            check.append(i)

    return check



def summarize_numbers(numbers):
    """Верни словарь с ключами count, total, average.
    Для пустого списка: {"count": 0, "total": 0, "average": None}.
    summarize_numbers([2, 4, 6]) -> {"count": 3, "total": 12, "average": 4.0}
    """
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)

    return count, total, total/count

def main():
    print("Проходные баллы:", filter_scores([40, 60, 90, 55]))
    print("Другой порог:", filter_scores([40, 60, 90, 55], minimum=80))
    print("Пустые баллы:", filter_scores([]))
    print("Без повторов:", unique_in_order(["a", "b", "a", "c"]))
    print("Пустой список:", unique_in_order([]))
    print("Статистика:", summarize_numbers([2, 4, 6]))
    print("Пустая статистика:", summarize_numbers([]))


if __name__ == "__main__":
    main()
