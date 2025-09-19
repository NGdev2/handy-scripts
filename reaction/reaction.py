from pynput.mouse import Listener, Controller, Button
from PIL import ImageGrab
import time

mouse = Controller()
click_position = None

def on_click(x, y, button, pressed):
    global click_position
    if pressed:
        click_position = (x, y)
        print(f"Position recorded: {click_position}")
        return False  # stop listener after first click

def get_pixel_color(x, y):
    # Capture 1 pixel area
    img = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return img.getpixel((0, 0))  # (R, G, B)

def wait_for_green(pos, tolerance=50):
    print("Waiting for green...")
    while True:
        color = get_pixel_color(*pos)
        r, g, b = color
        # Detect if green is dominant
        if g > r + tolerance and g > b + tolerance:
            print(f"Green detected at {pos} with color {color}")
            return
        time.sleep(0.01)  # check every 10ms

def main():
    print("Click once on the screen to set the position to monitor...")
    with Listener(on_click=on_click) as listener:
        listener.join()

    if click_position is None:
        print("No position recorded, exiting.")
        return

    # Wait for green pixel
    wait_for_green(click_position)

    # Click immediately
    mouse.position = click_position
    mouse.click(Button.left, 1)
    print("Clicked!")

if __name__ == "__main__":
    main()

# reaction time https://humanbenchmark.com/tests/reactiontime