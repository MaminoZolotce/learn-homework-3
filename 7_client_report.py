"""
Задание 7. Итоговая задача: отчёт по клиентам.

Важно: churn = 0 — ушёл; churn = 1 — остался.
Данные корректны, все ключи присутствуют.

Реализуй функции так, чтобы build_report использовала вспомогательные функции.
Не используй pandas, global и изменение исходных данных.

Для CLIENTS в build_report ожидается:
total = 5
departed_count = 3
departed_share = 0.6 (доля от 0 до 1, не процент)
departed_names = ["Анна", "Олег", "Мария"]
cities = {"Москва", "Казань", "Омск"} (множество)
departed_by_city = {"Москва": 2, "Казань": 0, "Омск": 1}

Для пустого списка:
total и departed_count = 0, departed_share = 0.0;
departed_names = [], cities = set(), departed_by_city = {}.

В main() построй и выведи отчёт для CLIENTS и для [].
Для каждого шага объясни, почему выбран список, словарь или множество.
"""

CLIENTS = [
    {"name": "Анна", "age": 25, "city": "Москва", "churn": 0},
    {"name": "Иван", "age": 32, "city": "Казань", "churn": 1},
    {"name": "Олег", "age": 40, "city": "Москва", "churn": 0},
    {"name": "Елена", "age": 28, "city": "Омск", "churn": 1},
    {"name": "Мария", "age": 35, "city": "Омск", "churn": 0},
]


def get_departed(clients):
    """Верни список словарей ушедших клиентов в исходном порядке."""
    if not clients:
        return clients

    return [client for client in clients if client["churn"] == 0]


def calculate_departed_share(clients: list, length: int) -> float:
    """Верни долю ушедших среди всех клиентов. Для [] верни 0.0."""
    if not clients:
        return 0.0
    return 1/len(clients)*length

def count_departed_by_city(clients):
    """Верни словарь город -> число ушедших.
    Включи каждый город из clients, даже если ушедших в нём нет.
    """
    result = {}
    for client in clients:
        if client['churn'] == 0:
            result[client['city']] = result.get(client['city'], 0) + 1
        else:
            result[client['city']] = result.get(client['city'], 0)
    return result

def build_report(clients):
    """Верни словарь с шестью ключами, перечисленными в условии."""
    departed_clients = get_departed(clients)
    departed_share = calculate_departed_share(clients, len(departed_clients))
    departed_by_city = count_departed_by_city(clients)
    print(departed_clients, departed_share, departed_by_city, sep='\n')
    pass


def main():
    print("Отчёт по клиентам:", build_report(CLIENTS))
    print("Отчёт без клиентов:", build_report([]))


if __name__ == "__main__":
    main()
