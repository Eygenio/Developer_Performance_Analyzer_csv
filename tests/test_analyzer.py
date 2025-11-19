from devreport.analyzer import average_performance_by_position
from devreport.models import Developer


def make_dev(name, pos, perf):
    return Developer(name=name, position=pos, completed_tasks=0, performance=perf, skills=[], team="", experience_years=0)


def test_compute_average_per_position():
    devs = [
        make_dev("A", "Backend", 4.5),
        make_dev("B", "Backend", 5.0),
        make_dev("C", "Frontend", 4.0),
    ]
    res = average_performance_by_position(devs)
    # ожидаем две строки, Backend первым (4.75), Frontend вторым (4.0)
    assert res[0][0] == "Backend"
    assert res[0][1] == 4.75
    assert res[1][0] == "Frontend"
    assert res[1][1] == 4.0
