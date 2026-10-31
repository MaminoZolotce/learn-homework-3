"""
Задание 4. Множества и кортежи.

1. Реализуй функции.
2. В main() создай кортеж ("Анна", 25, "Москва") и распакуй в три переменные.
3. В комментарии объясни отличие списка от кортежа.
4. Создай пустое множество и объясни, почему {} здесь не подходит.
"""


def compare_groups(first: list[str], second: list[str]):
    """Принимает два списка имён. Верни словарь с тремя множествами:
    common — имена в обеих группах;
    only_first — имена только в первой группе;
    all_names — все уникальные имена.
    Порядок элементов множеств не учитывается.
    """
    first, second = set(first), set(second)
    return {"common": first.intersection(second),
            'only_first': first.difference(second),
            'all_names': first.union(second),}


def get_bounds(numbers)-> tuple:
    """Верни кортеж (минимум, максимум).
    get_bounds([8, 2, 5]) -> (2, 8)
    Для пустого списка верни (None, None).
    """
    if not numbers:
        return None,None
    return min(numbers),max(numbers)



def main():
    print("Группы:", compare_groups(["Анна", "Иван"], ["Иван", "Олег"]))
    print("Пустые группы:", compare_groups([], []))
    print("Границы:", get_bounds([8, 2, 5]))
    print("Пустые границы:", get_bounds([]))
    # Добавь здесь создание и распаковку кортежа, пустое множество
    # и комментарии из условия.


if __name__ == "__main__":
    main()
