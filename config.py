import os
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv('OPEN_AI_KEY')
groq_cloud_key = os.getenv('GROQ_CLOUD_KEY')
