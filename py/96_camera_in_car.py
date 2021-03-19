import cv2
import numpy as np

frameCount = 0
thresRate = 150
speedList = np.array([])
aveSpeed = 0


def setSpeedMovie(img):
    global frameCount
    global aveSpeed

    height = img.shape[0]
    width  = img.shape[1]
    y = int(height * .8)
    x = int(width  * .5)
    h = y + 5
    w = x + int(width * .3)

    monitor = img[y:h, x:w]
    cv2.imshow("Monitor", monitor)
    monitor = cv2.cvtColor(monitor, cv2.COLOR_BGR2GRAY)
    _, monitor  = cv2.threshold(monitor, thresRate, 255, cv2.THRESH_BINARY)
    avePixelNum = np.average(monitor)

    # -------------------------------------------------------------------------
    # 10 / 255 で判定をしている
    # 基本的にはセンターラインでしか白色にならないのでこれで十分であると思う
    # -------------------------------------------------------------------------
    if avePixelNum > 10:
        frameCount += 1
    else:
        print(frameCount)
        if frameCount > 0:
            aveSpeed = getSpeed(frameCount)
        frameCount = 0

    # モニターがどこを見ているのかを確認するシステムになっているので
    # 基本的には
    cv2.imshow("Monitor", monitor)
    img = getResize(img)
    color = (255, 255, 255)
    cv2.putText(img, f"Speed {aveSpeed}Km/h", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)

    return img


def getSpeed(num):

    global speedList
    whiteLine = 8
    oneFrameSec = 1 / 30 # フレームレート
    whiteLinePassingSec = num * oneFrameSec # フレーム数を秒数に変換
    carSpeed = whiteLine / 1000 / whiteLinePassingSec * 60 * 60

    if carSpeed < 150:
        speedList = np.append(speedList, carSpeed)

    if speedList.size > 10:
        speedList = np.delete(speedList, 0)

    print(f"Speed = {np.average(speedList)} Count = {speedList.size}")

    return int(np.average(speedList))
    


def getResize(src):
    basePixSize = 1280
    height = src.shape[0]
    width  = src.shape[1]
    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize
    dst        = cv2.resize(src, (int(width  * resizeRate), int(height * resizeRate)), interpolation = None)
    return dst


if __name__ == "__main__":

    data_dir = "./docs/IF2101T/CQProjectApp"
    cap = cv2.VideoCapture(data_dir + "/" + "MVI_1186_Trim.mp4")
    
    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()
    
    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break
        img = setSpeedMovie(img)
        cv2.imshow("Speed", img)
        if cv2.waitKeyEx(10) > -1:
            break

    cap.release()
    cv2.destroyAllWindows()
