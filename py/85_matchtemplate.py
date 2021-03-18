import cv2
import numpy as np

data_dir = "docs/IF2101T/CQProjectBasics_1"

def __main():
    img = cv2.imread(data_dir + "/" + "IMG_1630_2.jpg")
    temple = cv2.imread(data_dir + "/" + "IMG_1630_2_T.jpg")
    h, w, _ = temple.shape

    result = cv2.matchTemplate(image = img, templ = temple, method = cv2.TM_CCOEFF)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    print(minVal, maxVal, minLoc, maxLoc)

    x, y = maxLoc
    color = np.array([0., 255., 255.])
    cv2.rectangle(img = img, pt1 = (x, y), pt2 = (x + w, y + h), color = color, thickness=3)

    cv2.imshow("Final result", img)
    cv2.imshow("Template", temple)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0

def getBinary(src):
    # カラーのまま二値化
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY)
    cv2.imshow('Bunary Color', c_dst)

    # グレーに変換した上で二値化
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', src)
    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY)

    return dst


if __name__ == "__main__":
    __main()

