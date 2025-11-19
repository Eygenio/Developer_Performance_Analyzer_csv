from typing import Callable, Dict, Iterable, List, Tuple

from tabulate import tabulate

from .analyzer import average_performance_by_position
from .models import Developer


ReportFunc = Callable[[Iterable[Developer]], List[Tuple[str, float]]]


class UnknownReportError(ValueError):
    pass


class ReportRegistry:
    _registry: Dict[str, ReportFunc] = {}

    @classmethod
    def register(cls, name: str):
        """Декоратор для регистрации отчетов."""
        def decorator(func: ReportFunc):
            cls._registry[name] = func
            return func
        return decorator

    @classmethod
    def get(cls, name: str) -> ReportFunc:
        try:
            return cls._registry[name]
        except KeyError as exc:
            raise UnknownReportError(f"Unknown report: {name}") from exc

    @classmethod
    def available_reports(cls):
        return sorted(cls._registry.keys())


@ReportRegistry.register("performance")
def performance_report(developers: Iterable[Developer]) -> List[Tuple[str, float]]:
    """Регистрация performance отчета."""
    return average_performance_by_position(developers)


def format_performance_table(data: List[Tuple[str, float]]) -> str:
    """Функция формирования таблицы"""
    table_rows = []
    for idx, (position, perf) in enumerate(data, start=1):
        table_rows.append([str(idx), position, f"{perf:.2f}"])

    return tabulate(
        table_rows,
        headers=["#", "position", "performance"],
        tablefmt="grid",
        disable_numparse=True,
    )
