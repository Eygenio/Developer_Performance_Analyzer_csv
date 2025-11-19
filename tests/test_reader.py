import csv
from pathlib import Path

import pytest

from devreport.reader import read_csv_files, CSVReadError


def write_csv(path: Path, rows):
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            ["name", "position", "completed_tasks", "performance", "skills", "team", "experience_years"]
        )
        for r in rows:
            writer.writerow(r)


def test_read_valid_and_invalid(tmp_path):
    valid = ["Alex", "Backend Developer", "10", "4.5", "Python", "API", "3"]
    invalid_conv = ["Bob", "Backend Developer", "ten", "4.5", "Python", "API", "3"]  # completed_tasks invalid
    p = tmp_path / "data.csv"
    write_csv(p, [valid, invalid_conv])

    developers, bad_rows = read_csv_files([str(p)])
    # one valid dev, one bad row
    assert len(developers) == 1
    assert developers[0].name == "Alex"
    assert len(bad_rows) == 1
    assert "_error" in bad_rows[0]


def test_file_not_found():
    with pytest.raises(CSVReadError):
        read_csv_files(["nonexistent_file.csv"])
