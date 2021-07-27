import random
import time

print("Starting...")
def Slow_Writer(Text, multiplyer, range):
    i = 0

    def multiply(multiplyer):
        try:
            multiplyer= int(multiplyer)
        except:
            multiplyer = 50

        if multiplyer < 1:
            multiplyer = 50
        
        return multiplyer

    def rang(range):        
        try:
            range= int(range)
        except:
            range = 1
        
        if not (range < 10 and range > 0):
            range = 1

        return range
    
    multiplyer = multiply(multiplyer)
    range = rang(range)

    for characters in Text:
        wait = (int(random.randint(1,10**float(range)))) / int(multiplyer)
        time.sleep(wait)
        print(Text[i], end = "")
        # print(wait)
        i += 1

    # if isinstance(multiplyer,str):
    #     print ("int")
    
    

if __name__ == "__main__":
    print("How slow? (Bigger number = faster text)")
    multiplyer = input()
    print("how different?(1 and 2 are good. 3 and 4 are just stupid)")
    range = input()
    print("What do you want me to type?")
    text = input()
    Slow_Writer(text, multiplyer, range)
