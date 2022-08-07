#Notification
import os
import ctypes
from tracemalloc import start
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'There was an error processing your request. Please keep your volume up. Click on OK to continue.', 'ALERT', 0)
#sound
import winsound
winsound.Beep(1000, 5000)
#Interval of 10 seconds
import time
time.sleep(10)

#Flicker
import tkinter as tk
count = 7
while count != 0:
    root = tk.Tk()
    root.configure(bg='black')
    root.overrideredirect(True)
    root.state('zoomed')
    root.after(100, root.destroy) # set the flash time to 100 milliseconds
    root.mainloop()
    count-= 1
    time.sleep(0.75)

#Pause baby
time.sleep(4)

import pygame
def music(music):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
from playsound import playsound

#Access hacked
import cv2
import numpy as np
ok = r"C:\Users\hp\Desktop\New Microsoft PowerPoint Presentation.png"
img = cv2.imread(ok)
height, width, c = img.shape
 
i = 0
 
while True:
    i += 1
     
    # divided the image into left and right part
    # like list concatenation we concatenated
    # right and left together
    l = img[:, :(i % width)]
    r = img[:, (i % width):]
 
    img1 = np.hstack((r, l))
     
    # this function will concatenate
    # the two matrices
    cv2.imshow('ATTEMPT SUCCESSFUL', img1)
 
    if cv2.waitKey(1) == ord('a'):
       
        # press q to terminate the loop
        path = r"C:\Users\hp\Desktop\initiating.wav"
        music(path)
        winsound.Beep(100, 2000)
        break


time.sleep(2)

#SHUT DOWN SIKE
os.system("shutdown /s /t 1")
