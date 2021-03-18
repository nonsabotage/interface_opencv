import cv2
import numpy as np


data_dir = "./docs/IF2101T/CQProjectApp"

def __main():
    maxPhotoNum = 100

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print ("Video Capture Err")
            exit()
        
        dst = setResultArea(img)
        getface(dst)
        x1, y1, x2, y2 = init(img)
        img[y1:y2, x1:x2] = dst
        cv2.rectangle(img, (50, 50), (330, 120), (0, 0, 0), -1)
        cv2.putText(
            img = img, 
            text = "{0}/{1}".format(str(faceCount).zfill(3), maxPhotoNum), 
            org = (80, 100), 
            fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale = 1.5, 
            color = (255, 255, 255), 
            lineType = cv2.LINE_AA
        )
        cv2.imshow("Final rsult", img)
        if cv2.waitKey(10) > -1:
            break
        if faceCount >= maxPhotoNum:
            break
            
    cap.release()
    cv2.destroyAllWindows()

    return 0

def init(src):
    h = src.shape[0]
    w = src.shape[1]
    x = w / 2
    y = h / 2
    rectLenght = w * .3
    x1 = int(x - (rectLenght/2))
    y1 = int(y - (rectLenght/2))
    x2 = int(x + (rectLenght/2))
    y2 = int(y + (rectLenght/2))
    
    return x1, y1, x2, y2


def setResultArea(src):
    x1, y1, x2, y2 = init(src)
    dst = src[y1:y2, x1:x2]
    cv2.rectangle(src, (x1, y1), (x2, y2), (255, 255, 255), 2)

    return dst


def getface(img):
    global cascade
    gray = cv2.cvtColor(
        src = img, 
        code = cv2.COLOR_BGR2GRAY
    )
    bodyRect = cascade.detectMultiScale(
        image = gray, 
        scaleFactor = 1.05, 
        minNeighbors = 10, 
        flags = None, 
        minSize = (30, 30)
    )
    for x, y, w, h in bodyRect:
        face = img[y:y+h, x:x+w]
        saveImg(face)
        cv2.rectangle(
            img = img,
            pt1 = (x, y), 
            pt2 = (x + w, y + h), 
            color = (0, 255, 255), 
            thickness = 3
        )
    return img

def saveImg(src):
    global faceCount
    dst = setImageSize(src, faceCount)
    fileName = f"./facesimag/face{faceCount:03d}.jpg"
    cv2.imwrite(fileName, dst)
    faceCount += 1


def setImageSize(src, count):
    global height
    global width

    if count > 0:
        h = src.shape[0]
        w = src.shape[1]
        rate = height / h
        print(rate)
        src = cv2.resize(
            src, 
            (int(w * rate), int(h * rate))
        )
    else:
        height = src.shape[0]
        width  = src.shape[1]

    return src

if __name__ == "__main__":
    faceCount = 0
    height = 0
    width = 0
    cascade = cv2.CascadeClassifier(data_dir + "/SecurityCamera/haarcascade_frontalface_default.xml")
    __main()




