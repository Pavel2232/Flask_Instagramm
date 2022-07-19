from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.joinpath('data')

LOG_DIR = BASE_DIR.parent.joinpath('logs')
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE_PATH = BASE_DIR.parent.joinpath('logs', 'api.log')

loger_api = logging.getLogger()
loger_api.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_FILE_PATH)
loger_api.addHandler(file_handler)

console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter_one)
