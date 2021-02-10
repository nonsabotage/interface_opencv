import cv2
import numpy as np
import random

def __main():
    size = np.array([720, 1280, 3])
    whiteColor = np.array([255., 255., 255.])
    wImg = np.full(size, whiteColor, dtype = np.uint8)

    blackColor = np.array([0., 0., 0.])
    bImg = np.full(size, blackColor, dtype = np.uint8)

    wImg = setCrossLines(wImg, blackColor)
    wOrg = wImg
    wDst = getMorpholigy(wImg)

    bImg = setCrossLines(bImg, whiteColor)
    bOrg = bImg
    bDst = getMorpholigy(bImg)

    cv2.imshow("White Original", wOrg)
    cv2.imshow("Black Original", bOrg)
    cv2.imshow("White result", wDst)
    cv2.imshow("Black result", bDst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# クロージング処理(白の膨張)
def getMorpholigy(img):
    kernel = np.ones((5,5), np.uint8)
    dst = cv2.morphologyEx(src = img, op = cv2.MORPH_CLOSE, kernel = kernel, iterations = 3)
    return dst

# ノイズの描画
def __setNoise(img, color):
    for num in range(400):
        x = int(random.uniform(10, 1270))
        y = int(random.uniform(10, 710))
        angle = (x, y, 3, 3)
        cv2.rectangle(img, angle, color, -1)

    return img


# クロスラインの描画
def setCrossLines(img, color):
    padding = 100
    border = 20
    height, width, channels = img.shape[:3]
    # 水平線
    img = cv2.line(img, (padding, int(height/2)), (width-padding, int(height/2)), color, border, cv2.LINE_AA)
    # 垂直線
    img = cv2.line(img, (int(width/2), padding), (int(width/2), height-padding), color, border, cv2.LINE_AA)
    # 斜線
    img = cv2.line(img, (padding, padding), (width-padding, height-padding), color, border, cv2.LINE_AA)

    __setNoise(img, color)

    return img

if __name__ == "__main__":
    print(cv2.__version__)
    __main()





