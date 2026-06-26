import duckdb
import pandas as pd

class LocalEconomicPipeline:
    def __init__(self, db_path: str = "economic_intelligence.db"):
        self.conn = duckdb.connect(db_path)

    def extract_and_load_mock_data(self):
        print("í³¥ Extracting macro-economic indicators...")
        data = {
            "date": pd.date_range(start="2022-01-01", periods=12, freq="ME"),
            "inflation_rate": [5.7, 5.9, 6.1, 6.5, 7.4, 7.8, 7.6, 7.5, 7.2, 6.8, 6.7, 7.2],
            "gdp_growth": [1.2, 1.1, 0.8, -0.2, 0.4, 0.6, 0.5, -0.1, 0.2, 0.3, 0.5, 0.9]
        }
        df = pd.DataFrame(data)
        self.conn.execute("CREATE TABLE IF NOT EXISTS macro_indicators AS SELECT * FROM df")
        print("í²¾ Successfully loaded datasets into local warehouse table: macro_indicators")

if __name__ == "__main__":
    pipeline = LocalEconomicPipeline()
    pipeline.extract_and_load_mock_data()
