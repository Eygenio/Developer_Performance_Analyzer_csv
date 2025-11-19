import argparse
import logging
import sys

from .reader import read_csv_files, CSVReadError
from .reports import ReportRegistry, format_performance_table


logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devreport",
        description="Анализ эффективности работы разработчика.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Путь к csv-файлу(ам).",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=ReportRegistry.available_reports(),   # <-- важно!
        help="Тип отчета (например: performance).",
    )
    parser.add_argument(
        "--show-bad-rows",
        action="store_true",
        help="Показывать строки csv, которые не прошли валидацию.",
    )
    return parser


def main(argv=None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        developers, bad_rows = read_csv_files(args.files)
    except CSVReadError as e:
        logger.error(f"Ошибка при чтении файлов: {e}.")
        return 2

    # Показывать ошибочные строки всегда, если попросили
    if args.show_bad_rows and bad_rows:
        logger.info("Проблемные строки (не прошли валидацию):")
        for row in bad_rows:
            logger.info(row)

    # Если нет валидных данных
    if not developers:
        logger.warning("Нет корректных данных для анализа.")
        return 0

    try:
        report_func = ReportRegistry.get(args.report)
    except Exception as e:
        logger.error(e)
        return 3

    report_data = report_func(developers)

    if args.report == "performance":
        output = format_performance_table(report_data)
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
