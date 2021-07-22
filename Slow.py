import random
import time

print("Starting...")
def Slow_Writer(Text):
    i = 0
    for characters in Text:
        wait = (random.randint(1,10)) / 50
        time.sleep(wait)
        print(Text[i], end = "")
        i += 1


if __name__ == "__main__":
    print("What do you want me to type?")
    text = input()
    Slow_Writer(text)
