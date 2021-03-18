import cv2
import numpy as np

data_dir = "./docs/IF2101T/CQProjectApp"

def __main() :
    img = cv2.imread(data_dir + "/" + "IMG_1610.JPG")
    img = getResize(img)
    dst = getFindContours(img)
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


def getFindContours(src):
    
    # グレー・スケール変換
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # ガウシアン・フィルタ
    ksize = (25, 25)
    gray = cv2.GaussianBlur(gray, ksize = ksize, sigmaX = 0, sigmaY = 0)

    # 二値化
    ret, c1img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("c1img", c1img)

    # 輪郭の検出
    contours, _ = cv2.findContours(image = c1img, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
    # contourIdxでどの輪郭を描画するのか調整が可能である．-1の場合にはすべての輪郭を描画する
    result = cv2.drawContours(image = src, contours = contours, contourIdx = -1, color = (0, 0, 255), thickness = 2, lineType = cv2.LINE_AA)
    cv2.imshow("result", result)

    for i, cont in enumerate(contours):
        # 四角で括れるエリアを検出
        rect = cv2.minAreaRect(cont)
        # 整数値に変換
        box  = cv2.boxPoints(rect)
        box  = np.int0(box)
        src  = cv2.drawContours(src, [box], -1, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.ellipse(src, rect, (0, 255, 255), 2)

    return src


if __name__ == "__main__":
    print(cv2.__version__)
    __main()

