import os
import subprocess
import sys
import duckdb

from huggingface_hub import hf_hub_download

def setup_flyrank():

    IN_COLAB = "google.colab" in sys.modules

    REPO_URL = "https://github.com/rishh19/FlyRank-AI-Internship"
    REPO_DIR = "FlyRank-AI-Internship"

    if IN_COLAB:
        if not os.path.isdir(REPO_DIR):
            subprocess.run(
                ["git", "clone", "--depth", "1", REPO_URL, REPO_DIR],
                check=True,
            )
        os.chdir(REPO_DIR)

        from google.colab import userdata

        HF_TOKEN = userdata.get("HF_TOKEN")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "duckdb",
            "huggingface_hub",
            "pandas",
            "pyarrow",
            "scikit-learn",
        ]
    )

    path = hf_hub_download(
        repo_id="FlyRank/internship-warehouse",
        repo_type="dataset",
        filename="fact_content_daily_performance/month=2026-03/data_0.parquet",
        token=HF_TOKEN,
    )

    con = duckdb.connect()

    print("✅ FlyRank setup complete.")
    print("Current directory:", os.getcwd())

    return con, path
