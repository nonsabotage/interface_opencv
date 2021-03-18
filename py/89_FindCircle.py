import cv2
import numpy as np

data_dir = "./docs/IF2101T/CQProjectApp"

def __main() :
    img = cv2.imread(data_dir + "/" + "IMG_1610.JPG")
    img = getResize(img)
    dst = getCircles(img)
    cv2.imshow("Final result", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return None

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


def getCircles(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ksize = (25, 25)
    gray = cv2.GaussianBlur(gray, ksize, 0, 0)
    ret, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("Preimg", gray)

    # 円を検知した座標を取得する
    circles = cv2.HoughCircles(image = gray, method = cv2.HOUGH_GRADIENT, dp = 1, minDist = 20, param1 = 100, param2 = 20, minRadius = None, maxRadius = None)
    for circle in circles[0, :]:
        src = cv2.circle(
            img = src, 
            center = (circle[0], circle[1]), 
            radius = int(circle[2]), 
            color = (255, 0, 255), 
            thickness = 2
        )
    return src


if __name__ == "__main__":
    print(cv2.__version__)
    __main()


    