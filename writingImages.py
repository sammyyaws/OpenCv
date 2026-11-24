import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def writeImage():
    root=os.getcwd()
    imgPath=os.path.join(root,"images","cokebottle.jpg")
    img=cv.imread(imgPath)
    ouputPath=os.path.join(root,"outputs","cokeCopy.jpg")
    cv.imwrite(ouputPath,img)




if __name__=="__main__":
    writeImage()