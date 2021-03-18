import cv2
import webbrowser
import numpy as np


def getQRCode(img):
    global code
    try:
        data, point, qrcode = code.detectAndDecode(img = img)
    except Exception as e:
        print(e)
        data = ""
    
    print (f"data = {data}")
    return data

def __main():
    width = 1280.
    height = 720.
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():  # ビデオキャプチャー可能か判断
        print("Not Opened Video Camera")
        exit()

    margin = 100
    pt1 = np.array([(width/2) - margin, (height/2) - margin], dtype = np.int)
    pt2 = np.array([(width/2) + margin, (height/2) + margin], dtype = np.int)
    color = (255, 255, 255)

    while True:
        ret, img = cap.read()
        org = img.copy()
        img = cv2.flip(img, 1) # 画像の左右反転
        img = cv2.rectangle(img = img, pt1 = (pt1[0], pt1[1]), pt2 = (pt2[0], pt2[1]), color = color, thickness = 2)
        
        qrArea = org[pt1[1]:pt2[1], pt1[0]:pt2[0]]
        qrData = getQRCode(qrArea)
        if len(qrData) > 0:
            webbrowser.open(url = qrData, new = 1, autoraise = True)
            cv2.waitKey(0)
            break
        cv2.imshow("QRCode  Reader", img)
        if cv2.waitKey(10) > -1:
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    code = cv2.QRCodeDetector()
    __main()





