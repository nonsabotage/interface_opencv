import cv2
import numpy as np

data_dir = "docs/IF2101T/CQProjectApp"


def __main():
    img = cv2.imread(data_dir + "/" + "DSCF0769.JPG")
    img = getResize(img)
    img = getPeople(img)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0

def getResize(src):
    basePixSize = 1280
    height = src.shape[0]
    width  = src.shape[1]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, 
        (
            int(width  * resizeRate), 
            int(height * resizeRate)
        ), 
        interpolation = None
    )

    return dst

def getPeople(img):
    gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
    hog  = cv2.HOGDescriptor()
    hog.setSVMDetector(svmdetector = cv2.HOGDescriptor_getDefaultPeopleDetector())
    human, _ = hog.detectMultiScale(img = gray, winStride = (10, 10), padding = (15, 15), scale = None)
    for (x, y, w, h) in human:
        cv2.rectangle(
            img = img, 
            pt1 = (x, y), 
            pt2 = (x + w, y + h), 
            color = (0, 255, 255), 
            thickness = 3
        )

    return img


if __name__ == "__main__":
    print(cv2.__version__)

    __main()


