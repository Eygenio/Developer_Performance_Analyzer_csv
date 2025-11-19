from devreport.reports import performance_report, format_performance_table
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


def test_performance_report_and_format():
    developers = [make_developer(
        "A",
        "Backend",
        4.5
    ),
        make_developer(
            "B",
            "Backend",
            5.0
        ),
        make_developer(
            "C",
            "QA",
            4.2
        )
    ]

    data = performance_report(developers)
    table = format_performance_table(data)
    assert "Backend" in table
    assert "4.75" in table
    assert "4.20" in table
