import pandas as pd

def parse_lms_log(filepath: str) -> pd.DataFrame:
    """Parse LMS log CSV into structured DataFrame."""
    df = pd.read_csv(filepath)
    required_cols = {"timestamp", "user_id", "event_type", "course_id"}
    if not required_cols.issubset(df.columns):
        raise ValueError("Missing required columns in CSV")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df
