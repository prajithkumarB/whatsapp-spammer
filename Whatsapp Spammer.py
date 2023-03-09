#developed by @prajithkumarB

#Instructions 
# 1. While entering the number of times you need to open the person's whatsapp chat and run the program

# 2. Then just click on the text feild then the program will be automatically executed  

import pyautogui as pt
import time 

limit =input("Enter the limit of message:")
message = input("Enter the message to send:")
i = 0

time.sleep(3)

while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i+=1

#developed by @prajithkumarB
