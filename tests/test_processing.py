import sys
import os

# Добавляем путь к папке src, чтобы pytest мог найти модуль
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from processing import filter_by_state  # Убираем import sort_by_date, так как он не используется

# Пример данных
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
]


# Тест для фильтрации по состоянию
def test_filter_by_state():
    # Ожидаемый результат при фильтрации по состоянию "EXECUTED"
    assert filter_by_state(operations) == [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
    ]

    # Ожидаемый результат при фильтрации по состоянию "CANCELED"
    assert filter_by_state(operations, "CANCELED") == [
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"}
    ]
