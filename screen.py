import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui
from time import sleep

bounding_box = {'top': 970, 'left': 972, 'width': 1, 'height': 1}

sct = mss()
sct_img = sct.grab(bounding_box)
x = sct_img.rgb

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    if sct_img.rgb != x:
        print(sct_img.rgb)  
        pyautogui.click() 
        sleep(0.5)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
