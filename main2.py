import plyer
import time # set intervals i have to display the notifiation
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Hello",
            message = "Hello how are you, i hope you are fine",
            app_icon = 'F:\drinkingwaternotificationusingpython\gestures.ico',
            timeout = 30
        )
        time.sleep(60)
