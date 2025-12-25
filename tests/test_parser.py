def test_missing_columns_raises_error():
    import pandas as pd
    from src.parser import parse_lms_log
    # Создаём CSV без нужного столбца
    bad_df = pd.DataFrame({"user_id": ["u1"], "timestamp": ["2024-01-01"]})
    bad_df.to_csv("data/bad_sample.csv", index=False)
    try:
        parse_lms_log("data/bad_sample.csv")
        assert False, "Should raise ValueError"
    except ValueError:
        pass
