import numpy as np
import cv2

data_dir = "./docs/IF2101T/CQProjectApp"

def __main():

    cap = cv2.VideoCapture(data_dir + "/" + "MVI_1592.MP4")
    
    if not cap.isOpened():
        print("Not Opened Vieo Camera")

    while True:
        ret, img = cap.read()
        img = getResize(img)
        org = img.copy()
        if not ret:
            print("Video Capture Err")
            break
        
        subImg = getBackgroundSubMog(org, img)
        cv2.imshow("bugs", subImg)
        cv2.imshow("org", org)
        if cv2.waitKeyEx(10) > -1:
            break
    cv2.destroyAllWindows()

    
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

def getBackgroundSubMog(org, img):

    global fgbg
    # 背景差分フィルタ
    # 戻り値には2値化されて差分が白で表現された画像が残る
    subImg = fgbg.apply(img)
    contours, hierarchy = cv2.findContours(image = subImg, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
    # 余りにも小さい変化は無視する
    contours = list(filter(lambda x: cv2.contourArea(x) > 30, contours))

    # for i, cont in enumerate(contours):
    #     # 四角で括れるエリアを検出
    #     rect = cv2.minAreaRect(cont)
    #     box  = cv2.boxPoints(rect)
    #     box  = np.int0(box)
    #     org  = cv2.drawContours(org, [box], -1, (255, 255, 0), 2, cv2.LINE_AA)

    # return org
    resultImg = cv2.drawContours(image = org, contours = contours, contourIdx = -1, color = (0, 0, 255), thickness = 2)
    return resultImg

if __name__ == "__main__":
    print(cv2.__version__)
    # history = 120とすることで120フレーム分を参照している
    fgbg = cv2.createBackgroundSubtractorMOG2(history = 240)
    # fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history = 240)

    __main()


