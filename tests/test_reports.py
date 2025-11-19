from devreport.reports import performance_report, format_performance_table
from devreport.models import Developer


def make_dev(name, pos, perf):
    return Developer(name=name, position=pos, completed_tasks=0, performance=perf, skills=[], team="", experience_years=0)


def test_performance_report_and_format():
    devs = [make_dev("A", "Backend", 4.5), make_dev("B", "Backend", 5.0), make_dev("C", "QA", 4.2)]
    data = performance_report(devs)
    table = format_performance_table(data)
    assert "Backend" in table
    assert "4.75" in table
    assert "4.20" in table
