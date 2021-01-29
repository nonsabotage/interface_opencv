from typing import TYPE_CHECKING
import cv2
import numpy as np

def __main():
    img = createPattern()
    org = img.copy()

    img = getResize(img)

    cv2.imshow("Original", org)
    cv2.imshow("INTER_LINEAR", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def getResize(src):
    basePixSize = 240
    height, width, _ = src.shape

    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize

    dst = cv2.resize(
        src,
        (int(width * resizeRate), int(height * resizeRate)),  
        interpolation = cv2.INTER_LINEAR,
    )

    return dst

def createPattern():
    square = 1000
    border = 2
    size   = np.array([square, square, 3])
    color  = np.array([255., 255., 255.])
    img    = np.full(size, color, dtype = np.uint8)

    # 斜め格子kパターン
    borderColor = (255, 0, 0)
    for wh in range(0, square, 10):
        cv2.line(
            img = img, 
            # (x, y)でポイントを指定するので，これは左下がりのパターンのはず（左上半分）
            pt1 = (wh, 0), 
            pt2 = (0, wh), 
            color = borderColor,
            thickness = border, 
            lineType = cv2.LINE_AA,
        )
    for wh in range(0, square, 10):
        cv2.line(
            img = img, 
            # (x, y)でポイントを指定するので，これは左下がりのパターンのはず（右下半分）
            pt1 = (square, wh), 
            pt2 = (wh, square), 
            color = borderColor,
            thickness = border, 
            lineType = cv2.LINE_AA,
        )

    borderColor = (255, 0, 255)
    for wh in range(square, 0, -10):
        cv2.line(
            img = img, 
            # (x, y)でポイントを指定するので，これは右下がりのパターンのはず（右上半分）
            pt1 = (wh, 0), 
            pt2 = (square, square - wh), 
            color = borderColor,
            thickness = border, 
            lineType = cv2.LINE_AA,
        )
    
    return img


if __name__ == "__main__":
    print(cv2.__version__)
    __main()



