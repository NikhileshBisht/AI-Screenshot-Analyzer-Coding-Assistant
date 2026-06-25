import keyboard
import threading
from screenshot_utils import take_screenshot


def run():
    take_screenshot()


keyboard.add_hotkey(
    "F8",
    lambda: threading.Thread(target=run, daemon=True).start()
)

print("Press F8 to capture and analyze")
print("Press ESC to exit")

keyboard.wait("esc")