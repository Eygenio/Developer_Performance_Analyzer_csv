import csv
from pathlib import Path

import pytest

from devreport.reader import read_csv_files, CSVReadError


def write_csv(path: Path, rows):
    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["name", "position", "completed_tasks", "performance", "skills", "team", "experience_years"]
        )
        for row in rows:
            writer.writerow(row)


def test_read_valid_and_invalid(file_path):
    valid = ["Alex", "Backend Developer", "10", "4.5", "Python", "API", "3"]
    invalid_conv = ["Bob", "Backend Developer", "ten", "4.5", "Python", "API", "3"]
    file = file_path / "data.csv"
    write_csv(file, [valid, invalid_conv])

    developers, bad_rows = read_csv_files([str(p)])
    assert len(developers) == 1
    assert developers[0].name == "Alex"
    assert len(bad_rows) == 1
    assert "_error" in bad_rows[0]


def test_file_not_found():
    with pytest.raises(CSVReadError):
        read_csv_files(["nonexistent_file.csv"])
