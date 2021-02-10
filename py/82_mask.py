import numpy as np
from numpy.core.defchararray import center
import cv2

data_dir = "docs/IF2101T/CQProjectBasics_1"

def __main():
    img = cv2.imread(data_dir + "/IMG_0260.JPG")

    img = getResize(img)
    org  = img.copy()
    mask = baseImage(img)

    imgMask = getMaskImg(img, mask)

    cv2.imshow("Original", org)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final result", imgMask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

def getMaskImg(img, mask):
    mask    = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    compImg = cv2.copyTo(src = img, mask = mask)
    return compImg

def getResize(src):
    basePixSize = 1280
    height, width, _ = src.shape
    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize
    dst = cv2.resize(
        src,
        (int(width * resizeRate), int(height * resizeRate)),  
        interpolation = None
    )
    return dst

def baseImage(img):
    height = img.shape[0]
    width  = img.shape[1]
    size = np.array([height, width, 3])
    img  = np.zeros(size, dtype = np.uint8)
    centerX = int(width / 2)
    centerY = int(height / 2)
    w = int(centerX * .6)
    h = int(centerY * .6)
    color = np.array([255., 255, 255.])
    cv2.ellipse(
        img = img, 
        center = (centerX, centerY), 
        axes = (w,h), 
        angle = 0, 
        startAngle = 0,
        endAngle = 360, 
        color = color, 
        thickness = -1,
        lineType = cv2.LINE_AA,
    )

    return img

if __name__ == "__main__":
    print(cv2.__version__)
    __main()

