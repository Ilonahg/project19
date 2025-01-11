from typing import List, Dict


def filter_by_state(
    operations: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """
    Filters a list of operations by the given state.

    Args:
        operations (List[Dict]): List of operation dictionaries.
        state (str): The state to filter by. Defaults to 'EXECUTED'.

    Returns:
        List[Dict]: A filtered list of operations.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict], descending: bool = True
) -> List[Dict]:
    """
    Sorts a list of operations by date.

    Args:
        operations (List[Dict]): List of operation dictionaries.
        descending (bool): Sort order. Defaults to True.

    Returns:
        List[Dict]: A sorted list of operations.
    """
    return sorted(
        operations, key=lambda x: x.get("date", ""), reverse=descending
    )
