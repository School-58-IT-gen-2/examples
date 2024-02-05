import os
from dotenv import load_dotenv

load_dotenv()


super_secret_key = os.getenv("SUPER_SECRET_KEY")
