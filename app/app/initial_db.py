import logging
import os
import sqlite3
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    conn = sqlite3.connect('test.db')
    conn.close()


def main() -> None:
    logger.info("Creating db")
    init()
    logger.info("Initial db created")


if __name__ == "__main__":
    main()
