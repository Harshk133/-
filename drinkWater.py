import time
from win10toast import ToastNotifier

def notify_user():
    toaster = ToastNotifier()
    notification_title = 'पाणी प्या 💧'
    notification_message = 'पाणी पिण्याची वेळ आली आहे! हायड्रेटेड राहा.'
    
    toaster.show_toast(
        notification_title,
        notification_message,
        duration=10  # Notification will disappear after 10 seconds
    )

def main():
    interval_minutes = 30
    
    try:
        while True:
            notify_user()
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
