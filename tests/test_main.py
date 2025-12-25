# tests/test_main.py
from src.main import analyze_data

def test_analyze_data_returns_dict():
    result = analyze_data("data/sample.csv")
    assert isinstance(result, dict)
    assert len(result) > 0
