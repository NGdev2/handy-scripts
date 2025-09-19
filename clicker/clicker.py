from pynput.mouse import Listener, Controller, Button
import time

mouse = Controller()
click_position = None

def on_click(x, y, button, pressed):
    global click_position
    if pressed:
        click_position = (x, y)
        print(f"Position recorded: {click_position}")
        return False  # stop listener after first click

def main():
    # Ask how many clicks
    num_clicks = int(input("Enter number of clicks: "))

    print("Click once on the screen to set the position...")
    with Listener(on_click=on_click) as listener:
        listener.join()

    if click_position is None:
        print("No position recorded, exiting.")
        return

    print(f"Clicking {num_clicks} times at {click_position}...")
    mouse.position = click_position
    time.sleep(1)  # small delay before clicking

    for _ in range(num_clicks):
        mouse.click(Button.left, 1)
        time.sleep(0.05)  # delay between clicks

    print("Done.")

if __name__ == "__main__":
    main()
