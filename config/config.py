import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TRELLO_KEY")
api_token = os.getenv("TRELLO_TOKEN")
url_base = os.getenv("URL_BASE")

auth_params = {
    "key": api_key,
    "token": api_token
}