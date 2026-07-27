import os
import subprocess
import sys

if not os.path.isdir("FlyRank-AI-Internship"):
    subprocess.run([
        "git",
        "clone",
        "https://github.com/rishh19/FlyRank-AI-Internship"
    ])

os.chdir("FlyRank-AI-Internship")

print(os.getcwd())
