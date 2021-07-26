import random
import time

print("Starting...")
def Slow_Writer(Text, multiplyer):
    i = 0

    try:
        multiplyer= int(multiplyer)
    except:
        multiplyer = 50

    if multiplyer < 1:
        multiplyer = 50
    for characters in Text:
        wait = (random.randint(1,10)) / int(multiplyer)
        time.sleep(wait)
        print(Text[i], end = "")
        i += 1
    if isinstance(multiplyer,str):
        print ("int")
    
    

if __name__ == "__main__":
    print("How slow? (Bigger number = faster text)")
    multiplyer = input()
    print("What do you want me to type?")
    text = input()
    Slow_Writer(text, multiplyer)
