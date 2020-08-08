import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Drinking Water Notification",
            message="Its being one hour, Please Drink a glass of water. An average man should have atleast 4 litre of water every day, where as a average women should have atleast 3 litre of water everyday",
            app_icon='F:\drinkingwaternotificationusingpython\glass2.ico',
            timeout=12
        )
        time.sleep(6)