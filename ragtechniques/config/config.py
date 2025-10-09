import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger  = logging.getLogger(__name__)

class Config:
    def __init__(self):
        self.OPENAI_API_KEY= None
        self.GCP_PROJECT_ID = None
        

config = Config()
