from dataclasses import dataclass
from typing import List


@dataclass
class Developer:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: List[str]
    team: str
    experience_years: int

    @classmethod
    def from_dict(cls, row: dict) -> "Developer":
        """Создаем Developer из словаря (строки csv)."""
        try:
            name = row["name"]
            position = row["position"]
            completed_tasks = int(row["completed_tasks"])
            performance = float(row["performance"])
            skills = [i.strip() for i in row.get("skills", "").split(",") if i.strip()]
            team = row["team"]
            experience_years = int(row["experience_years"])
        except KeyError as e:
            raise ValueError(f"Отсутствует столбец: {e}") from e
        except (TypeError, ValueError) as e:
            raise ValueError(f"Ошибка конвертации: {e}") from e

        return cls(
            name=name,
            position=position,
            completed_tasks=completed_tasks,
            performance=performance,
            skills=skills,
            team=team,
            experience_years=experience_years,
        )
