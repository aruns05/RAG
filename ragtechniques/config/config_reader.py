import os , sys
import logging

logger  = logging.getLogger(__name__)

from .config import config

class ConfigReader:
    def __init__(self):
        self.load_env_variables()

    def load_env_variables(self):
        config.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        config.GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
        if not config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in environment variables")
        
try:
    config_reader = ConfigReader()
    logger.info("Configuration loaded successfully.")
except Exception as e:
    logger.error(f"Error loading configuration: {e}")
    raise