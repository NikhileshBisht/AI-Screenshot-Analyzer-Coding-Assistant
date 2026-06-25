import pyautogui
from datetime import datetime
import os
import requests
import base64
from PIL import Image
from telegram_utils import send_telegram

os.makedirs("screenshots", exist_ok=True)


def resize_image(path):
    img = Image.open(path)
    img.thumbnail((1280, 720))
    img.save(path)


def vision(image_path):
    try:
        with open(image_path, "rb") as f:
            image = base64.b64encode(f.read()).decode()

        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5vl:latest",
                "prompt": """
Read this screenshot carefully.

If it contains:
- LeetCode problems
- Competitive programming questions
- Error messages
- Code snippets

Extract the important information and problem statement.

Otherwise describe what is shown.
""",
                "images": [image],
                "stream": False
            },
            timeout=300
        )

        data = r.json()

        if "response" not in data:
            print("Vision Model Error:")
            print(data)
            return "Could not analyze screenshot."

        return data["response"]

    except Exception as e:
        return f"Vision Error: {e}"


def solve(problem):
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5-coder:14b",
                "prompt": f"""
You are an expert competitive programming assistant.

The screenshot content is:

{problem}

If this is a coding problem:
1. Explain the problem.
2. Give the optimal approach.
3. Provide a complete C++17 solution.
4. Provide time complexity.
5. Provide space complexity.

If this is not a coding problem:
Explain the content clearly.
""",
                "stream": False
            },
            timeout=300
        )

        data = r.json()

        if "response" not in data:
            print("Coder Model Error:")
            print(data)
            return "Failed to generate solution."

        return data["response"]

    except Exception as e:
        return f"Solver Error: {e}"


def take_screenshot():
    try:
        filename = (
            f"screenshots/"
            f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )

        pyautogui.screenshot().save(filename)

        resize_image(filename)

        print("\nReading screenshot...\n")

        text = vision(filename)

        print("Detected:")
        print(text)

        print("\nThinking...\n")

        answer = solve(text)

        print("\nAI Solution:\n")
        print(answer)

        try:
            send_telegram(answer)
            print("\nTelegram message sent!")
        except Exception as e:
            print(f"\nTelegram Error: {e}")

    except Exception as e:
        print(f"\nScreenshot Error: {e}")