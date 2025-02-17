import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")  # Overwrites the previous line
        time.sleep(1)
        seconds -= 1

    print("Time's up! ⏰")

if __name__ == "__main__":
    seconds = int(input("Enter countdown time in seconds: "))
    countdown_timer(seconds)
