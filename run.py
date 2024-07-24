import time
from win10toast import ToastNotifier
from topnews import topStories

# Initialize ToastNotifier
toaster = ToastNotifier()

# Fetch news items
newsitems = [
    {
        "title": "The tiny Indian village claiming Kamala Harris as its own",
        "description": "Thulasendhrapuram, a tiny village around 300km from the south Indian city of Chennai (formerly Madras) and 14,000 km from Washington DC, is where Kamala Harris’ maternal grandparents were from."
    }
]

for newsitem in newsitems:
    try:
        # Show notification
        toaster.show_toast(newsitem['title'], newsitem['description'], duration=10)

        # Short delay between notifications
        time.sleep(15)  # 15 seconds
    except Exception as e:
        print(f"Error displaying notification: {e}")

# Optional: Sleep after showing all notifications to keep the script alive
time.sleep(10)
