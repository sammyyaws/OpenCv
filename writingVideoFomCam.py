import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def WriteVideo():
    root=os.getcwd()
    videoPath=os.path.join(root,"videos","websample.avi")
    cap=cv.VideoCapture(0)
    fourcc=cv.VideoWriter_fourcc(*'XVID')
    out=cv.VideoWriter(videoPath,fourcc,20.0,(640,480))

    if not cap.isOpened():
            print("Cant acess Camera")
            exit() 

    while cap.isOpened():
        ret,frame=cap.read()
        if ret :
           out.write(frame)
           cv.imshow("webcam",frame)
        if cv.waitKey(1)==ord("q"):
          break
    cap.release()
    out.release()
    cv.destroyAllWindows()        

if __name__=="__main__":
    WriteVideo()