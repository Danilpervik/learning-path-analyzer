# src/analyzer.py

import pandas as pd
from scipy.stats import pearsonr

def compute_activity_grade_correlation(df: pd.DataFrame) -> dict:
    """Compute correlation between activity counts and grades."""
    # Подсчитываем количество каждого event_type по пользователю и курсу
    user_activity = (
        df.groupby(["user_id", "course_id"])["event_type"]
        .value_counts()
        .unstack(fill_value=0)
    )
    # Средняя оценка по пользователю и курсу
    grades = df.groupby(["user_id", "course_id"])["grade"].mean()

    # Объединяем
    merged = user_activity.join(grades, how="inner")

    correlations = {}
    for col in merged.columns:
        if col == "grade":
            continue
        x = merged[col]
        y = merged["grade"]

        # Пропускаем, если данные константны (дисперсия = 0)
        if x.nunique() < 2 or y.nunique() < 2:
            correlations[col] = 0.0  # или None, но лучше 0.0 для стабильности
        else:
            corr, _ = pearsonr(x, y)
            correlations[col] = float(round(corr, 3))
    return correlations