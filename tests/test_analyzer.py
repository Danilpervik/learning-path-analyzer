# tests/test_analyzer.py

import pandas as pd
from src.analyzer import compute_activity_grade_correlation


def test_correlation_output():
    data = {
        "user_id": ["u1", "u1", "u1", "u2", "u2", "u3"],
        "course_id": ["c1", "c1", "c1", "c1", "c1", "c1"],
        "event_type": [
            "quiz_attempt",
            "quiz_attempt",
            "assignment_submission",
            "quiz_attempt",
            "assignment_submission",
            "assignment_submission",
        ],
        "grade": [90, 90, 90, 70, 70, 50],  # одна оценка на пользователя
    }
    df = pd.DataFrame(data)
    corr = compute_activity_grade_correlation(df)

    assert "quiz_attempt" in corr
    assert "assignment_submission" in corr
    assert corr["quiz_attempt"] > 0.9   # будет ~0.98
    assert corr["assignment_submission"] < 0.5  # слабая связь (0,1,1 vs 90,70,50)