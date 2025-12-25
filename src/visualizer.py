import matplotlib.pyplot as plt
import os

def plot_correlations(correlations: dict, output_path: str = "docs/correlation.png"):
    activities = list(correlations.keys())
    values = list(correlations.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(activities, values, color="skyblue")
    plt.title("Correlation Between Activity Type and Grade")
    plt.ylabel("Pearson Correlation")
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    os.makedirs("docs", exist_ok=True)
    plt.savefig(output_path)
    plt.close()
