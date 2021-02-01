from typing import TYPE_CHECKING
import cv2
import numpy as np

def __main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break
        img15 = getGaussian(img, 15)
        img05 = getGaussian(img, 5)
        cv2.imshow("15x15", img15)
        cv2.imshow("5x5",   img05)
        if cv2.waitKey(10) > -1:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def getGaussian(img, k):
    # カーネルサイズ
    ksize = (k, k)
    # sigmaX, sigmaYは通常は０にしておく
    # 値を大きくするとぶれていく
    img   = cv2.GaussianBlur(src = img, ksize = ksize, sigmaX = 0, sigmaY = 0)

    return img

if __name__ == "__main__":
    print(cv2.__version__)
    __main()



