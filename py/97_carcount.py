import cv2
import numpy as np

data_dir = "./docs/IF2101T/CQProjectApp"

def __main():
    cap = cv2.VideoCapture(data_dir + "/" + "PXL_20201011_005931739.mp4")
    while True:
        ret, img = cap.read()
        if not ret:
            print("Vieo Capture Err")
            break

        img = getResize(img)
        img = getArea(img)
        cv2.imshow("Final result", img)
        if cv2.waitKey(10) > -1:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def getArea(img):
    # 判定サイズ
    w = 310
    h = 5
    # 内側 車線
    x1 = 570
    y1 = 630
    x2 = x1 + w
    y2 = y1 + h
    # 外側 車線
    x3 = 930
    y3 = 630
    x4 = x3 + w
    y4 = y3 + h

    area1 = img[y1:y2, x1:x2]
    area2 = img[y3:y4, x3:x4]
    area1 = getBackgroundSubMog(img, area1, 1)
    area2 = getBackgroundSubMog(img, area2, 2)
    img[y1:y2, x1:x2] = cv2.cvtColor(area1, cv2.COLOR_GRAY2BGR)
    img[y3:y4, x3:x4] = cv2.cvtColor(area2, cv2.COLOR_GRAY2BGR)

    return img

def getBackgroundSubMog(img, area, loadLine):
    global inside
    global outside
    global outsideZeroCount
    global insideZeroCount
    global fgbg

    # 差分を計算しているので変化があった場合には
    # 当該画素が白(255)になることを利用して変化をカウントする
    monitor = fgbg.apply(area)
    avePixelNum = np.average(monitor)
    print(f"Average = {avePixelNum}")

    # 外側
    if loadLine == 2:
        # ノイズを考慮するために5未満の場合を見通過フレーム（変化が起きていない）と見なす
        if avePixelNum < 5:
            outsideZeroCount += 1
        else:
            # 見通過フレームが5フレーム以上続いた上で，変化があった場合にカウントを行う
            if outsideZeroCount > 5:
                outside += 1
                outsideZeroCount = 0
    # 内側
    if loadLine == 1:
        if avePixelNum < 5:
            insideZeroCount += 1
        else:
            if insideZeroCount > 5:
                inside += 1
                insideZeroCount = 0
    
    cv2.putText(img=img, text="{0}".format(outside), org=(1100, 680), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5, color=(255, 255, 255), lineType=cv2.LINE_AA)
    cv2.putText(img=img, text="{0}".format(inside), org=(700, 680), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5, color=(255, 255, 255), lineType=cv2.LINE_AA)



    return monitor

def getResize(src):
    basePixSize = 1280
    height = src.shape[0]
    width  = src.shape[1]
    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize
    dst        = cv2.resize(src, (int(width  * resizeRate), int(height * resizeRate)), interpolation = None)
    return dst

if __name__ == "__main__":
    outside = 0
    inside  = 0
    outsideZeroCount = 0
    insideZeroCount  = 0
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history = 120)
    __main()


