import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

APP_TITLE = "SafeRoute AI"
APP_SUBTITLE = "Historical accident hotspot prediction for Indian road corridors"

ORIGINAL_DATASET_URL = (
    "https://raw.githubusercontent.com/madhan112007/road-accident-hotspot-prediction/" 
    "main/Dataset1%20Folder/indian_roads_dataset.csv"
)

DATA_DIR = BASE_DIR / "data"
DATA_PATH = DATA_DIR / "indian_roads_dataset.csv"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY", "")

MODEL_TARGET = "severity_high_risk"
