from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
STATIC_DIR = BASE_DIR / "static"

STREAM_DELAY = 60
RETRY_TIMEOUT = 15000