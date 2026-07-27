import os
import sys
import subprocess

def setup_flyrank():
    """
    Clone the FlyRank repo (if needed), move into it,
    install required packages, and return the working directory.
    """

    REPO_URL = "https://github.com/rishh19/FlyRank-AI-Internship"
    REPO_DIR = "FlyRank-AI-Internship"

    # Clone only if it doesn't already exist
    if not os.path.exists(REPO_DIR):
        subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL],
            check=True
        )

    # Move into repo
    os.chdir(REPO_DIR)

    # Install packages
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
        ],
        check=True,
    )

    print("FlyRank setup completed.")
    print("Current directory:", os.getcwd())
