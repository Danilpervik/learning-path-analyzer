from .parser import parse_lms_log
from .analyzer import compute_activity_grade_correlation
from .visualizer import plot_correlations


def analyze_data(filepath: str):
    df = parse_lms_log(filepath)
    corr = compute_activity_grade_correlation(df)
    plot_correlations(corr)
    return corr
