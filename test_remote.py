import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



# API configuration
api_url = "https://api.mistral.ai/v1/audio/transcriptions"
api_key = os.getenv("MISTRAL_API_KEY")

# Headers
headers = {
    "x-api-key": api_key
}

# File and model data
files = {
    'file': ('CAR0001.mp3', open('CAR0001.wav', 'rb'), 'audio/wav')
}

data = {
    'model': 'voxtral-mini-2507'
}

# Make the API request
try:
    response = requests.post(api_url, headers=headers, files=files, data=data, timeout=30)
    
    # Check if request was successful
    if response.status_code == 200:
        result = response.json()
        print("Transcription:", result)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    # save transcription to a file
    with open('transcription.txt', 'w') as f:
        f.write(str(result['text']))        
        
except FileNotFoundError:
    print("Error: CAR0001.mp3 file not found")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
finally:
    # Close the file if it was opened
    if 'files' in locals() and files['file'][1]:
        files['file'][1].close()