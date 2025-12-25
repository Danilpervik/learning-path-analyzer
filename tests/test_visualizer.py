# tests/test_visualizer.py
import os
from src.visualizer import plot_correlations


def test_plot_correlations_creates_file():
    plot_correlations({"login": 0.2, "forum_post": 0.5})
    assert os.path.exists("docs/correlation.png")
