import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_TELE = os.getenv("TOKEN_TELE")
USERNAME_TELE = os.getenv("USERNAME_TELE")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")