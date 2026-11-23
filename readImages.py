import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt



def readImage():
    root=os.getcwd()
    imgPath=os.path.join(root,"images","cokebottle.jpg")
    img=cv.imread(imgPath)
    cv.namedWindow("img",cv.WINDOW_NORMAL)
    cv.resizeWindow("img", 600, 600)
    cv.imshow("img",img)
    cv.waitKey(0)
if __name__=="__main__":
 readImage()