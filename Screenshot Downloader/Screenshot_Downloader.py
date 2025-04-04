
import argparse
import pyautogui
import os
import time

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Screenshot Downloader"
    )
    parser.add_argument("--x", required=True, type=int)
    parser.add_argument("--y", required=True, type=int)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", required=True, type=int)
    args = parser.parse_args()

    x = args.x
    y = args.y
    width = args.width
    height = args.height

    # Create a folder to save screenshots
    save_folder = 'screenshots'
    os.makedirs(save_folder, exist_ok=True)

    # Take screenshots and press right arrow every 0.5 seconds
    try:
        while True:
            screenshot_num = 0
            screenshot_path = os.path.join(save_folder, f"{screenshot_num}.png")

            screenshot_num += 1

            # Capture the screen
            screenshot = pyautogui.screenshot(region=tuple[x, y, width, height])
            screenshot.save(screenshot_path)

            print(f"Saved: {screenshot_path}")

            # Simulate pressing the right arrow key
            pyautogui.press("right")
            print("Pressed right arrow key")

            time.sleep(0.5)  # Wait for 0.5 seconds before next cycle

    except KeyboardInterrupt:
        print("Stopped screenshot capturing.")
