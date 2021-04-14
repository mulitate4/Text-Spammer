import pyautogui
from time import sleep



print("=======How it works======= - \nEnter the message to spam, \nclick on input box you want to spam. \nWait 10 seconds before script activates\nThen wait :)\n")
print("Enter the message to spam: ")
message = input()

print("Enter number of times to spam")
n = input()

for i in range(10,0,-1):
    print(f"waiting for {i} seconds")
    sleep(1)

for i in range(0, n):
    pyautogui.write(message)
    pyautogui.press('enter')
    sleep(0.05)
    