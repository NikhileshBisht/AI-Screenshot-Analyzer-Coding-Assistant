import requests

BOT_TOKEN = "xyz"
CHAT_ID = "zzz"


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message[:4000]  # Telegram limit
    }

    r = requests.post(url, json=payload)
    r.raise_for_status()