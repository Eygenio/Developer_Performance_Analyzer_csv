from collections import defaultdict
from typing import Dict, Iterable, List, Tuple

from .models import Developer


def average(values: Iterable[float]) -> float:
    """Вычисляет среднее значение из чисел списка."""
    val = list(values)
    if not val:
        return 0.0
    return sum(val) / len(val)


def average_performance_by_position(developers: Iterable[Developer]) -> List[Tuple[str, float]]:
    """Возвращает список (position, average_performance), отсортированный по убыванию average_performance."""
    per_pos: Dict[str, List[float]] = defaultdict(list)
    for developer in developers:
        per_pos[developer.position].append(developer.performance)

    result = [(pos, round(average(score), 2)) for pos , score in per_pos.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    return result
