from dotenv import load_dotenv
import os

load_dotenv()

IMAGE_HEIGHT = os.getenv('SCREENSHOT_HEIGHT')
IMAGE_WIDTH = os.getenv('SCREENSHOT_WIDTH')
IMAGE_PERCENTAGE = os.getenv('PERCENTAGE_SCREEN')
Footer