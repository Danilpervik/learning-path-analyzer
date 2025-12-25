# scripts/generate_report.py
from src.main import analyze_data

if __name__ == "__main__":
    print("Running Learning Path Analyzer...")
    result = analyze_data("data/sample.csv")
    print("Correlations:", result)
    print("Report and graph saved to docs/")