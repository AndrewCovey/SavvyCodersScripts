# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

def countdown(s,t):
    while s <= t:
        print(str(s) + " Mississippi")
        s+=1
        time.sleep(1)
    print("Ready or not here I come!")

countdown(1,5)