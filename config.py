# config.py
import os

class Config:
    API_KEY = os.getenv('RIOT_API_KEY')
    DEBUG = True
