import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = f"{os.getenv('YOUGILE_BASE_URL')}/api-v2/auth/companies"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('YOUGILE_API_KEY')}"
}

response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")