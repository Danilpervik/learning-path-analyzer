# tests/test_analyzer.py
import pandas as pd
from src.analyzer import compute_activity_grade_correlation

def test_correlation_output():
    data = {
        "user_id": ["u1", "u1", "u2", "u2"],
        "course_id": ["c1", "c1", "c1", "c1"],
        "event_type": ["quiz_attempt", "assignment_submission", "quiz_attempt", "assignment_submission"],
        "grade": [90, 95, 70, 75],
    }
    df = pd.DataFrame(data)
    corr = compute_activity_grade_correlation(df)
    assert "quiz_attempt" in corr
    assert "assignment_submission" in corr
    # Корреляция должна быть положительной (в этом примере — идеальная)
    assert corr["quiz_attempt"] > 0.9
