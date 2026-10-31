"""
Задание 3. Словари.

Данные корректны: age — целое число, churn — 0 или 1.
В main() создай минимум четыре словаря клиентов и проверь функции.
"""


def describe_client(client):
    """Верни строку "Анна, 25 лет, город: Москва".
    Обязательные ключи: name, age. Если city отсутствует, используй "не указан".
    """
    return f"{client["name"]}, {client["age"]}, {client.get("city", "не указан")}"


def count_by_city(clients):
    """Верни словарь: город -> число клиентов.
    У всех клиентов здесь есть ключ city.
    Для пустого списка верни {}. Исходные данные не изменяй.
    """
    result = {}
    for client in clients:
        city = client["city"]
        result["city"] = result.get(city, 0) + 1
    return result



def get_departed_names(clients):
    """Верни список имён клиентов с churn == 0 в исходном порядке.
    У каждого клиента есть name и churn. Для пустого списка верни [].
    """
    result = []
    for client in clients:
        if client["churn"] == 0:
            result.append(client)
    return result

def main():
    clients = [
        {"name": "Анна", "age": 25, "city": "Москва", "churn": 0},
        {"name": "Иван", "age": 32, "city": "Казань", "churn": 1},
        {"name": "Олег", "age": 40, "city": "Москва", "churn": 0},
        {"name": "Елена", "age": 28, "city": "Омск", "churn": 1},
    ]
    print("Клиент:", describe_client(clients[0]))
    print("Без города:", describe_client({"name": "Мария", "age": 35}))
    print("Клиенты по городам:", count_by_city(clients))
    print("Пустой список городов:", count_by_city([]))
    print("Ушедшие:", get_departed_names(clients))
    print("Нет клиентов:", get_departed_names([]))


if __name__ == "__main__":
    main()
