import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os 

def CapVideoFromWebcam():
    cap=cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cant acess Camera")
        exit()
    while(True):
        ret,frame=cap.read()
        if ret:
            cv.imshow("Webcam",frame)
        if cv.waitKey(1)==ord('q'):
          break
    cap.release()
    cv.destroyAllWindows()

def VideoFromFile():
    root=os.getcwd()
    VideoPath=os.path.join(root,"videos","vidsample.mp4")
    cap=cv.VideoCapture(VideoPath)

    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            cv.imshow("FileVid",frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()



if __name__=="__main__":
     #CapVideoFromWebcam()
     VideoFromFile()
