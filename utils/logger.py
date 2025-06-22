# utils/logger.py
from loguru import logger

logger.add("automation.log", rotation="1 MB")
