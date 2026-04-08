import requests

URL = "http://localhost:3000/speak"


def speak(text):
    try:
        requests.post(URL, json={"text": text}, timeout=0.2)
    except:
        # silently ignore if server not running
        pass