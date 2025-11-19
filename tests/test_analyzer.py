from devreport.analyzer import average_performance_by_position
from devreport.models import Developer


def make_developer(name, position, performance):
    return Developer(
        name=name,
        position=position,
        completed_tasks=0,
        performance=performance,
        skills=[],
        team="",
        experience_years=0
    )


def test_compute_average_per_position():
    developers = [
        make_developer("A", "Backend", 4.5),
        make_developer("B", "Backend", 5.0),
        make_developer("C", "Frontend", 4.0),
    ]
    result = average_performance_by_position(developers)
    assert result[0][0] == "Backend"
    assert result[0][1] == 4.75
    assert result[1][0] == "Frontend"
    assert result[1][1] == 4.0
