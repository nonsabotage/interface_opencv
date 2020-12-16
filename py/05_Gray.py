import cv2
import numpy as np


def getGray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def createImage():
    width, height = 600, 480
    size = (height, width, 3)
    img  = np.zeros(size, dtype = np.uint8)
    rate = 255 / width
    for h in range(0, height):
        for w in range(0, width):
            data = int(w * rate)
            img[h, w] = np.full((3), data)   
    red   = np.array([0., 0., 255.])
    blue  = np.array([0., 255., 0.])
    green = np.array([255., 0., 0.])
    cyan    = np.array([255., 255., 0.])
    magenta = np.array([255., 0., 255.])
    yellow  = np.array([0., 255., 255.])

    # インデックスで領域を指定することが可能
    cv2.rectangle(img = img, pt1 = (0, 0),     pt2 = (200,200), color = red,     thickness = -1)
    cv2.rectangle(img = img, pt1 = (200, 0),   pt2 = (400,200), color = blue,    thickness = -1)
    cv2.rectangle(img = img, pt1 = (400, 0),   pt2 = (600,200), color = green,   thickness = -1)
    cv2.rectangle(img = img, pt1 = (0, 200),   pt2 = (200,400), color = cyan,    thickness = -1)
    cv2.rectangle(img = img, pt1 = (200, 200), pt2 = (400,400), color = magenta, thickness = -1)
    cv2.rectangle(img = img, pt1 = (400, 200), pt2 = (600,400), color = yellow,  thickness = -1)

    return img

if __name__ == "__main__":
    img = createImage()
    cv2.imshow("Original", img)

    img = getGray(img)
    cv2.imshow("Final result", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

