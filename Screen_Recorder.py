#Importing the required packages 
import cv2
import numpy as np
import pyautogui

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*'mp4v')

filename = "Recording.mp4"    #Specifying the name of outpput fimename

fps = 60.0      #Frame Rate

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow('Live',cv2.WINDOW_NORMAL)

cv2.resizeWindow('Live',480, 270)

while True:
    img = pyautogui.screenshot()    #Will Take SS using Pyautogui

    frame = np.array(img)    #Convert the ScreenShots into 'numpy' array

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)     #Convert the BGR(Blue, Green, Red) to RGB(Red, Green, Blue)

    out.write(frame)

    cv2.imshow('Live',frame)

    #By pressing 'Q' or 'q' button the Recording will stop !
    if cv2.waitKey(1)==ord('q' or 'Q'):
        break
  
cv2.destroyAllWindows   #Destroy all the Windows
