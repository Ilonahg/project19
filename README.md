<<<<<<< HEAD
# project19
=======
# Проект: Виджет банковских операций

## Цель
Фильтрация и сортировка банковских операций.

## Установка
1. Установите Poetry: `pip install poetry`
2. Установите зависимости: `poetry install`

## Использование
```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
]

# Фильтрация
executed_ops = filter_by_state(operations)

# Сортировка
sorted_ops = sort_by_date(operations)
>>>>>>> 84acd4d (Initial commit)
