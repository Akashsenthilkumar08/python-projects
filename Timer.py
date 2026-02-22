import time
def countdown_timer(seconds):
    while seconds > 0:
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")
total_seconds = int(input("Enter time in seconds: "))
countdown_timer(total_seconds)