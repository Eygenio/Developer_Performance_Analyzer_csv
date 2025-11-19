import csv
import logging
from pathlib import Path
from typing import Iterable, Tuple, List

from .models import Developer


logger = logging.getLogger(__name__)


class CSVReadError(Exception):
    """Ошибки чтения csv (например, файл не найден или не удалось открыть)."""


def read_csv_files(file_paths: Iterable[str]) -> Tuple[List[Developer], List[dict]]:
    """Читаем csv файлы и возвращаем список Developer и список не конвертированных строк (value-error)."""
    developers = []
    bad_rows = []

    for i in file_paths:
        path = Path(i)
        if not path.exists():
            logger.error(f"Файл не найден: {i}")
            raise CSVReadError(f"Файл не найден: {i}")

        try:
            with path.open(newline="", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        dev = Developer.from_dict(row)
                        developers.append(dev)
                    except ValueError as e:
                        row_copy = dict(row)
                        row_copy["_error"] = str(e)
                        bad_rows.append(row_copy)
        except Exception as e:
            logger.exception(f"Ошибка открытия файла: {i}, {e}")
            raise CSVReadError(f"Ошибка открытия файла: {i}, {e}") from e

    return developers, bad_rows
