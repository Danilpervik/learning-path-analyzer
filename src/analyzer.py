import pandas as pd
from scipy.stats import pearsonr

def compute_activity_grade_correlation(df: pd.DataFrame) -> dict:
    """Compute correlation between activity counts and grades."""
    # Group by user + course
    user_activity = df.groupby(["user_id", "course_id"])["event_type"].value_counts().unstack(fill_value=0)
    grades = df.groupby(["user_id", "course_id"])["grade"].mean()
    
    # Merge
    merged = user_activity.join(grades, how="inner")
    
    correlations = {}
    for col in merged.columns:
        if col != "grade":
            corr, _ = pearsonr(merged[col], merged["grade"])
            correlations[col] = round(corr, 3)
    return correlations
