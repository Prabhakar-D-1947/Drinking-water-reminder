import time
import threading
import datetime
import winsound

import pystray
from PIL import Image, ImageDraw
from plyer import notification


# =========================
# SETTINGS
# =========================

INTERVAL = 30

stop_event = threading.Event()


# =========================
# CREATE ICON
# =========================

def create_icon():

    image = Image.new("RGB", (64, 64), "white")

    draw = ImageDraw.Draw(image)

    draw.ellipse(
        (16, 10, 48, 50),
        fill="blue"
    )

    return image


# =========================
# WATER REMINDER
# =========================

def water_reminder():

    while not stop_event.wait(INTERVAL):

        current_time = datetime.datetime.now()

        print(
            "Reminder:",
            current_time.strftime("%I:%M:%S %p")
        )

        notification.notify(
            title="💧 Water Reminder",
            message="It's time to drink some water!",
            timeout=10
                )
        winsound.Beep(500, 500)
        
        winsound.Beep(500, 500)
        
# =========================
# QUIT PROGRAM
# =========================

def quit_program(icon, item):

    print("Stopping Water Reminder...")

    # Tell reminder thread to stop
    stop_event.set()

    # Stop tray icon
    icon.stop()


# =========================
# MENU
# =========================

menu = pystray.Menu(

    pystray.MenuItem(
        "💧 Water Reminder",
        lambda: None
    ),

    pystray.MenuItem(
        "❌ Quit",
        quit_program
    )
)


# =========================
# START REMINDER THREAD
# =========================

reminder_thread = threading.Thread(
    target=water_reminder,
    daemon=True
)

reminder_thread.start()


# =========================
# START TRAY
# =========================

icon = pystray.Icon(
    "Water Reminder",
    create_icon(),
    "Water Reminder",
    menu
)

icon.run()


# =========================
# WAIT FOR REMINDER THREAD
# =========================

reminder_thread.join()

print("Water Reminder stopped.")


